#!/usr/bin/env python3
"""Check statically discoverable menu labels against the language pack.

This is deliberately not a C++ parser or a claim of complete runtime coverage.
It checks literal arguments to text/widget helpers, sidebar/card tables,
MenuOption vectors and QuirksTabLabel's choices. Arbitrary dynamic text needs review.
Technical labels that intentionally remain English are documented in the allowlist.
"""
import ast
import json
import pathlib
import re

from validate_translations import specs, split_record

ROOT = pathlib.Path(__file__).resolve().parents[2]
MENU = ROOT / "OptiScaler/menu/menu_common.cpp"
PACK = ROOT / "lang/zh-CN.txt"
ALLOWLIST = pathlib.Path(__file__).with_name("coverage_allowlist.json")
TOKEN = re.compile(
    r'//[^\n]*|/\*.*?\*/|(?:u8)?"(?:\\.|[^"\\])*"|'
    r"'(?:\\.|[^'\\])*'|[A-Za-z_]\w*|::|[^\s]", re.DOTALL
)
STRING = re.compile(r'(?:u8)?"(?:\\.|[^"\\])*"\Z', re.DOTALL)
# Value = (argument index, whether ImGui's hidden ID suffix is meaningful).
CALLS = {
    **{f"ImGui::{name}": (0, True) for name in (
        "Button", "SmallButton", "Checkbox", "RadioButton", "Selectable",
        "Combo", "BeginCombo", "TreeNode", "TreeNodeEx", "CollapsingHeader",
        "SliderInt", "SliderFloat", "SliderScalar", "InputInt", "InputFloat",
        "InputScalar", "ColorEdit3", "ColorEdit4", "TableSetupColumn",
        "SeparatorText", "TextLinkOpenURL", "Begin",
    )},
    **{f"ImGui::{name}": (0, False) for name in (
        "Text", "TextDisabled", "TextWrapped", "TextUnformatted",
        "SetTooltip", "SetItemTooltip",
    )},
    "ImGui::TextColored": (1, False),
    **{name: (0, True) for name in (
        "SectionTitle", "ConfigCheckbox", "ScopedCollapsingHeader", "StatusFlag",
    )},
    "ShowTooltip": (0, False),
    "SeparatorWithHelpMarker": (0, True),
    "PopulateCombo": (0, True),
    "Keybind": (0, True),
    "Tr::Translate": (0, False),
    "Tr::TranslateLabel": (0, True),
    "Tr::TranslateVisible": (0, True),
}


def tokenize(code):
    return [(m.group(), m.start()) for m in TOKEN.finditer(code)
            if not m.group().startswith(("//", "/*"))]


def literal(tokens):
    """Decode adjacent ordinary C++ string literals, without stripping spaces."""
    if not tokens or not all(STRING.fullmatch(t) for t in tokens):
        return None
    return "".join(ast.literal_eval(t[2:] if t.startswith("u8") else t) for t in tokens)


def arguments(tokens, start):
    """Split call arguments, respecting nested parentheses, brackets and braces."""
    args, current, stack = [], [], []
    pairs = {"(": ")", "[": "]", "{": "}"}
    for token, _ in tokens[start:]:
        if token == ")" and not stack:
            return args + [current]
        if token == "," and not stack:
            args.append(current)
            current = []
            continue
        current.append(token)
        if token in pairs:
            stack.append(pairs[token])
        elif stack and token == stack[-1]:
            stack.pop()
    return []


def extract(code):
    tokens = tokenize(code)
    found = {}

    def add(text, offset, label=False):
        if text is None:
            return
        if label:
            text = text.split("##", 1)[0]
        # Skip empty/hidden labels, numeric formats and strings containing only
        # printf conversions. Do not treat their English-looking conversion letters as prose.
        prose = text
        try:
            conversions = specs(text)
        except ValueError:
            conversions = []
        for conversion in conversions:
            prose = prose.replace(conversion, "", 1)
        if not re.search(r"[A-Za-z]", prose):
            return
        found.setdefault(text, code.count("\n", 0, offset) + 1)

    for index, (name, offset) in enumerate(tokens):
        call, opening = name, index + 1
        if index + 2 < len(tokens) and tokens[index + 1][0] == "::":
            call += "::" + tokens[index + 2][0]
            opening = index + 3
        if call not in CALLS or opening >= len(tokens) or tokens[opening][0] != "(":
            continue
        args = arguments(tokens, opening + 1)
        position, label = CALLS[call]
        if position < len(args):
            add(literal(args[position]), offset, label)
        if call == "SeparatorWithHelpMarker" and len(args) > 1:
            add(literal(args[1]), offset)

    # Static sidebar/card tables: group IDs are internal; labels are visible.
    for index, (name, _) in enumerate(tokens):
        if name not in ("Tab", "MenuBox") or index + 6 >= len(tokens):
            continue
        if [t for t, _ in tokens[index + 2:index + 6]] != ["[", "]", "=", "{"]:
            continue
        depth = 1
        fields = []
        offset = tokens[index][1]
        for token, pos in tokens[index + 6:]:
            if token == "{":
                depth += 1
                if depth == 2:
                    fields, offset = [], pos
            elif token == "}":
                if depth == 2:
                    # First item is an internal ID/group, next items are labels.
                    for field in fields[1:3 if name == "MenuBox" else 2]:
                        add(field, offset, True)
                depth -= 1
                if depth == 0:
                    break
            elif depth == 2 and STRING.fullmatch(token):
                fields.append(literal([token]))

    # MenuOption vectors carry labels and descriptions as data rather than
    # direct widget arguments. Include their initializers and later assignments.
    option_vectors = set(re.findall(
        r"\bvector\s*<\s*MenuOption\s*<[^>]+>\s*>\s+(\w+)", code))
    for index, (name, offset) in enumerate(tokens):
        if name in option_vectors and [t for t, _ in tokens[index + 1:index + 3]] == ["=", "{"]:
            depth, row = 1, []
            row_offset = offset
            for token, pos in tokens[index + 3:]:
                if token == "{" and depth == 1:
                    row, row_offset = [], pos
                    depth = 2
                    continue
                if token == "}" and depth == 2:
                    fields = arguments(row + [(")", pos)], 0)
                    for field_index, field in enumerate(fields[1:3], 1):
                        add(literal(field), row_offset, field_index == 1)
                    depth = 1
                    continue
                if depth >= 2:
                    row.append((token, pos))
                if token == "{":
                    depth += 1
                elif token == "}":
                    depth -= 1
                    if depth == 0:
                        break
        if name == "set_disabled" and index + 1 < len(tokens) and tokens[index + 1][0] == "(":
            args = arguments(tokens, index + 2)
            if len(args) > 1:
                add(literal(args[1]), offset)
        if name == "tooltip" and index > 0 and tokens[index - 1][0] == ".":
            if index + 1 < len(tokens) and tokens[index + 1][0] == "=":
                expression = []
                for token, _ in tokens[index + 2:]:
                    if token == ";":
                        break
                    expression.append(token)
                add(literal(expression), offset)

    # Runtime-selected sidebar labels live in this small helper.
    match = re.search(r"\bQuirksTabLabel\s*\([^)]*\)\s*\{([^}]+)\}", code)
    if match:
        for token, offset in tokenize(match.group(1)):
            if STRING.fullmatch(token):
                add(literal([token]), match.start(1) + offset, True)
    return found


def check(menu=MENU, pack=PACK, allowlist=ALLOWLIST):
    translations = dict(split_record(line.strip()) for line in pack.read_text(encoding="utf-8-sig").splitlines()
                        if line.strip() and not line.strip().startswith(("#", ";")))
    allowed = json.loads(allowlist.read_text(encoding="utf-8"))
    if not isinstance(allowed, dict) or any(not isinstance(v, str) or not v.strip() for v in allowed.values()):
        raise ValueError("Every coverage exception must have an explanation")
    entries = extract(menu.read_text(encoding="utf-8-sig"))
    missing = entries.keys() - translations.keys() - allowed.keys()
    for text in sorted(missing):
        print(f"{menu}:{entries[text]}: untranslated {text!r}")
    if missing:
        raise SystemExit(1)
    print(f"Menu coverage OK: {len(entries)} static strings checked, "
          f"{len(entries.keys() & allowed.keys())} documented exceptions")


if __name__ == "__main__":
    check()
