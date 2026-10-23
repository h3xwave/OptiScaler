#include "pch.h"

#include "Translation.h"

#include <detours/detours.h>
#include <imgui/imgui.h>
// ImGui::FindRenderedTextEnd() lives in the internal header, not the public one.
#include <imgui/imgui_internal.h>

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
using TreeNode_t = bool (*)(const char* label);
using TableSetupColumn_t = void (*)(const char* label, ImGuiTableColumnFlags flags, float init_width_or_weight,
                                    ImGuiID user_id);
using BeginCombo_t = bool (*)(const char* label, const char* preview_value, ImGuiComboFlags flags);
using TextLinkOpenURL_t = void (*)(const char* label, const char* url);
using CollapsingHeader_t = bool (*)(const char* label, ImGuiTreeNodeFlags flags);
using SliderScalar_t = bool (*)(const char* label, ImGuiDataType data_type, void* p_data, const void* p_min,
                                const void* p_max, const char* format, ImGuiSliderFlags flags);
using InputScalar_t = bool (*)(const char* label, ImGuiDataType data_type, void* p_data, const void* p_step,
                               const void* p_step_fast, const char* format, ImGuiInputTextFlags flags);

TextUnformatted_t o_TextUnformatted = nullptr;
SeparatorText_t o_SeparatorText = nullptr;
Checkbox_t o_Checkbox = nullptr;
Button_t o_Button = nullptr;
Selectable_t o_Selectable = nullptr;
RadioButton_t o_RadioButton = nullptr;
Combo_t o_Combo = nullptr;
TreeNode_t o_TreeNode = nullptr;
TableSetupColumn_t o_TableSetupColumn = nullptr;
BeginCombo_t o_BeginCombo = nullptr;
TextLinkOpenURL_t o_TextLinkOpenURL = nullptr;
CollapsingHeader_t o_CollapsingHeader = nullptr;
SliderScalar_t o_SliderScalar = nullptr;
InputScalar_t o_InputScalar = nullptr;

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

    // The supplied end is a bounded range, not necessarily NUL-terminated.
    // Looking beyond it (or performing strlen on it) risks out-of-bounds reads.
    const auto length = static_cast<size_t>(text_end - text);
    if (const char* translated = Tr::TranslateRange(text, length))
        o_TextUnformatted(translated, nullptr);
    else
        o_TextUnformatted(text, text_end);
}

void hkSeparatorText(const char* label) { o_SeparatorText(Tr::TranslateLabel(label)); }

bool hkCheckbox(const char* label, bool* v) { return o_Checkbox(Tr::TranslateLabel(label), v); }

bool hkButton(const char* label, const ImVec2& size) { return o_Button(Tr::TranslateLabel(label), size); }

bool hkSelectable(const char* label, bool selected, ImGuiSelectableFlags flags, const ImVec2& size)
{
    return o_Selectable(Tr::TranslateLabel(label), selected, flags, size);
}

bool hkRadioButton(const char* label, bool active) { return o_RadioButton(Tr::TranslateLabel(label), active); }

bool hkCombo(const char* label, int* current_item, const char* const items[], int items_count,
             int popup_max_height_in_items)
{
    return o_Combo(Tr::TranslateLabel(label), current_item, items, items_count, popup_max_height_in_items);
}

bool hkTreeNode(const char* label) { return o_TreeNode(Tr::TranslateLabel(label)); }

void hkTableSetupColumn(const char* label, ImGuiTableColumnFlags flags, float init_width_or_weight, ImGuiID user_id)
{
    o_TableSetupColumn(Tr::TranslateLabel(label), flags, init_width_or_weight, user_id);
}

// BeginCombo draws the collapsed preview text itself, so the selected item needs
// translating here. The popup entries are Selectable() calls and are covered by
// hkSelectable instead.
bool hkBeginCombo(const char* label, const char* preview_value, ImGuiComboFlags flags)
{
    return o_BeginCombo(Tr::TranslateLabel(label), Tr::Translate(preview_value), flags);
}

void hkTextLinkOpenURL(const char* label, const char* url) { o_TextLinkOpenURL(Tr::TranslateLabel(label), url); }

bool hkCollapsingHeader(const char* label, ImGuiTreeNodeFlags flags)
{
    return o_CollapsingHeader(Tr::TranslateLabel(label), flags);
}

bool hkSliderScalar(const char* label, ImGuiDataType data_type, void* p_data, const void* p_min, const void* p_max,
                    const char* format, ImGuiSliderFlags flags)
{
    return o_SliderScalar(Tr::TranslateLabel(label), data_type, p_data, p_min, p_max, format, flags);
}

bool hkInputScalar(const char* label, ImGuiDataType data_type, void* p_data, const void* p_step,
                   const void* p_step_fast, const char* format, ImGuiInputTextFlags flags)
{
    return o_InputScalar(Tr::TranslateLabel(label), data_type, p_data, p_step, p_step_fast, format, flags);
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
} // namespace

void Tr::InstallImGuiHooks()
{
    // Overloaded functions need the wanted overload selected explicitly.
    o_TextUnformatted = ImGui::TextUnformatted;
    o_SeparatorText = ImGui::SeparatorText;
    o_Checkbox = ImGui::Checkbox;
    o_Button = ImGui::Button;
    o_Selectable = static_cast<Selectable_t>(ImGui::Selectable);
    o_RadioButton = static_cast<RadioButton_t>(ImGui::RadioButton);
    o_Combo = static_cast<Combo_t>(ImGui::Combo);
    o_TreeNode = static_cast<TreeNode_t>(ImGui::TreeNode);
    o_TableSetupColumn = ImGui::TableSetupColumn;
    o_BeginCombo = ImGui::BeginCombo;
    o_TextLinkOpenURL = ImGui::TextLinkOpenURL;
    o_CollapsingHeader = static_cast<CollapsingHeader_t>(ImGui::CollapsingHeader);
    o_SliderScalar = ImGui::SliderScalar;
    o_InputScalar = ImGui::InputScalar;

    constexpr int hookCount = 14;
    int installed = 0;
    installed += AttachOne(o_TextUnformatted, hkTextUnformatted, "TextUnformatted") ? 1 : 0;
    installed += AttachOne(o_SeparatorText, hkSeparatorText, "SeparatorText") ? 1 : 0;
    installed += AttachOne(o_Checkbox, hkCheckbox, "Checkbox") ? 1 : 0;
    installed += AttachOne(o_Button, hkButton, "Button") ? 1 : 0;
    installed += AttachOne(o_Selectable, hkSelectable, "Selectable") ? 1 : 0;
    installed += AttachOne(o_RadioButton, hkRadioButton, "RadioButton") ? 1 : 0;
    installed += AttachOne(o_Combo, hkCombo, "Combo") ? 1 : 0;
    installed += AttachOne(o_TreeNode, hkTreeNode, "TreeNode") ? 1 : 0;
    installed += AttachOne(o_TableSetupColumn, hkTableSetupColumn, "TableSetupColumn") ? 1 : 0;
    installed += AttachOne(o_BeginCombo, hkBeginCombo, "BeginCombo") ? 1 : 0;
    installed += AttachOne(o_TextLinkOpenURL, hkTextLinkOpenURL, "TextLinkOpenURL") ? 1 : 0;
    installed += AttachOne(o_CollapsingHeader, hkCollapsingHeader, "CollapsingHeader") ? 1 : 0;
    installed += AttachOne(o_SliderScalar, hkSliderScalar, "SliderScalar") ? 1 : 0;
    installed += AttachOne(o_InputScalar, hkInputScalar, "InputScalar") ? 1 : 0;

    LOG_INFO("i18n: {} of {} ImGui label hooks installed", installed, hookCount);
}
