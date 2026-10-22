import re
import json

with open("merged_menu_common.cpp", "r", encoding="utf-8") as f:
    code = f.read()

entries = []
seen = set()

def add_entry(source, category, context=""):
    if not source:
        return
    # In C++ string literals, things like \n, \t, \" are escaped
    # But let's check what our Tr::LoadTable expects:
    # Tr::LoadTable reads line by line: source = Unescape(Trim(line.substr(0, separator)))
    # and Unescape turns r"\n" into '\n', r"\t" into '\t', r"\\" into '\'.
    # In C++ source code, a string literal written as "foo\nbar" has the characters 'f','o','o','\','n','b','a','r'.
    # When compiled, C++ puts the byte '\n' (0x0A) in memory.
    # When our runtime hook runs:
    # Tr::Translate(text) looks up text in g_table.
    # In g_table: key is std::string.
    # When LoadTable reads line:
    # `foo\nbar=...`
    # LoadTable does Unescape("foo\\nbar") -> "foo\nbar" (with byte 0x0A).
    # So the key in g_table matches the C++ in-memory string with 0x0A!
    # Therefore, in our translation file `zh-CN.txt`, we write `\n` literally as the two characters '\' and 'n'!
    # In Python, if we have raw string from source code `"foo\nbar"`, its characters are already `\n`.
    
    # Strip any surrounding whitespace from the key
    s = source.strip()
    if not s:
        return
    # Strip ## suffix if present and not starting with ##
    if "##" in s and not s.startswith("##"):
        s = s.split("##")[0].strip()
    if not s:
        return
        
    # Filter out pure numbers, pure punctuation, format strings without text
    if re.match(r'^[0-9.]+$', s) and len(s) <= 4:
        return
    if s in ["%s", "%d", "%u", "%X", "%08X", "%.2f", "%.1f", "%.3f", "%.0f", "%s%s", "|", "-", "/", "", "#", "##", "###"]:
        return
    if s.startswith("##") and len(s) <= 8:
        return
    if s in seen:
        return
    seen.add(s)
    entries.append({
        "source": s,
        "category": category,
        "context": context
    })

# 1. ScopedCollapsingHeader / ImGui::CollapsingHeader / TreeNode
for m in re.finditer(r'(?:ScopedCollapsingHeader|ImGui::CollapsingHeader|ImGui::TreeNode)\s*\(\s*"((?:[^"\\]|\\.)*)"', code):
    add_entry(m.group(1), "Header/TreeNode", m.group(0))

# 2. SectionTitle / SeparatorWithHelpMarker
for m in re.finditer(r'SectionTitle\s*\(\s*"((?:[^"\\]|\\.)*)"', code):
    add_entry(m.group(1), "SectionTitle", m.group(0))

for m in re.finditer(r'SeparatorWithHelpMarker\s*\(\s*"((?:[^"\\]|\\.)*)"\s*,\s*"((?:[^"\\]|\\.)*)"', code):
    add_entry(m.group(1), "SectionTitle", m.group(0))
    add_entry(m.group(2), "Tooltip", m.group(0))

# 3. ConfigCheckbox / ImGui::Checkbox
for m in re.finditer(r'ConfigCheckbox\s*\(\s*"((?:[^"\\]|\\.)*)"(?:\s*,\s*[^,)]+)*(?:\s*,\s*"((?:[^"\\]|\\.)*)")?', code):
    add_entry(m.group(1), "Checkbox", "ConfigCheckbox")
    if m.group(2):
        add_entry(m.group(2), "Tooltip", "ConfigCheckbox tip")

for m in re.finditer(r'ImGui::Checkbox\s*\(\s*"((?:[^"\\]|\\.)*)"', code):
    add_entry(m.group(1), "Checkbox", "ImGui::Checkbox")

# 4. Buttons, Selectables, RadioButtons, Links
for m in re.finditer(r'ImGui::Button\s*\(\s*"((?:[^"\\]|\\.)*)"', code):
    add_entry(m.group(1), "Button", "ImGui::Button")

for m in re.finditer(r'ImGui::Selectable\s*\(\s*"((?:[^"\\]|\\.)*)"', code):
    add_entry(m.group(1), "Selectable", "ImGui::Selectable")

for m in re.finditer(r'ImGui::RadioButton\s*\(\s*"((?:[^"\\]|\\.)*)"', code):
    add_entry(m.group(1), "RadioButton", "ImGui::RadioButton")

for m in re.finditer(r'ImGui::TextLinkOpenURL\s*\(\s*"((?:[^"\\]|\\.)*)"', code):
    add_entry(m.group(1), "Link", "ImGui::TextLinkOpenURL")

# 5. Sliders and Inputs
for m in re.finditer(r'ImGui::Slider(?:Float|Int|Scalar)\s*\(\s*"((?:[^"\\]|\\.)*)"', code):
    add_entry(m.group(1), "Slider", "Slider")

for m in re.finditer(r'ImGui::Input(?:Float|Int|Scalar)\s*\(\s*"((?:[^"\\]|\\.)*)"', code):
    add_entry(m.group(1), "Input", "Input")

# 6. Combo & BeginCombo
for m in re.finditer(r'ImGui::(?:Combo|BeginCombo)\s*\(\s*"((?:[^"\\]|\\.)*)"', code):
    add_entry(m.group(1), "Combo", "Combo")

# 7. Tooltips: ShowTooltip, SetTooltip, SetItemTooltip
for m in re.finditer(r'(?:ShowTooltip|ImGui::SetTooltip|ImGui::SetItemTooltip)\s*\(\s*"((?:[^"\\]|\\.)*)"', code):
    add_entry(m.group(1), "Tooltip", "Tooltip")

# 8. Table columns
for m in re.finditer(r'ImGui::TableSetupColumn\s*\(\s*"((?:[^"\\]|\\.)*)"', code):
    add_entry(m.group(1), "TableColumn", "Table Column")

# 9. Tabs and boxes tables
for m in re.finditer(r'\{\s*"((?:[^"\\]|\\.)*)"\s*,\s*"((?:[^"\\]|\\.)*)"\s*,\s*"((?:[^"\\]|\\.)*)"', code):
    g, l, d = m.group(1), m.group(2), m.group(3)
    # Check if looks like tab table
    if g in ["MAIN", "SYSTEM", "ADVANCED"]:
        add_entry(g, "SidebarGroup")
        add_entry(l, "SidebarTab")
        add_entry(d, "TabDescription")

for m in re.finditer(r'\{\s*"[a-z0-9_]+"\s*,\s*"((?:[^"\\]|\\.)*)"\s*,\s*"((?:[^"\\]|\\.)*)"', code):
    add_entry(m.group(1), "BoxTab")
    add_entry(m.group(2), "BoxName")

# 10. Arrays
arrays = re.findall(r'(?:const\s+char\s*\*\s*(?:const\s*)?|static\s+const\s+char\s*\*\s*)(\w+)\[\]\s*=\s*\{([^}]+)\};', code)
for name, body in arrays:
    items = re.findall(r'"((?:[^"\\]|\\.)*)"', body)
    for it in items:
        add_entry(it, f"Array {name}")

# 11. MenuOption structs
for m in re.finditer(r'\{\s*(?:[A-Za-z0-9_:]+)?\s*,\s*"((?:[^"\\]|\\.)*)"(?:\s*,\s*"((?:[^"\\]|\\.)*)")?\s*\}', code):
    add_entry(m.group(1), "MenuOption")
    if m.group(2):
        add_entry(m.group(2), "MenuOptionDescription")

# 12. ImGui::Text / TextDisabled / TextColored / TextWrapped
for m in re.finditer(r'ImGui::Text(?:Disabled|Colored|Wrapped)?\s*\(\s*(?:[^,()]*,\s*)?"((?:[^"\\]|\\.)*)"', code):
    add_entry(m.group(1), "Text")

print(f"Total structured entries: {len(entries)}")
with open("entries_parsed.json", "w", encoding="utf-8") as f:
    json.dump(entries, f, ensure_ascii=False, indent=2)
