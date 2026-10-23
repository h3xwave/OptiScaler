#pragma once

#include <string>

// Runtime translation layer for the OptiScaler menu.
//
// Every menu string is a hardcoded English literal inside menu_common.cpp. Rewriting
// those literals would conflict with every upstream sync, so this layer translates
// them while they are being drawn instead:
//
//   * ImGui::TextV() is patched directly in imgui_widgets.cpp. That covers Text(),
//     TextColored(), TextDisabled(), TextWrapped() and BulletText() - in other words
//     every tooltip and description. Patching the function body is immune to the
//     link time inlining that /GL + /LTCG performs, so it cannot silently stop
//     working.
//   * The label taking widgets (Checkbox, Button, Selectable, RadioButton, Combo,
//     SeparatorText, TextUnformatted, TreeNode, TableSetupColumn, BeginCombo,
//     TextLinkOpenURL, CollapsingHeader, SliderScalar, InputScalar) are
//     intercepted with Detours hooks installed from ImGuiTrHooks.cpp. A missed
//     hook only leaves that label in English.
//
// Translation files live in a "lang" folder next to OptiScaler.dll and are named
// after a language code, e.g. lang/zh-CN.txt. See lang/zh-CN.txt for the format.
//
// Everything degrades to the original English when no language file is present, so
// the layer is inert unless it is explicitly enabled.
namespace Tr
{
// Loads the language table and installs the ImGui hooks. Idempotent: only the
// first call does any work. Must be called before the menu font atlas is built
// so that FallbackFontPath() is available to the font setup code.
void Initialize();

// Returns the translation of 'text', or 'text' itself when there is no entry.
// Never returns nullptr for a non-null input.
const char* Translate(const char* text);

// Translates a bounded string, or returns nullptr when no entry matches.
const char* TranslateRange(const char* text, size_t length);

// UI-only text without ImGui ID suffixes.
const char* TranslateVisible(const char* text);

// Like Translate() but keeps a trailing "##id" suffix intact so that ImGui
// widget IDs stay stable when the visible label is translated.
const char* TranslateLabel(const char* label);

// True when a language file was loaded and contains at least one entry.
bool IsActive();

// Language code that was loaded, e.g. "zh-CN". Empty when inactive.
const std::string& Language();

// Path of a CJK capable system font that should be used for the menu when the
// user did not configure TTFFontPath. Empty when no such font was found.
const std::wstring& FallbackFontPath();

// Internal: called by Initialize(); exposed so that ImGuiTrHooks.cpp can define it.
void InstallImGuiHooks();
} // namespace Tr
