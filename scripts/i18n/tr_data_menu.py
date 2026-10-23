# -*- coding: utf-8 -*-
"""Additional menu strings found by the static coverage audit after upstream sync."""

TR_MENU = {
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
