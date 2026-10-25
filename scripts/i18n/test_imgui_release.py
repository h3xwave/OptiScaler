#!/usr/bin/env python3
"""Headless MSVC /O2 /GL /LTCG regression test for the actual bundled ImGui.

Uses the production translation table/parser/lookup functions, omitting only
Windows application startup and font discovery. No Detours and no game required.
This checks emitted UI text, not screenshots or game compatibility.
"""
import os
import pathlib
import subprocess
import tempfile

ROOT = pathlib.Path(__file__).resolve().parents[2]

HARNESS = r'''
#include <functional>
#include <iostream>
#include <sstream>
#include <stdexcept>
#include <string>
#include "imgui/imgui.h"
#include "imgui/imgui_internal.h"
#include "i18n/Translation.h"

void LoadTranslationsForTest(const char* path);
void SetTranslationActiveForTest(bool active);

static void Check(bool ok, const char* message)
{
    if (!ok) throw std::runtime_error(message);
}

static void CheckText(const char* source, const std::function<void()>& draw)
{
    static int caseNumber = 0;
    ++caseNumber;
    const std::string translated = Tr::Translate(source);
    Check(translated != source, "Missing test translation");
    ImGui::LogToBuffer();
    draw();
    const std::string actual = GImGui->LogBuffer.c_str();
    ImGui::LogFinish();
    std::istringstream lines(translated);
    std::string line;
    while (std::getline(lines, line))
    {
        if (!line.empty() && actual.find(line) == std::string::npos)
        {
            std::cerr << "Untranslated rendered text for: " << source << "\nCaptured: " << actual << "\n";
            throw std::runtime_error("Widget bypassed translation");
        }
    }
    // CollapsingHeader's logger itself adds "### " decorations; only an
    // appended source identifier is a translation suffix leak.
    if (actual.find(std::string("###") + source) != std::string::npos)
    {
        std::cerr << "Case " << caseNumber << " leaked an ID: " << actual << "\n";
        throw std::runtime_error("Hidden ID leaked into rendered text");
    }
}

int main(int argc, char** argv)
{
    try
    {
        Check(argc == 2, "Expected language pack path");
        LoadTranslationsForTest(argv[1]);
        ImGui::CreateContext();
        ImGuiIO& io = ImGui::GetIO();
        io.IniFilename = nullptr;
        io.DisplaySize = ImVec2(1600, 1800);
        io.DeltaTime = 1.0f / 60.0f;
        // Headless 1.92 texture-capable backend: CPU glyph generation is enough;
        // no GPU texture upload or legacy font-atlas API is needed for text logs.
        io.BackendFlags |= ImGuiBackendFlags_RendererHasTextures;
        io.Fonts->AddFontDefault();
        ImGui::NewFrame();
        ImGui::SetNextWindowPos(ImVec2(0, 0));
        ImGui::SetNextWindowSize(ImVec2(1500, 1700));
        ImGui::Begin("Translation regression", nullptr, ImGuiWindowFlags_NoSavedSettings);

        const std::string dynamicMenu = "Menu";
        CheckText("Menu", [&] { ImGui::Button(dynamicMenu.c_str()); });
        CheckText("Save Settings", [] { ImGui::Button("Save Settings"); });
        CheckText("Close", [] { ImGui::SmallButton("Close"); });
        CheckText("Menu", [] { bool checked = false; ImGui::Checkbox("Menu##check", &checked); });
        CheckText("Menu", [] { ImGui::RadioButton("Menu##radio", false); });
        CheckText("Menu", [] { ImGui::Selectable("Menu##select"); });
        CheckText("Menu", [] { ImGui::SeparatorText("Menu"); });
        CheckText("Menu", [] { ImGui::TextLink("Menu"); });
        CheckText("Menu", [] { if (ImGui::TreeNode("Menu##tree")) ImGui::TreePop(); });
        CheckText("Menu", [] { ImGui::CollapsingHeader("Menu##header"); });
        CheckText("Menu", [] { if (ImGui::BeginCombo("##combo", "Menu")) ImGui::EndCombo(); });
        CheckText("Menu", [] { int value = 0; ImGui::SliderInt("Menu##slider", &value, 0, 10); });
        CheckText("Square", [] { float value = 0.0f; ImGui::SliderFloat("Corner Rounding##slider", &value, 0.0f, 16.0f, "Square"); });
        CheckText("Menu", [] { int value = 0; ImGui::InputInt("Menu##input", &value); });
        CheckText("Custom Font File", [] { char buf[32] = ""; ImGui::InputText("Custom Font File##text", buf, sizeof(buf)); });
        CheckText("Labels", [] { float rgb[3] = { 1.0f, 1.0f, 1.0f }; ImGui::ColorEdit3("Labels##color", rgb, ImGuiColorEditFlags_NoInputs); });
        CheckText("Menu", [] {
            if (ImGui::BeginTable("table", 1)) {
                ImGui::TableSetupColumn("Menu");
                ImGui::TableHeadersRow();
                ImGui::EndTable();
            }
        });
        CheckText("Menu", [] {
            const char bounded[] = { 'M', 'e', 'n', 'u' };
            ImGui::TextUnformatted(bounded, bounded + sizeof(bounded));
        });
        const char* fgTip = "Can be used with any FG Output\n\nRequires enabling FSR-FG in game settings\nSupports HUDless out of the box";
        CheckText(fgTip, [&] { ImGui::TextUnformatted(fgTip); });
        CheckText("Menu", [] { ImGui::Text("Menu"); });

        SetTranslationActiveForTest(false);
        ImGui::LogToBuffer();
        ImGui::Button("Save Settings");
        Check(std::string(GImGui->LogBuffer.c_str()).find("Save Settings") != std::string::npos,
              "Disabled translation changed the English fallback");
        ImGui::LogFinish();
        ImGui::End();
        ImGui::Render();
        ImGui::DestroyContext();
        std::cout << "PASS: 20 rendered-text checks and inactive fallback under /O2 /GL /LTCG\n";
        return 0;
    }
    catch (const std::exception& error)
    {
        std::cerr << error.what() << "\n";
        return 1;
    }
}
'''


def main():
    if os.name != "nt":
        raise SystemExit("This Release-path test requires Windows and MSVC")
    vswhere = pathlib.Path(os.environ["ProgramFiles(x86)"]) / "Microsoft Visual Studio/Installer/vswhere.exe"
    vs = subprocess.check_output([
        str(vswhere), "-latest", "-products", "*", "-requires",
        "Microsoft.VisualStudio.Component.VC.Tools.x86.x64", "-property", "installationPath"
    ], text=True).strip()
    if not vs:
        raise SystemExit("MSVC x64 tools not found")
    vcvars = pathlib.Path(vs) / "VC/Auxiliary/Build/vcvars64.bat"
    source = (ROOT / "OptiScaler/i18n/Translation.cpp").read_text(encoding="utf-8-sig")
    helpers = source[source.index("struct TransparentStringHash"):source.index("std::string DetectSystemLanguage()")]
    methods = source[source.index("const char* Tr::Translate(const char* text)"):]
    portable = (
        '#include <algorithm>\n#include <cctype>\n#include <filesystem>\n#include <fstream>\n'
        '#include <functional>\n#include <stdexcept>\n#include <string>\n#include <string_view>\n'
        '#include <unordered_map>\n#include <vector>\n#include "i18n/Translation.h"\n'
        '#define LOG_INFO(...)\n#define LOG_WARN(...)\nnamespace {\n' + helpers + '\n}\n' + methods +
        '\nvoid LoadTranslationsForTest(const char* path) {\n'
        'if (!LoadTable(std::filesystem::path(path))) throw std::runtime_error("Cannot load language pack");\n'
        'g_active = true; }\nvoid SetTranslationActiveForTest(bool active) { g_active = active; }\n'
    )
    # Guard the application-side path as well: formatting "%s" is not translation.
    menu = (ROOT / "OptiScaler/menu/menu_common.cpp").read_text(encoding="utf-8-sig")
    assert 'ShowTooltip(opt.tooltip.c_str());' in menu
    assert 'ImGui::TextUnformatted(Tr::Translate(tip));' in menu
    with tempfile.TemporaryDirectory(prefix="optiscaler-imgui-test-") as directory:
        work = pathlib.Path(directory)
        (work / "translation_test.cpp").write_text(portable, encoding="utf-8")
        (work / "harness.cpp").write_text(HARNESS, encoding="utf-8")
        imgui = ROOT / "OptiScaler/include/imgui"
        args = ["/nologo", "/EHsc", "/std:c++20", "/utf-8", "/MD", "/O2", "/GL",
                f'/I"{ROOT / "OptiScaler"}"', f'/I"{ROOT / "OptiScaler/include"}"',
                f'/I"{ROOT / "external/freetype"}"', "harness.cpp", "translation_test.cpp"]
        args += [f'"{imgui / name}"' for name in (
            "imgui.cpp", "imgui_draw.cpp", "imgui_widgets.cpp", "imgui_tables.cpp",
            "misc/freetype/imgui_freetype.cpp")]
        args += [f'"{ROOT / "external/freetype/freetype.lib"}"', "/Fe:imgui_test.exe", "/link", "/LTCG",
                 "user32.lib", "gdi32.lib", "shell32.lib", "imm32.lib"]
        (work / "build.rsp").write_text(" ".join(args), encoding="utf-8")
        (work / "build.cmd").write_text(
            f'@echo off\ncall "{vcvars}" >nul\nif errorlevel 1 exit /b %errorlevel%\n'
            'cl @build.rsp\nexit /b %errorlevel%\n', encoding="utf-8")
        subprocess.run(["cmd.exe", "/d", "/c", "build.cmd"], cwd=work, check=True)
        subprocess.run([str(work / "imgui_test.exe"), str(ROOT / "lang/zh-CN.txt")], cwd=work, check=True)


if __name__ == "__main__":
    main()
