#include "pch.h"

#include "Translation.h"

#include <detours/detours.h>
#include <imgui/imgui.h>

// Intercepts the ImGui widgets that take a label, so their visible text can be
// translated without touching a single call site in menu_common.cpp.
//
// ImGui::TextV() is deliberately NOT hooked here: it is patched directly in
// imgui_widgets.cpp instead. Release builds use /GL and the linker turns that into
// /LTCG, which is free to inline TextV into Text and every other caller. A Detours
// hook on TextV would then only cover a subset of the call sites, which is a silent
// and very confusing failure mode. Patching the function body cannot be inlined away.
//
// The widgets below are large enough (layout, input handling, drawing) that LTCG is
// unlikely to inline them, and a missed hook only leaves that one label in English.
namespace
{
    using TextUnformatted_t = void (*)(const char* text, const char* text_end);
    using SeparatorText_t = void (*)(const char* label);
    using Checkbox_t = bool (*)(const char* label, bool* v);
    using Button_t = bool (*)(const char* label, const ImVec2& size);
    using Selectable_t = bool (*)(const char* label, bool selected, ImGuiSelectableFlags flags, const ImVec2& size);
    using RadioButton_t = bool (*)(const char* label, bool active);
    using Combo_t = bool (*)(const char* label, int* current_item, const char* const items[], int items_count,
                             int popup_max_height_in_items);

    TextUnformatted_t o_TextUnformatted = nullptr;
    SeparatorText_t o_SeparatorText = nullptr;
    Checkbox_t o_Checkbox = nullptr;
    Button_t o_Button = nullptr;
    Selectable_t o_Selectable = nullptr;
    RadioButton_t o_RadioButton = nullptr;
    Combo_t o_Combo = nullptr;

    void hkTextUnformatted(const char* text, const char* text_end)
    {
        if (text == nullptr || !Tr::IsActive())
        {
            o_TextUnformatted(text, text_end);
            return;
        }

        // Whole string, no hidden id suffix.
        if (text_end == nullptr)
        {
            o_TextUnformatted(Tr::Translate(text), nullptr);
            return;
        }

        // ImGui::FindRenderedTextEnd() is the usual non-null text_end: it stops at a
        // "##id" marker or at the terminator, so the whole string is still a label.
        // Card titles in menu_common.cpp are drawn this way.
        if (*text_end == '\0' || (text_end[0] == '#' && text_end[1] == '#'))
        {
            const char* translated = Tr::TranslateLabel(text);
            o_TextUnformatted(translated, ImGui::FindRenderedTextEnd(translated));
            return;
        }

        // A genuine sub-range of a larger buffer, which is never a translation key.
        o_TextUnformatted(text, text_end);
    }

    void hkSeparatorText(const char* label)
    {
        o_SeparatorText(Tr::TranslateLabel(label));
    }

    bool hkCheckbox(const char* label, bool* v)
    {
        return o_Checkbox(Tr::TranslateLabel(label), v);
    }

    bool hkButton(const char* label, const ImVec2& size)
    {
        return o_Button(Tr::TranslateLabel(label), size);
    }

    bool hkSelectable(const char* label, bool selected, ImGuiSelectableFlags flags, const ImVec2& size)
    {
        return o_Selectable(Tr::TranslateLabel(label), selected, flags, size);
    }

    bool hkRadioButton(const char* label, bool active)
    {
        return o_RadioButton(Tr::TranslateLabel(label), active);
    }

    bool hkCombo(const char* label, int* current_item, const char* const items[], int items_count,
                 int popup_max_height_in_items)
    {
        return o_Combo(Tr::TranslateLabel(label), current_item, items, items_count, popup_max_height_in_items);
    }

    // Each hook gets its own transaction so that a single failure (a function too small
    // for a trampoline, for instance) cannot take the remaining hooks down with it.
    template <typename T> bool AttachOne(T& original, PVOID hook, const char* name)
    {
        if (original == nullptr)
            return false;

        if (DetourTransactionBegin() != NO_ERROR)
            return false;

        DetourUpdateThread(GetCurrentThread());

        if (DetourAttach(&(PVOID&) original, hook) != NO_ERROR)
        {
            DetourTransactionAbort();
            LOG_WARN("i18n: could not hook ImGui::{}", name);
            return false;
        }

        if (DetourTransactionCommit() != NO_ERROR)
        {
            LOG_WARN("i18n: could not commit the ImGui::{} hook", name);
            return false;
        }

        return true;
    }
}

void Tr::InstallImGuiHooks()
{
    // ImGui::Selectable, ImGui::RadioButton and ImGui::Combo are overloaded, so the
    // wanted overload has to be selected explicitly.
    o_TextUnformatted = ImGui::TextUnformatted;
    o_SeparatorText = ImGui::SeparatorText;
    o_Checkbox = ImGui::Checkbox;
    o_Button = ImGui::Button;
    o_Selectable = static_cast<Selectable_t>(ImGui::Selectable);
    o_RadioButton = static_cast<RadioButton_t>(ImGui::RadioButton);
    o_Combo = static_cast<Combo_t>(ImGui::Combo);

    int installed = 0;
    installed += AttachOne(o_TextUnformatted, hkTextUnformatted, "TextUnformatted") ? 1 : 0;
    installed += AttachOne(o_SeparatorText, hkSeparatorText, "SeparatorText") ? 1 : 0;
    installed += AttachOne(o_Checkbox, hkCheckbox, "Checkbox") ? 1 : 0;
    installed += AttachOne(o_Button, hkButton, "Button") ? 1 : 0;
    installed += AttachOne(o_Selectable, hkSelectable, "Selectable") ? 1 : 0;
    installed += AttachOne(o_RadioButton, hkRadioButton, "RadioButton") ? 1 : 0;
    installed += AttachOne(o_Combo, hkCombo, "Combo") ? 1 : 0;

    LOG_INFO("i18n: {} of 7 ImGui label hooks installed", installed);
}
