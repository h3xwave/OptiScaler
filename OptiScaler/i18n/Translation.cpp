#include "pch.h"

#include "Translation.h"

#include "Util.h"

#include <algorithm>
#include <cctype>
#include <filesystem>
#include <fstream>
#include <functional>
#include <ranges>
#include <string_view>
#include <unordered_map>
#include <vector>

namespace
{
// Heterogeneous lookup so that translating a string never allocates.
struct TransparentStringHash
{
    using is_transparent = void;

    size_t operator()(std::string_view value) const noexcept { return std::hash<std::string_view> {}(value); }

    size_t operator()(const std::string& value) const noexcept
    {
        return std::hash<std::string_view> {}(std::string_view(value));
    }
};

using Table = std::unordered_map<std::string, std::string, TransparentStringHash, std::equal_to<>>;

Table g_table;
std::string g_language;
std::wstring g_fontPath;
bool g_active = false;
bool g_initialized = false;

// Rotating buffers for TranslateLabel(), which has to rebuild "translated##id".
// A ring avoids both allocations and clobbering a pointer that a caller still
// holds while it triggers a nested translated call.
std::string& NextLabelBuffer()
{
    constexpr size_t BufferCount = 8;
    thread_local std::string buffers[BufferCount];
    thread_local size_t index = 0;

    std::string& buffer = buffers[index];
    index = (index + 1) % BufferCount;
    return buffer;
}

// Compare the full printf conversion spelling and order, never only its count.
// This preserves va_list types, width/precision '*' arguments and positional indices.
bool CollectFormatSpecifiers(std::string_view text, std::vector<std::string_view>& specs)
{
    for (size_t i = 0; i < text.size(); ++i)
    {
        if (text[i] != '%')
            continue;

        const size_t start = i++;
        if (i == text.size())
            return false;
        if (text[i] == '%')
            continue;

        const size_t possiblePosition = i;
        while (i < text.size() && std::isdigit(static_cast<unsigned char>(text[i])))
            ++i;
        if (i < text.size() && text[i] == '$')
            ++i;
        else
            i = possiblePosition;

        while (i < text.size() && std::string_view("-+ #0'").find(text[i]) != std::string_view::npos)
            ++i;

        auto width = [&]()
            if (i < text.size() && text[i] == '*')
            {
                ++i;
                const size_t begin = i;
                while (i < text.size() && std::isdigit(static_cast<unsigned char>(text[i])))
                    ++i;
                if (i < text.size() && text[i] == '$')
                    ++i;
                else
                    i = begin;
            }
            else
            {
                while (i < text.size() && std::isdigit(static_cast<unsigned char>(text[i])))
                    ++i;
            }
        };
        width();
        if (i < text.size() && text[i] == '.')
        {
            ++i;
            width();
        }

        if (text.substr(i, 3) == "I64" || text.substr(i, 3) == "I32")
            i += 3;
        else if (text.substr(i, 2) == "hh" || text.substr(i, 2) == "ll")
            i += 2;
        else if (i < text.size() && std::string_view("hljztLI").find(text[i]) != std::string_view::npos)
            ++i;

        if (i >= text.size() || std::string_view("diuoxXfFeEgGaAcspnCSZ").find(text[i]) == std::string_view::npos)
            return false;

        specs.push_back(text.substr(start, i - start + 1));
    }
    return true;
}

bool HasCompatibleFormatSpecifiers(std::string_view source, std::string_view translated)
{
    std::vector<std::string_view> expected;
    std::vector<std::string_view> actual;
    return CollectFormatSpecifiers(source, expected) && CollectFormatSpecifiers(translated, actual) &&
           expected == actual;
}

std::string_view Trim(std::string_view value)
{
    while (!value.empty() && (value.front() == ' ' || value.front() == '\t' || value.front() == '\r'))
        value.remove_prefix(1);

    while (!value.empty() && (value.back() == ' ' || value.back() == '\t' || value.back() == '\r'))
        value.remove_suffix(1);

    return value;
}

// Expands the \n, \t and \\ escapes so that multi line tooltips can be written
// on a single line in the language file.
std::string Unescape(std::string_view value)
{
    std::string result;
    result.reserve(value.size());

    for (size_t i = 0; i < value.size(); ++i)
    {
        if (value[i] == '\\' && i + 1 < value.size())
        {
            switch (value[i + 1])
            {
            case 'n':
                result.push_back('\n');
                ++i;
                continue;
            case 't':
                result.push_back('\t');
                ++i;
                continue;
            case '\\':
                result.push_back('\\');
                ++i;
                continue;
            case '=':
                result.push_back('=');
                ++i;
                continue;
            default:
                break;
            }
        }

        result.push_back(value[i]);
    }

    return result;
}

bool LoadTable(const std::filesystem::path& path)
{
    std::ifstream file(path, std::ios::binary);
    if (!file.is_open())
        return false;

    // Skip a UTF-8 byte order mark. Notepad adds one by default.
    if (file.peek() == 0xEF)
    {
        char bom[3] {};
        file.read(bom, 3);

        const bool isUtf8Bom = file.gcount() == 3 && static_cast<unsigned char>(bom[1]) == 0xBB &&
                               static_cast<unsigned char>(bom[2]) == 0xBF;

        if (!isUtf8Bom)
        {
            file.clear();
            file.seekg(0);
        }
    }

    std::string line;
    int lineNumber = 0;
    int accepted = 0;
    int rejected = 0;

    while (std::getline(file, line))
    {
        ++lineNumber;

        const std::string_view trimmed = Trim(line);
        if (trimmed.empty() || trimmed.front() == '#' || trimmed.front() == ';')
            continue;

        size_t separator = std::string_view::npos;
        for (size_t i = 0; i < trimmed.size(); ++i)
        {
            if (trimmed[i] == '\\' && i + 1 < trimmed.size())
            {
                ++i;
                continue;
            }
            if (trimmed[i] == '=')
            {
                separator = i;
                break;
            }
        }
        if (separator == std::string_view::npos)
        {
            LOG_WARN("i18n: line {} has no '=' separator, skipped", lineNumber);
            ++rejected;
            continue;
        }

        // Spaces around the '=' are ignored. The source side is otherwise taken
        // verbatim, because it has to match the C++ literal exactly.
        const std::string source = Unescape(Trim(trimmed.substr(0, separator)));
        const std::string target = Unescape(Trim(trimmed.substr(separator + 1)));

        if (source.empty() || target.empty())
        {
            ++rejected;
            continue;
        }

        if (!HasCompatibleFormatSpecifiers(source, target))
        {
            LOG_WARN("i18n: line {} has incompatible printf format specifiers, skipped", lineNumber);
            ++rejected;
            continue;
        }

        g_table.insert_or_assign(source, target);
        ++accepted;
    }

    LOG_INFO("i18n: {} entries accepted, {} rejected from {}", accepted, rejected, wstring_to_string(path.wstring()));

    return accepted > 0;
}

std::string DetectSystemLanguage()
{
    wchar_t name[LOCALE_NAME_MAX_LENGTH] {};

    if (GetUserDefaultLocaleName(name, LOCALE_NAME_MAX_LENGTH) > 0)
        return wstring_to_string(name);

    return {};
}

std::filesystem::path ResolveLanguageFile(const std::string& code)
{
    const std::filesystem::path directory = Util::DllPath().parent_path() / L"lang";

    std::vector<std::filesystem::path> candidates;
    candidates.push_back(directory / (string_to_wstring(code) + L".txt"));

    // Fall back to the bare language part so that "zh-CN" also finds "zh.txt".
    const size_t dash = code.find('-');
    if (dash != std::string::npos && dash > 0)
        candidates.push_back(directory / (string_to_wstring(code.substr(0, dash)) + L".txt"));

    for (const auto& candidate : candidates)
    {
        std::error_code error;
        if (std::filesystem::exists(candidate, error) && !error)
            return candidate;
    }

    return {};
}

// The bundled Hack font has no CJK glyphs, so a translation needs a system font
// that does. Ordered by how good they look at small overlay sizes.
std::wstring FindCjkFont()
{
    static const wchar_t* const candidates[] = {
        L"msyh.ttc",   // Microsoft YaHei
        L"msyhbd.ttc", // Microsoft YaHei Bold
        L"deng.ttf",   // DengXian
        L"simhei.ttf", // SimHei
        L"simsun.ttc", // SimSun
        L"simkai.ttf", // KaiTi
    };

    wchar_t windowsDirectory[MAX_PATH] {};
    const UINT length = GetWindowsDirectoryW(windowsDirectory, MAX_PATH);

    if (length == 0 || length >= MAX_PATH)
        return {};

    const std::filesystem::path fontDirectory = std::filesystem::path(windowsDirectory) / L"Fonts";

    for (const wchar_t* candidate : candidates)
    {
        std::error_code error;
        const std::filesystem::path path = fontDirectory / candidate;

        if (std::filesystem::exists(path, error) && !error)
            return path.wstring();
    }

    return {};
}

bool IsDisabledCode(const std::string& code)
{
    std::string lower = code;
    std::ranges::transform(lower, lower.begin(), [](unsigned char c) { return (char) std::tolower(c); });

    return lower.empty() || lower == "none" || lower == "off" || lower == "en";
}
} // namespace

void Tr::Initialize()
{
    if (g_initialized)
        return;

    g_initialized = true;

    std::string code;

    const auto& configured = Config::Instance()->Language;
    if (configured.has_value())
        code = configured.value();
    else
        code = DetectSystemLanguage();

    if (IsDisabledCode(code))
    {
        LOG_INFO("i18n: inactive, language '{}'", code);
        return;
    }

    const std::filesystem::path file = ResolveLanguageFile(code);
    if (file.empty())
    {
        LOG_INFO("i18n: no translation file for '{}' in the lang folder", code);
        return;
    }

    if (!LoadTable(file))
    {
        LOG_WARN("i18n: '{}' contained no usable entries", wstring_to_string(file.wstring()));
        return;
    }

    g_language = code;
    g_fontPath = FindCjkFont();
    g_active = true;

    LOG_INFO("i18n: active, language '{}', {} entries, font '{}'", g_language, g_table.size(),
             g_fontPath.empty() ? std::string("<bundled>") : wstring_to_string(g_fontPath));

    InstallImGuiHooks();
}

const char* Tr::Translate(const char* text)
{
    if (text == nullptr || !g_active)
        return text;

    const auto entry = g_table.find(std::string_view(text));
    if (entry == g_table.end())
        return text;

    return entry->second.c_str();
}

const char* Tr::TranslateRange(const char* text, size_t length)
{
    if (text == nullptr || !g_active)
        return nullptr;
    const auto entry = g_table.find(std::string_view(text, length));
    return entry == g_table.end() ? nullptr : entry->second.c_str();
}

const char* Tr::TranslateLabel(const char* label)
{
    if (label == nullptr || !g_active)
        return label;
    const std::string_view view(label);
    const size_t idSeparator = view.find("##");
    const auto entry = g_table.find(view.substr(0, idSeparator));
    if (entry == g_table.end())
        return label;

    std::string& buffer = NextLabelBuffer();
    buffer.assign(entry->second);
    buffer.append("###");
    buffer.append(view);
    return buffer.c_str();
}

bool Tr::IsActive() { return g_active; }

const std::string& Tr::Language() { return g_language; }

const std::wstring& Tr::FallbackFontPath() { return g_fontPath; }
