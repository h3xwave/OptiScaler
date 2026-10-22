import re
import json

with open("OptiScaler/menu/menu_common.cpp", "r", encoding="utf-8") as f:
    code = f.read()

# Step 1: Strip C and C++ comments (except inside strings)
n = len(code)
i = 0
cleaned = []
while i < n:
    if code[i] == '"':
        start = i
        i += 1
        while i < n and code[i] != '"':
            if code[i] == '\\':
                i += 2
            else:
                i += 1
        if i < n:
            i += 1
        cleaned.append(code[start:i])
    elif code[i:i+2] == '//':
        while i < n and code[i] != '\n':
            i += 1
    elif code[i:i+2] == '/*':
        i += 2
        while i < n and code[i:i+2] != '*/':
            i += 1
        if i < n:
            i += 2
    else:
        cleaned.append(code[i])
        i += 1

clean_code = "".join(cleaned)

# Step 2: Merge adjacent string literals: "foo" \s* "bar" -> "foobar"
def merge_adjacent_strings(text):
    # Lex tokens: string vs other
    tokens = []
    i = 0
    n = len(text)
    while i < n:
        if text[i] == '"':
            start = i
            i += 1
            while i < n and text[i] != '"':
                if text[i] == '\\':
                    i += 2
                else:
                    i += 1
            if i < n:
                i += 1
            # content inside quotes
            tokens.append(('STR', text[start+1:i-1]))
        elif text[i].isspace():
            start = i
            while i < n and text[i].isspace():
                i += 1
            tokens.append(('SPACE', text[start:i]))
        else:
            start = i
            while i < n and text[i] != '"' and not text[i].isspace():
                i += 1
            tokens.append(('OTHER', text[start:i]))
    
    # Merge consecutive STR separated only by SPACE
    merged_tokens = []
    for tok, val in tokens:
        if tok == 'STR':
            # Check if previous was STR or (SPACE preceded by STR)
            if merged_tokens and merged_tokens[-1][0] == 'SPACE' and len(merged_tokens) >= 2 and merged_tokens[-2][0] == 'STR':
                merged_tokens.pop() # remove space
                prev_str = merged_tokens.pop()[1]
                merged_tokens.append(('STR', prev_str + val))
            elif merged_tokens and merged_tokens[-1][0] == 'STR':
                prev_str = merged_tokens.pop()[1]
                merged_tokens.append(('STR', prev_str + val))
            else:
                merged_tokens.append(('STR', val))
        else:
            merged_tokens.append((tok, val))
            
    # Reassemble code
    res = []
    for tok, val in merged_tokens:
        if tok == 'STR':
            res.append('"' + val + '"')
        else:
            res.append(val)
    return "".join(res)

merged_code = merge_adjacent_strings(clean_code)
print(f"Clean len: {len(clean_code)}, merged len: {len(merged_code)}")

with open("merged_menu_common.cpp", "w", encoding="utf-8") as f:
    f.write(merged_code)
