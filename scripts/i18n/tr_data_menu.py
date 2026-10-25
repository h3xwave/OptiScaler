# -*- coding: utf-8 -*-
"""Additional menu strings found by the static coverage audit after upstream sync."""

TR_MENU = {
    # Upstream FPS overlay appearance/layout settings (08e13adf).
    "A file in C:\\Windows\\Fonts or a full path, Enter applies it": (
        "填写 C:\\Windows\\Fonts 中的文件名或完整路径，按回车应用", "Custom overlay font tooltip"),
    "Appearance": ("外观", "Overlay appearance section"),
    "Applies a copied code. Settings it doesn't list go back to their defaults.": (
        "应用复制的设置代码，代码中未列出的设置将恢复默认值。", "Import overlay settings tooltip"),
    "Before the overlay's scale, the far left is the menu's font size": (
        "此字号在叠加层缩放之前生效，滑块最左端表示使用菜单字号", "Overlay font size tooltip"),
    "Choose a Windows system font or enter any custom .ttf/.otf file below": (
        "选择 Windows 系统字体，或在下方输入自定义 .ttf/.otf 字体文件", "Overlay font selector tooltip"),
    "Colors": ("颜色", "Overlay color section"),
    "Copies your overlay settings as a code to keep or share": (
        "将叠加层设置复制为代码，便于保存或分享", "Export overlay settings tooltip"),
    "Copy Code": ("复制代码", "Export overlay settings button"),
    "Corner Rounding": ("圆角大小", "Menu and overlay corner radius"),
    "Custom's rows back to the ones of Full + Graph": (
        "将自定义模式的显示行恢复为“完整 + 图表”的默认行", "Reset overlay rows tooltip"),
    "Extra horizontal tracking in pixels between characters": (
        "字符之间额外的水平间距，单位为像素", "Letter spacing tooltip"),
    "FPS Row": ("帧率行", "Overlay FPS row selector"),
    "Font": ("字体", "Overlay font selector"),
    "Font Size": ("字号", "Overlay font size"),
    "Graph Height": ("图表高度", "Overlay graph height"),
    "Horizontal Position": ("水平位置", "Custom overlay position"),
    "How often FPS and times change, averaged in between. Higher is easier to read.": (
        "帧率与耗时的更新间隔，期间的数据会取平均值。间隔越大越便于阅读。", "Overlay update interval tooltip"),
    "Just the number, or with the API, frame time or average FPS, frame generation and upscaler": (
        "仅显示帧率数值，或同时显示图形 API、帧时间或平均帧率、帧生成和升频算法", "Overlay FPS row tooltip"),
    "Layout": ("布局", "Overlay layout section"),
    "Letter Spacing": ("字间距", "Overlay text spacing"),
    "Menu font": ("菜单字体", "Overlay font fallback"),
    "Names like FPS: and Avg:": ("FPS:、Avg: 等标签的大小", "Overlay label scale tooltip"),
    "Order": ("顺序", "Overlay row order column"),
    "Paste Code": ("粘贴代码", "Import overlay settings button"),
    "Presets": ("预设", "Overlay appearance presets"),
    "Presets of the rows, Custom shows the ones chosen in Rows.\nThe Overlay Cycle key switches between them.": (
        "选择显示行的预设；自定义模式显示在“显示行”中选择的内容。\n可使用叠加层模式切换键切换预设。", "Overlay type tooltip"),
    "Reset Appearance": ("重置外观", "Reset overlay appearance button"),
    "Row": ("显示行", "Overlay row column"),
    "Row Spacing": ("行间距", "Overlay row spacing"),
    "Rows": ("显示行", "Overlay rows section"),
    "Shadow Strength": ("阴影强度", "Overlay shadow strength"),
    "Share Settings": ("分享设置", "Overlay settings exchange section"),
    "Size of the FPS overlay, independent from the menu scale unless set to Same as menu": (
        "帧率叠加层的大小；除非设为与菜单相同，否则独立于菜单缩放", "Overlay scale tooltip"),
    "Text": ("文字", "Overlay text section"),
    "Text Shadow": ("文字阴影", "Overlay shadow selector"),
    "The menu theme's colors for the labels, values, graph and background": (
        "标签、数值、图表和背景使用菜单主题的颜色", "Overlay theme tooltip"),
    "The numbers": ("数值的大小", "Overlay value scale tooltip"),
    "Thickness and darkness of the shadow, thickness of the outline": (
        "调整阴影的厚度与深浅，或描边的粗细", "Overlay shadow strength tooltip"),
    "Update Interval": ("更新间隔", "Overlay update interval"),
    "Use Theme": ("使用主题", "Overlay theme colors"),
    "Vertical Position": ("垂直位置", "Custom overlay position"),
    # Additional labels passed through arrays and local UI helpers.
    "With Frame Time": ("附带帧时间", "Overlay FPS row choice"),
    "With Average FPS": ("附带平均帧率", "Overlay FPS row choice"),
    "Upscale Ratio in Presets": ("在预设中显示升频比例", "Overlay row option"),
    "The Upscale Ratio row in the presets from Simple on, Custom has it in its rows": (
        "在简洁及更详细的预设中显示升频比例行；自定义模式可在显示行中选择", "Overlay ratio row tooltip"),
    "Reset Rows & Spacing": ("重置显示行和间距", "Reset custom overlay rows"),
    "Reset Spacing": ("重置间距", "Reset overlay row spacing"),
    "Classic": ("经典", "Overlay appearance preset"),
    "Afterburner-Like": ("Afterburner 风格", "Overlay appearance preset"),
    "Glass Strip": ("玻璃条", "Overlay appearance preset"),
    "OptiScaler's overlay: every row with the graphs, grey labels with a shadow": (
        "OptiScaler 叠加层：显示所有行与图表，使用带阴影的灰色标签", "Default overlay preset tooltip"),
    "OptiScaler's earlier overlay: just the FPS in white, no shadow": (
        "OptiScaler 早期叠加层：仅显示白色帧率，无阴影", "Classic overlay preset tooltip"),
    "As MSI Afterburner: Unispace Bold, orange labels, outlined, no background": (
        "类似 MSI Afterburner：Unispace 粗体、橙色标签、描边，无背景", "Afterburner overlay preset tooltip"),
    "A strip at the top center: Bahnschrift, cyan values on a dark glass panel": (
        "顶部居中的条形面板：Bahnschrift 字体，深色玻璃背景与青色数值", "Glass overlay preset tooltip"),
    "Compact Labels": ("精简标签", "Overlay compact labels option"),
    "Shorter labels for a narrower overlay: UPS, FT, UT": (
        "使用 UPS、FT、UT 等简短标签，缩窄叠加层", "Overlay compact labels tooltip"),
    "Custom Font File": ("自定义字体文件", "Overlay font file input"),
    "Label Size": ("标签大小", "Overlay label scale"),
    "Value Size": ("数值大小", "Overlay value scale"),
    "Shadow": ("阴影", "Overlay shadow type/color"),
    "Outline": ("描边", "Overlay shadow type"),
    "Labels": ("标签", "Overlay label color"),
    "Values": ("数值", "Overlay value color"),
    "Graph": ("图表", "Overlay graph color"),
    "Background": ("背景", "Overlay background color"),
    # Runtime labels and descriptions passed through MenuOption/Keybind helpers.
    "FG Input": ("帧生成输入", "Frame generation source selector"),
    "FG Output": ("帧生成输出", "Frame generation backend selector"),
    "FG Nvngx": ("Nvngx 帧生成", "Nvngx replacement selector"),
    "FG Nvngx Replacement": ("Nvngx 帧生成替代方案", "Nvngx replacement selector"),
    "FPS Overlay Cycle": ("切换性能叠加层模式", "Keybind button"),
    "Downscaler": ("降采样算法", "Downscaler selector"),
    "Edge fill mode": ("边缘填充模式", "Reprojection selector"),
    "Force State": ("强制状态", "Low latency selector"),
    "LatencyFlex mode": ("LatencyFlex 模式", "Low latency selector"),
    "Output": ("输出", "Low latency selector"),
    "Unsupported API": ("不支持此图形 API", "Disabled option reason"),
    "Unsupported hardware": ("硬件不支持", "Disabled option reason"),
    "Unsupported hardware and no replacements": (
        "硬件不支持，且没有可用的替代方案", "Disabled FG output reason"),
    "amd_fidelityfx_dx12.dll is missing": (
        "缺少 amd_fidelityfx_dx12.dll", "Disabled FG input reason"),
    "libxess_fg.dll is missing": ("缺少 libxess_fg.dll", "Disabled FG input reason"),
    "Missing amd_fidelityfx_framegeneration_dx12.dll": (
        "缺少 amd_fidelityfx_framegeneration_dx12.dll", "Disabled replacement reason"),
    "Missing amd_fidelityfx_framegeneration_dx12.dll\nor missing dlss-enabler-headless.dll": (
        "缺少 amd_fidelityfx_framegeneration_dx12.dll\n或 dlss-enabler-headless.dll", "Disabled replacement reason"),
    "Missing dlss-enabler-headless.dll": (
        "缺少 dlss-enabler-headless.dll", "Disabled replacement reason"),
    "Missing dlssg_to_fsr3_amd_is_better.dll": (
        "缺少 dlssg_to_fsr3_amd_is_better.dll", "Disabled replacement reason"),
    "No real DLSSG, unsupported hardware\nOnly Nvngx FG replacements available": (
        "硬件不支持原生 DLSSG\n只能使用 Nvngx 帧生成替代方案", "FG output description"),
    "After changing this option, please Save Settings.\nIt will be applied on next launch.": (
        "修改此选项后，请保存设置。\n更改将在下次启动时生效。", "Appended restart notice"),
    "The best input the game sends: Reflex, XeLL when enabled in the game, AntiLag 2, UE, XeLL.\n"
    "AntiLag 2 first while the game's FSR-FG reports its frames through it.\n"
    "Without any, OptiScaler's own with the DLSSG output.": (
        "按优先级选择游戏提供的输入：Reflex、游戏中已开启的 XeLL、AntiLag 2、UE、XeLL。\n"
        "当游戏通过 AntiLag 2 上报 FSR 帧生成信息时，优先使用 AntiLag 2。\n"
        "若均不可用，则在使用 DLSSG 输出时采用 OptiScaler 自身的输入。", "Automatic low latency input"),
    "Reset Custom Tab": ("重置自定义选项卡", "Custom tab reset button"),
    "Compatibility list, known issues and FG options explained": (
        "兼容性列表、已知问题及帧生成选项说明", "Wiki tooltip"),
    "Latency": ("延迟", "Sidebar and card category"),
    "Quirks and ASI": ("兼容补丁与 ASI 插件", "Dynamic sidebar label"),
    "(Potential FSR3 fallback)": ("（可能回退到 FSR3）", "Upscaler status"),
    "3rd person detected (%.2f, orbit %.2f)": (
        "检测到第三人称视角（%.2f，环绕 %.2f）", "Camera detection status"),
    "ACTIVATE FG": ("启用帧生成", "Frame generation button"),
    "Borderless display mode required!": ("需要使用无边框显示模式！", "Frame generation warning"),
    "Customise this tab": ("自定义此选项卡", "Custom tab action"),
    "DLSS Enabler as dlss-enabler-headless.dll": (
        "以 dlss-enabler-headless.dll 形式使用 DLSS Enabler", "Replacement library hint"),
    "DLSS capable GPU": ("显卡支持 DLSS", "Detected capabilities"),
    "DLSSG only supports HDR10": ("DLSSG 仅支持 HDR10", "HDR compatibility warning"),
    "FSR hooks": ("FSR 钩子", "Detected hooks"),
    "FSR4 capable GPU": ("显卡支持 FSR4", "Detected capabilities"),
    "Frame generation rectangle, adjust for letterboxed content##2": (
        "帧生成区域，可针对带黑边的画面调整", "Literal tooltip, not a widget ID"),
    "Hooks": ("钩子", "Status card"),
    "Idle": ("空闲", "Sidebar status"),
    "OFF": ("关闭", "Frame generation state"),
    "ON": ("开启", "Frame generation state"),
    "Paused, 3rd person detected": ("已暂停，检测到第三人称视角", "Reprojection status"),
    "Performance Overlay": ("性能叠加层", "Overlay window title"),
    "Please put dlss-enabler-headless.dll into OptiScaler folder": (
        "请将 dlss-enabler-headless.dll 放入 OptiScaler 文件夹", "Missing replacement library"),
    "Please put dlssg_to_fsr3_amd_is_better.dll into OptiScaler folder": (
        "请将 dlssg_to_fsr3_amd_is_better.dll 放入 OptiScaler 文件夹", "Missing replacement library"),
    "Presets are overridden externally": ("预设已被外部配置覆盖", "DLSS preset warning"),
    "Reflex not hooked": ("未挂接 Reflex", "Low latency status"),
    "Requires disabling dilated motion vectors": ("需要关闭膨胀运动矢量", "XeFG compatibility warning"),
    "Resets Frame generation rectangle##2": ("重置帧生成区域", "Literal tooltip, not a widget ID"),
    "Restart the game to apply correct XeFG settings!": (
        "请重启游戏以应用正确的 XeFG 设置！", "XeFG configuration warning"),
    "Save Settings and restart to apply the changes": (
        "保存设置并重启游戏以应用更改", "Restart hint"),
    'Selects how many elements close to the camera\nshould be shown over the reprojected image.\n'
    'This prevents your gun from being moved in weird ways.\n\n'
    'Use "Show static elements" to help you adjust it\n'
    'Unreal Engine games are usually around 0.10\nCyberpunk is around 0.02': (
        '选择在重投影画面上保留多少靠近镜头的元素，\n以避免枪械等物体发生异常位移。\n\n'
        '可使用“显示静态元素”辅助调整。\n虚幻引擎游戏通常约为 0.10，\n赛博朋克约为 0.02。',
        "Reprojection depth tooltip, including literal quotes"),
    "Shaders": ("着色器", "Compatibility card"),
    "Splash": ("启动提示", "Splash window title"),
    "Spoofing": ("硬件信息伪装", "Compatibility card"),
    "Startup": ("启动", "Compatibility card"),
    "Status": ("状态", "Sidebar and card category"),
    "Update available: %s (current %s)": (
        "有可用更新：%s（当前 %s）", "Version notification"),
    "Using Reflex's limit with FSR FG has performance overhead": (
        "配合 FSR 帧生成使用 Reflex 帧率限制会产生性能开销", "Frame limiter warning"),
    "Using a subset of features from DLSS Enabler": (
        "使用 DLSS Enabler 的部分功能", "Replacement library description"),
    "XeFG only supports HDR10": ("XeFG 仅支持 HDR10", "HDR compatibility warning"),
    "Yes": ("是", "Sidebar status"),
    "amd_fidelityfx_dx12.dll is missing!": (
        "缺少 amd_fidelityfx_dx12.dll！", "Missing library warning"),
    "libxess_fg.dll is missing!": ("缺少 libxess_fg.dll！", "Missing library warning"),
    "nvngx replacement": ("nvngx 替代库", "Detected capabilities"),
    "nvngx_dlss.dll not found, DLSS disabled!": (
        "未找到 nvngx_dlss.dll，DLSS 已禁用！", "Missing library warning"),
}
