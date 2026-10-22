# -*- coding: utf-8 -*-
import json
import re

from tr_data_1 import TR_PART1
from tr_data_2 import TR_PART2
from tr_data_3 import TR_PART3
from tr_data_4 import TR_PART4

with open("sources_to_translate.json", "r", encoding="utf-8") as f:
    all_sources = json.load(f)

print(f"Total target sources: {len(all_sources)}")

merged = {}
merged.update(TR_PART1)
merged.update(TR_PART2)
merged.update(TR_PART3)
merged.update(TR_PART4)

print(f"Merged translations count: {len(merged)}")

missing = [s for s in all_sources if s not in merged]
if missing:
    print(f"ERROR: {len(missing)} missing sources!")
    for m in missing[:10]:
        print(" ", repr(m))
    exit(1)

print("All 741 sources are 100% covered!")

# Check format specifiers
def count_fmt(text):
    cnt = 0
    i = 0
    n = len(text)
    while i < n:
        if text[i] == '%':
            if i + 1 < n and text[i + 1] == '%':
                i += 2
                continue
            cnt += 1
        i += 1
    return cnt

fmt_mismatches = []
for src, (zh, reason) in merged.items():
    if count_fmt(src) != count_fmt(zh):
        fmt_mismatches.append((src, zh, count_fmt(src), count_fmt(zh)))

if fmt_mismatches:
    print(f"ERROR: {len(fmt_mismatches)} format specifier mismatches!")
    for src, zh, c1, c2 in fmt_mismatches:
        print(f"  {repr(src)} ({c1}) != {repr(zh)} ({c2})")
    exit(1)

print("All format specifiers match perfectly!")

# Write lang/zh-CN.txt
# Note: we group the output in lang/zh-CN.txt by modules for clarity and readability
with open("sources_by_mod.json", "r", encoding="utf-8") as f:
    by_mod = json.load(f)

mod_titles = {
    "1_Nav": "模块 1：导航栏、主标签页与侧边栏 (Navigation, Tabs & Sidebar)",
    "2_Upscaler": "模块 2：超分辨率技术 (Upscalers - DLSS / FSR / XeSS)",
    "3_FrameGen": "模块 3：帧生成技术 (Frame Generation - DLSSG / FSR-FG / XeFG / OptiFG)",
    "4_Latency": "模块 4：低延迟与帧率管理 (Low Latency, Reflex, Anti-Lag, FPS Limiter)",
    "5_Texture": "模块 5：图像锐化、纹理与画质过滤 (Sharpening, Mipmap Bias, Anisotropy, Magnifier)",
    "6_Compatibility": "模块 6：兼容性、伪装与底层挂钩 (Compatibility, Spoofing, Hooks, Plugins)",
    "7_Barriers_Quirks": "模块 7：DirectX 12 资源屏障与游戏专属修复 (Resource Barriers & Quirks)",
    "8_Menu_Overlay": "模块 8：菜单界面、主题、快捷键与性能监控 (Menu UI, Theme, Keybinds, FPS Overlay)",
    "9_Common": "模块 9：通用按钮、状态与交互控件 (Common Buttons, States & Dialogs)",
}

with open("lang/zh-CN.txt", "w", encoding="utf-8") as out:
    out.write("# ============================================================================\n")
    out.write("# OptiScaler 完整简体中文本地化语言包 (Simplified Chinese Translation)\n")
    out.write("# 编码：UTF-8\n")
    out.write("# 启用：在 OptiScaler.ini 中设置 [Menu] Language=zh-CN 或 auto\n")
    out.write("# 条目总数：741 条全量覆盖\n")
    out.write("# ============================================================================\n\n")

    for mod, items in sorted(by_mod.items()):
        title = mod_titles.get(mod, mod)
        out.write(f"\n# ----------------------------------------------------------------------------\n")
        out.write(f"# {title}\n")
        out.write(f"# ----------------------------------------------------------------------------\n\n")
        
        seen_mod = set()
        for item in sorted(items):
            if item in seen_mod:
                continue
            seen_mod.add(item)
            if item in merged:
                zh, _ = merged[item]
                # Replace actual newlines in strings if any (they are already escaped \n in keys)
                out.write(f"{item} = {zh}\n")

print("Successfully wrote lang/zh-CN.txt!")

# Save complete structured JSON with rationales for inspection or review
with open("translations_full_with_reasons.json", "w", encoding="utf-8") as out:
    dump_data = []
    for mod, items in sorted(by_mod.items()):
        seen_mod = set()
        for item in sorted(items):
            if item in seen_mod:
                continue
            seen_mod.add(item)
            zh, reason = merged[item]
            dump_data.append({
                "module": mod_titles.get(mod, mod),
                "en": item,
                "zh": zh,
                "reason": reason
            })
    json.dump(dump_data, out, ensure_ascii=False, indent=2)

print("Successfully wrote translations_full_with_reasons.json!")