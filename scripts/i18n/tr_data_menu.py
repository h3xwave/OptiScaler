# -*- coding: utf-8 -*-
"""Additional menu strings found by the static coverage audit after upstream sync."""

TR_MENU = {
    # Upstream sync through 992f4e19: plugin tabs, AMD flip metering, DLSSD and Vulkan present mode.
    "Flip Meter (WIP)": ("翻转节拍（开发中）", "AMD driver flip metering output"),
    "Frames of a FG Nvngx Replacement, paced by AMD's driver flip metering\n\n- AMD only, needs driver support\n"
    "- Only generates in exclusive or borderless fullscreen\n- Works with Anti-Lag 2": (
        "由 AMD 驱动翻转节拍控制帧生成替代方案的输出节奏\n\n- 仅支持 AMD 显卡，需要驱动支持\n"
        "- 仅在独占全屏或无边框全屏下生成帧\n- 可与 Anti-Lag 2 同时使用", "Flip Meter output tooltip"),
    "Flip Meter Settings": ("翻转节拍设置", "Flip Meter card"),
    "Flip metering isn't supported by the driver": (
        "当前驱动不支持翻转节拍", "Unsupported Flip Meter reason"),
    "Flip HUDless": ("翻转无界面纹理", "HUDless texture orientation"),
    "Flip the HUDless texture\nGames can also request it with the Opti.Hudless.Flip parameter": (
        "上下翻转无界面纹理\n游戏也可通过 Opti.Hudless.Flip 参数请求翻转", "Flip HUDless tooltip"),
    "Driver pacing: %s, %uX": ("驱动节拍：%s，%u 倍", "Driver flip metering status"),
    "frame index mode": ("帧索引模式", "AMD flip metering mode"),
    "adaptive mode": ("自适应模式", "AMD flip metering mode"),
    "AMD driver flip metering holds the flips of the generated frames\n"
    "Adaptive mode is FSR's and paces one generated frame,\nframe index mode paces more": (
        "AMD 驱动翻转节拍会控制生成帧的呈现节奏\n"
        "自适应模式由 FSR 控制，每次只安排一帧生成帧；\n帧索引模式可安排更多生成帧", "Driver pacing tooltip"),
    "Driver pacing: off while no frames are generated": (
        "驱动节拍：当前未生成帧，节拍已关闭", "Driver pacing inactive"),
    "Frame generation is off, or the game doesn't send\nits inputs, like in menus and loading screens": (
        "帧生成已关闭，或游戏未发送帧生成输入\n例如在菜单和加载画面中", "Driver pacing inactive tooltip"),
    "Driver pacing: off, only the game's frames are shown": (
        "驱动节拍：已关闭，仅显示游戏自身渲染的帧", "Driver pacing error"),
    "Needs exclusive fullscreen or a window covering the whole display": (
        "需要独占全屏，或覆盖整个显示器的窗口", "Flip Meter fullscreen requirement"),
    "The driver rejected the config: %08X, status %u": (
        "驱动拒绝了该配置：%08X，状态 %u", "Flip Meter configuration error"),
    "The driver allows up to %dX, the FG replacement %dX": (
        "驱动最多允许 %d 倍，当前帧生成替代方案为 %d 倍", "Flip Meter multiplier limit"),
    "AMD's driver only paces 2X by default. More needs a registry setting.\n"
    "Button below creates a .reg file next to the game's exe.\nRun it and restart your computer.": (
        "AMD 驱动默认只支持 2 倍节拍，更高倍率需要修改注册表。\n"
        "下方按钮会在游戏 EXE 旁生成 .reg 文件。\n运行该文件并重启电脑。", "Flip Meter registry notice"),
    "Create .reg file": ("创建 .reg 文件", "Flip Meter registry action"),
    "Create .reg file##flipmeter": ("创建 .reg 文件", "Flip Meter registry action"),
    "Saved %s": ("已保存 %s", "File creation success"),
    "Couldn't create it: %s": ("无法创建：%s", "File creation failure"),
    "Double-click it and allow the change (needs admin), then restart Windows. The file says how to undo it.": (
        "双击该文件并允许更改（需要管理员权限），然后重启 Windows。文件中说明了如何撤销更改。", "Registry file instructions"),
    "Ray Reconstruction": ("光线重建", "RR upscaler selector"),
    "No denoise": ("不降噪", "RR upscaler choice"),
    "Upscaler used when Ray Reconstruction is turned on in the game.": (
        "游戏中启用光线重建时使用的超分辨率算法。", "RR offer tooltip"),
    "No DLSSD can run on this GPU, so the game doesn't offer Ray Reconstruction.\n"
    "Picking an upscaler here lets you turn it on in the game.": (
        "该显卡无法运行 DLSSD，因此游戏不会提供光线重建。\n在此选择超分算法可在游戏中启用它。", "RR unavailable tooltip"),
    "This upscaler can't denoise.\nWith DLSSD on in the game, image may look grainy or noisy.": (
        "此超分算法无法降噪。\n游戏中启用 DLSSD 时，画面可能出现颗粒或噪点。", "RR denoise warning"),
    "DLSSD is on in the game, but this upscaler can't denoise.\nImage may look grainy or noisy.": (
        "游戏中已启用 DLSSD，但此超分算法无法降噪。\n画面可能出现颗粒或噪点。", "RR denoise warning"),
    "Save Settings and restart the game to apply": (
        "保存设置并重启游戏以应用更改", "RR restart notice"),
    "FSR FG Provider": ("FSR 帧生成提供方", "Custom FSR FG selector"),
    "FFX frame generation and swapchain used by FSR FG\nCustom ones are from custom\\<name>\\ffx_fg(_vk) or plugins": (
        "FSR 帧生成使用的 FFX 帧生成与交换链\n自定义提供方来自 custom\\<名称>\\ffx_fg(_vk) 或插件", "FSR FG provider tooltip"),
    "GB Ver: %d.%d": ("GB 版本：%d.%d", "Nvngx anti-ghosting version"),
    "DE Ver: %d.%d.%d.%d   GB Ver: %d.%d": ("DE 版本：%d.%d.%d.%d   GB 版本：%d.%d", "Nvngx versions"),
    "Lowers sharpness at high contrast areas.": (
        "降低高对比区域的锐化强度。", "Contrast tooltip"),
    "If UI is too bright, disable this option": (
        "如果 UI 过亮，请关闭此选项", "UI gamma tooltip"),
    "Unblend UI": ("分离 UI 叠加", "HUDfix UI unblend"),
    "Rebuild the HUDless by removing the UI texture from the frame\n"
    "FSR-FG gets the UI only this way, DLSSG takes the UI texture directly": (
        "从画面中移除 UI 纹理以重建无界面帧\nFSR 帧生成只能通过这种方式取得 UI，DLSSG 则直接使用 UI 纹理", "Unblend UI tooltip"),
    "Afterburner": ("Afterburner 风格", "Overlay appearance preset"),
    "As MSI Afterburner: Unispace Bold, orange labels, outlined, no background": (
        "仿 MSI Afterburner 风格：Unispace 粗体、橙色标签、黑色描边、无背景底板", "Afterburner preset tooltip"),
    "Lemon zest": ("柠檬青", "Overlay appearance preset"),
    "A winning submission from user Voodoo: a top center strip in Unispace Bold, lime values": (
        "用户 Voodoo 的获奖预设：顶部居中的 Unispace 粗体信息条，青柠色数值", "Lemon zest preset tooltip"),
    "Present Mode": ("呈现模式", "Vulkan present mode selector"),
    "Game's": ("游戏默认", "Vulkan present mode default"),
    "Game's present mode: %s": ("游戏当前呈现模式：%s", "Vulkan present mode status"),
    "Overrides the game's Vulkan present mode, the game recreates its swapchain to apply it.\n\n"
    "Immediate: no V-Sync, tears.\nMailbox: no tearing, newest frame replaces the queued one.\n"
    "FIFO: V-Sync.\nFIFO Relaxed: V-Sync, tears when below the refresh rate.\n"
    "FIFO Latest Ready: V-Sync, shows the newest ready frame at each refresh.\n\n"
    "Mailbox and FIFO Latest Ready can drop generated frames above the refresh rate.\n"
    "Only modes the display supports are listed.": (
        "覆盖游戏的 Vulkan 呈现模式；游戏会重建交换链以应用更改。\n\n"
        "Immediate：关闭垂直同步，可能出现撕裂。\nMailbox：不撕裂，新帧替换已排队帧。\n"
        "FIFO：启用垂直同步。\nFIFO Relaxed：启用垂直同步，低于刷新率时可能撕裂。\n"
        "FIFO Latest Ready：启用垂直同步，每次刷新显示最新的就绪帧。\n\n"
        "Mailbox 和 FIFO Latest Ready 在高于刷新率时可能丢弃生成帧。\n仅列出显示器支持的模式。", "Vulkan present mode tooltip"),
    "VLK + Ext": ("Vulkan + 扩展", "Vulkan spoofing status"),
    "VLK Ext": ("Vulkan 扩展", "Vulkan extension spoofing status"),
    "VLK": ("Vulkan", "Vulkan spoofing status"),
    "DXGI": ("DXGI", "DXGI spoofing status"),
    "Spoof": ("伪装", "Spoofing status label"),
    "Ultra Performance": ("超高性能", "Upscaler quality preset"),
    # Upstream sync through ab379b25: Vulkan FFX, custom providers and overlay changes.
    "Custom DLSSG from the custom folder": (
        "从 custom 文件夹加载的自定义 DLSSG", "Custom frame generation backend"),
    "Custom DLSSG from custom\\%s\\dlssg": (
        "来自 custom\\%s\\dlssg 的自定义 DLSSG", "Custom frame generation path"),
    "Frame Generation (%s)": ("帧生成（%s）", "Custom frame generation section title"),
    "Missing amd_fidelityfx_framegeneration_vk.dll": (
        "缺少 amd_fidelityfx_framegeneration_vk.dll", "Vulkan frame generation availability"),
    "FFX Vk": ("FFX Vulkan", "Vulkan FidelityFX loader status"),
    "FFX Vk SR": ("FFX Vulkan 超分辨率", "Vulkan FidelityFX upscaler status"),
    "FFX Vk FG": ("FFX Vulkan 帧生成", "Vulkan FidelityFX frame generation status"),
    "Hide Averages": ("隐藏平均值", "Overlay averages visibility"),
    "Only the current values, without the averages of FPS, frame time and upscaler time": (
        "仅显示当前数值，不显示帧率、帧时间及超分辨率耗时的平均值", "Hide averages tooltip"),
    "Strip": ("顶部信息条", "Overlay appearance preset"),
    "A strip at the top center: Bahnschrift, FPS and upscaler time in orange on a dark panel": (
        "屏幕顶部居中的信息条：Bahnschrift 字体，在深色面板上以橙色显示帧率和超分辨率耗时", "Strip preset tooltip"),
    "Low latency timings, whole frame:": ("低延迟耗时，整帧：", "Overlay low latency total label"),
    # Upstream FPS overlay appearance/layout settings (08e13adf).
    "A file in C:\\Windows\\Fonts or a full path, Enter applies it": (
        "可输入 C:\\Windows\\Fonts 下的字体文件名或完整路径，按回车键生效", "Custom overlay font tooltip"),
    "Appearance": ("外观", "Overlay appearance section"),
    "Applies a copied code. Settings it doesn't list go back to their defaults.": (
        "应用已复制的设置代码；代码中未包含的设置将恢复默认值。", "Import overlay settings tooltip"),
    "Before the overlay's scale, the far left is the menu's font size": (
        "叠加层整体缩放前的基础字号；拉到最左端则跟随主菜单字号", "Overlay font size tooltip"),
    "Choose a Windows system font or enter any custom .ttf/.otf file below": (
        "选择 Windows 系统字体，或在下方输入自定义 .ttf/.otf 字体文件", "Overlay font selector tooltip"),
    "Colors": ("颜色", "Overlay color section"),
    "Copies your overlay settings as a code to keep or share": (
        "将当前叠加层设置复制为代码，便于备份或分享", "Export overlay settings tooltip"),
    "Copy Code": ("复制代码", "Export overlay settings button"),
    "Corner Rounding": ("圆角大小", "Menu and overlay corner radius"),
    "Custom's rows back to the ones of Full + Graph": (
        "将自定义显示行恢复为“全面信息 + 曲线图”的默认配置", "Reset overlay rows tooltip"),
    "Extra horizontal tracking in pixels between characters": (
        "字符之间额外的水平字距（单位：像素）", "Letter spacing tooltip"),
    "FPS Row": ("帧率行内容", "Overlay FPS row selector"),
    "Font": ("字体", "Overlay font selector"),
    "Font Size": ("字号", "Overlay font size"),
    "Graph Height": ("图表高度", "Overlay graph height"),
    "Horizontal Position": ("水平位置", "Custom overlay position"),
    "How often FPS and times change, averaged in between. Higher is easier to read.": (
        "帧率与耗时的刷新间隔，期间的数据取平均值显示。间隔越大数值越平稳易读。", "Overlay update interval tooltip"),
    "Just the number, or with the API, frame time or average FPS, frame generation and upscaler": (
        "仅显示帧率数值，或附带显示图形 API、帧时间/平均帧率、帧生成及超分辨率算法", "Overlay FPS row tooltip"),
    "Layout": ("布局", "Overlay layout section"),
    "Letter Spacing": ("字间距", "Overlay text spacing"),
    "Menu font": ("菜单字体", "Overlay font fallback"),
    "Names like FPS: and Avg:": ("调整如 FPS:、Avg: 等前缀标签的字号缩放比例", "Overlay label scale tooltip"),
    "Order": ("顺序", "Overlay row order column"),
    "Paste Code": ("粘贴代码", "Import overlay settings button"),
    "Presets": ("预设", "Overlay appearance presets"),
    "Presets of the rows, Custom shows the ones chosen in Rows.\nThe Overlay Cycle key switches between them.": (
        "选择显示行的预设；设为“自定义”时按下方“显示行配置”中的勾选项显示。\n可使用切换快捷键在各预设间循环切换。", "Overlay type tooltip"),
    "Reset Appearance": ("重置外观", "Reset overlay appearance button"),
    "Row": ("显示项", "Overlay row column"),
    "Row Spacing": ("行间距", "Overlay row spacing"),
    "Rows": ("显示行配置", "Overlay rows section"),
    "Shadow Strength": ("阴影强度", "Overlay shadow strength"),
    "Share Settings": ("分享设置", "Overlay settings exchange section"),
    "Size of the FPS overlay, independent from the menu scale unless set to Same as menu": (
        "帧率叠加层的缩放比例；除非设为“与菜单相同”，否则独立于主菜单缩放", "Overlay scale tooltip"),
    "Text": ("文字", "Overlay text section"),
    "Text Shadow": ("文字阴影", "Overlay shadow selector"),
    "The menu theme's colors for the labels, values, graph and background": (
        "标签、数值、图表和背景跟随主菜单主题配色", "Overlay theme tooltip"),
    "The numbers": ("调整帧率、帧时间等实时数值的字号缩放比例", "Overlay value scale tooltip"),
    "Thickness and darkness of the shadow, thickness of the outline": (
        "调整阴影的厚度与深浅，或文字描边的粗细", "Overlay shadow strength tooltip"),
    "Update Interval": ("刷新间隔", "Overlay update interval"),
    "Use Theme": ("使用主题配色", "Overlay theme colors"),
    "Vertical Position": ("垂直位置", "Custom overlay position"),
    # Additional labels passed through arrays, slider formats, and local UI helpers.
    "Top Center": ("顶部居中", "Overlay position choice"),
    "Bottom Center": ("底部居中", "Overlay position choice"),
    "Low latency timings": ("低延迟耗时统计", "Overlay type choice"),
    "Same as menu (%.1f)": ("与菜单相同 (%.1f)", "Overlay scale slider default format"),
    "The rows of %s, set Overlay Type to Custom to change them.": (
        "当前显示的是“%s”预设的行，将叠加层类型设为“自定义”即可修改。", "Overlay rows status notice"),
    "Frame Time": ("帧时间", "Overlay row name"),
    "Frame Time Graph": ("帧时间曲线图", "Overlay row name"),
    "Upscaler Time": ("超分辨率耗时", "Overlay row name"),
    "Upscaler Time Graph": ("超分辨率耗时曲线图", "Overlay row name"),
    "Low Latency Timings": ("低延迟耗时", "Overlay row name"),
    "The FPS, the frame generation and the upscaler, FPS Row below sets what's shown": (
        "显示帧率、帧生成及超分辨率信息，具体内容由下方“帧率行内容”决定", "Overlay FPS row checkbox tooltip"),
    "Render -> output resolution and upscale ratio, while upscaling": (
        "启用超分辨率时，显示渲染分辨率 -> 输出分辨率及超分缩放倍率", "Overlay upscale row checkbox tooltip"),
    "The last frame time and the average": ("显示最近一帧的耗时与平均帧时间", "Overlay frame time row tooltip"),
    "The frame times of the last frames": ("显示近期帧时间的实时波动曲线图", "Overlay frame time graph row tooltip"),
    "The upscaler's last time and the average": (
        "显示超分辨率最近一帧的 GPU 耗时与平均耗时", "Overlay upscaler time row tooltip"),
    "The upscaler's times of the last frames": (
        "显示近期超分辨率 GPU 耗时的实时波动曲线图", "Overlay upscaler graph row tooltip"),
    "Timings of the frame from the low latency markers, while there are any": (
        "当存在低延迟标记数据时，显示各阶段的帧延迟耗时", "Overlay low latency row tooltip"),
    "With Frame Time": ("附带帧时间", "Overlay FPS row choice"),
    "With Average FPS": ("附带平均帧率", "Overlay FPS row choice"),
    "Upscale Ratio in Presets": ("在预设中显示超分缩放倍率", "Overlay row option"),
    "The Upscale Ratio row in the presets from Simple on, Custom has it in its rows": (
        "在“简洁概览”及更详细的预设中显示超分缩放倍率行；自定义模式可在“显示行配置”中单独勾选", "Overlay ratio row tooltip"),
    "Reset Rows & Spacing": ("重置显示行与间距", "Reset custom overlay rows"),
    "Reset Spacing": ("重置行间距", "Reset overlay row spacing"),
    "Classic": ("经典", "Overlay appearance preset"),
    "Afterburner-Like": ("Afterburner 风格", "Overlay appearance preset"),
    "Glass Strip": ("毛玻璃顶栏", "Overlay appearance preset"),
    "OptiScaler's overlay: every row with the graphs, grey labels with a shadow": (
        "OptiScaler 默认叠加层：包含全部数据行与曲线图，带阴影的灰色标签", "Default overlay preset tooltip"),
    "OptiScaler's earlier overlay: just the FPS in white, no shadow": (
        "OptiScaler 经典叠加层：仅显示白色帧率文字，无阴影", "Classic overlay preset tooltip"),
    "As MSI Afterburner: Unispace Bold, orange labels, outlined, no background": (
        "仿 MSI Afterburner 风格：Unispace 粗体、橙色标签、黑色描边、无背景底板", "Afterburner overlay preset tooltip"),
    "A strip at the top center: Bahnschrift, cyan values on a dark glass panel": (
        "屏幕顶部居中的深色毛玻璃顶栏：Bahnschrift 字体配青色数值", "Glass overlay preset tooltip"),
    "Compact Labels": ("精简标签", "Overlay compact labels option"),
    "Shorter labels for a narrower overlay: UPS, FT, UT": (
        "使用 UPS、FT、UT 等缩写标签，使叠加层更紧凑", "Overlay compact labels tooltip"),
    "Square": ("直角", "Corner rounding slider zero format"),
    "Custom Font File": ("自定义字体文件", "Overlay font file input"),
    "Menu font size": ("跟随菜单字号", "Overlay font size slider default format"),
    "Every frame": ("每帧实时更新", "Overlay update interval slider zero format"),
    "Label Size": ("标签大小", "Overlay label scale"),
    "Value Size": ("数值大小", "Overlay value scale"),
    "Shadow": ("阴影", "Overlay shadow type/color"),
    "Outline": ("描边", "Overlay shadow type"),
    "Labels": ("标签", "Overlay label color"),
    "Values": ("数值", "Overlay value color"),
    "Graph": ("图表", "Overlay graph color"),
    "Background": ("背景", "Overlay background color"),
    "Copied to the clipboard": ("已复制到剪贴板", "Export overlay settings status"),
    "Applied, Save Settings to keep it": ("已应用，请点击“保存设置”以持久化保存", "Import overlay settings status"),
    "No FPS overlay code in the clipboard": ("剪贴板中未检测到有效的叠加层设置代码", "Import overlay settings error"),
    # ConfigCheckbox tooltips across menu_common.cpp caught by the 3rd-argument check.
    "Adds a tab on top of the list that shows only the picked boxes": (
        "在侧边栏顶部新增一个选项卡，仅显示下方勾选的功能模块", "Show Custom tab tooltip"),
    "Blur the game behind the menu\nOnly visible when Background Alpha is below 1": (
        "对菜单背后的游戏画面应用模糊效果\n仅当“背景不透明度”小于 1 时可见", "Background blur tooltip"),
    "Disable supported overlays (autoenabled with OptiFG)\nIncluding Steam Input (controller issues)": (
        "禁用受支持的第三方叠加层（使用 OptiFG 时自动启用）\n同时涵盖 Steam 输入叠加层（可缓解部分手柄失灵问题）", "Disable overlays tooltip"),
    "Disables Startup Splash message (bottom left corner)": (
        "禁用游戏启动时左下角的提示横幅", "Disable splash tooltip"),
    "Dynamic Resolution Scaling\nFix for games ignoring official DRS limits": (
        "动态分辨率缩放 (DRS)\n修复部分游戏无视官方动态分辨率上下限的问题", "DRS fix tooltip"),
    "Enable Nvidia Extension spoofing for Vulkan\nDetailed modifications available in the INI": (
        "为 Vulkan 启用 NVIDIA 扩展伪装\n可在 INI 配置文件中调整详细参数", "Vulkan extension spoofing tooltip"),
    "Enable Nvidia GPU spoofing for DXGI adapter\nDetailed modifications available in the INI": (
        "为 DXGI 显示适配器启用 NVIDIA 显卡型号伪装\n可在 INI 配置文件中调整详细参数", "DXGI spoofing tooltip"),
    "Enable Nvidia GPU spoofing for Vulkan\nDetailed modifications available in the INI": (
        "为 Vulkan 启用 NVIDIA 显卡型号伪装\n可在 INI 配置文件中调整详细参数", "Vulkan spoofing tooltip"),
    "Enable checking Github for latest version\nOnly works on stable/final releases": (
        "启动时连接 GitHub 检查是否有新版本\n仅在正式稳定版中生效", "Check for update tooltip"),
    "Enables drawing of Interpolation skip lines": (
        "绘制插帧跳过调试指示线", "FSR FG debug skip lines tooltip"),
    "Enables drawing of Pacing lines": (
        "绘制帧节奏调度 (Pacing) 调试指示线", "FSR FG debug pacing lines tooltip"),
    "Enables drawing of Tear and Interpolation skip lines": (
        "绘制画面撕裂与插帧跳过调试指示线", "FSR FG debug tear lines tooltip"),
    "Enables the FSR FG watermark": (
        "启用 FSR 帧生成调试水印", "FSR FG watermark tooltip"),
    "Extended sliders limit for quality presets\n\nUsing this option changes resolution detection logic\nand might cause issues and crashes!": (
        "放宽画质预设滑块的调节范围上限\n\n开启此项会改变分辨率检测逻辑，\n可能导致画面异常或游戏崩溃！", "Extended limits tooltip"),
    "Hook the inputs of this API": (
        "挂接此 API 的超分辨率输入源", "Upscaler input enable tooltip"),
    "Let OptiScaler load *.asi files from plugins folder": (
        "允许 OptiScaler 从 plugins 文件夹加载 *.asi 插件", "Load ASI plugins tooltip"),
    "Only hook ntdll.dll methods\nDisable for switching back to kernel hooks": (
        "仅挂接 ntdll.dll 函数\n关闭此项将切换回内核层 (Kernel) 钩子", "Ntdll hooks tooltip"),
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
    # Upstream sync through f005b3db: OptiSharpen, flip meter diagnostics and new status text.
    "(the replacement supports up to %dx)": (
        "（该替代方案最高支持 %d 倍）", "FG replacement multiplier warning"),
    "Clamps the final image to the [0, 1] range.\n\n"
    "Prevents overshoot artifacts such as bright halos or negative colors.\n"
    "Recommended for LDR pipelines; optional for HDR depending on tone-mapping.\n\n"
    "Off when not set, games that report SDR can still send HDR color": (
        "将最终图像限制在 [0, 1] 范围内。\n\n"
        "防止亮部光晕或负色等过冲伪影。\n"
        "推荐用于 LDR 管线；HDR 是否启用取决于色调映射。\n\n"
        "未设置时关闭；上报 SDR 的游戏仍可能发送 HDR 颜色", "Clamp output tooltip"),
    "Controls how the sharpening adapts to the detected edges.\n\n"
    "Negative values smooth the edges.\nPositive values enhance the edges.\n"
    "0 is uniform.": (
        "控制锐化如何根据检测到的边缘进行调整。\n\n"
        "负值会平滑边缘。\n正值会增强边缘。\n0 表示均匀处理。", "Edge response tooltip"),
    "Driver pacing: %s": ("驱动节拍：%s", "Driver flip metering status"),
    "Driver pacing: the driver doesn't pace the flips (%08X, status %u)": (
        "驱动节拍：驱动未对翻转进行节拍控制（%08X，状态 %u）", "Driver flip metering error"),
    "Edge Response": ("边缘响应", "Neural sharpening edge response"),
    "For when the game sends a UI texture, but you want to disable it\n"
    "Greyed out while the game doesn't send one": (
        "当游戏发送 UI 纹理但你希望禁用时使用\n游戏未发送 UI 纹理时该项为灰色", "Disable UI texture tooltip"),
    "Model": ("模型", "Sharpener model selector"),
    "Model A: Standard sharpening.\nModel B: Edge-enhanced.": (
        "模型 A：标准锐化。\n模型 B：边缘增强。", "Neural model tooltip"),
    "Neural Model": ("神经模型", "Neural sharpening model label"),
    "Neural Sharpening Parameters": ("神经锐化参数", "Neural sharpening settings card"),
    "Normal: The final image.\n"
    "Sharpening map: The sharpening that gets applied, plain gray means no change.\n"
    "Residual map: Where the network wants to change the image.": (
        "Normal：最终图像。\n"
        "Sharpening map：实际应用的锐化量，纯灰色表示无变化。\n"
        "Residual map：网络希望改变图像的位置。", "Neural sharpening debug view tooltip"),
    "Normal: The final image.\n"
    "Sharpening map: The relative luma change, plain gray means no change.\n"
    "Change magnitude: How much each pixel changes, black means no change.": (
        "Normal：最终图像。\n"
        "Sharpening map：相对亮度变化，纯灰色表示无变化。\n"
        "Change magnitude：每个像素的变化幅度，黑色表示无变化。", "OptiSharpen debug view tooltip"),
    "ON %dx": ("开启 %d 倍", "Frame generation status"),
    "Natural D10: Natural sharpening.\n"
    "Crisp D10 p50: Stronger.\n"
    "(fp16 packed): The same networks in half precision, written for packed math.\n"
    "Faster on Dx12 / Vulkan, Dx11 runs them in fp32.\n"
    "All use a 25 tap (5x5) window and overshoot the local range by up to 15 percent.\n"
    "Each model scales the strength, the top of the slider is its best point.": (
        "Natural D10：自然锐化。\n"
        "Crisp D10 p50：更强。\n"
        "（fp16 packed）：相同的网络以半精度实现，为打包数学优化。\n"
        "在 Dx12 / Vulkan 上更快，Dx11 以 fp32 运行。\n"
        "均使用 25 抽头（5x5）窗口，并最多超出局部范围百分之十五。\n"
        "每个模型会缩放强度，滑块顶端即其最佳效果点。", "OptiSharpen model tooltip"),
    "For when the game sends HUDless, but you want to disable it\n"
    "Might be required for some sets of DispatchFlags": (
        "当游戏发送无界面画面而你希望禁用它时使用\n某些 DispatchFlags 组合可能需要此设置", "Nvngx HUDless tooltip"),
    "For when the game sends HUDless, but you want to disable it\n"
    "Greyed out while the game doesn't send one": (
        "当游戏发送无界面画面而你希望禁用它时使用\n游戏未发送无界面画面时该项为灰色", "HUDless tooltip"),
    "Cutoffs transparency from UI to help with interpolation\n0.0 is auto": (
        "裁剪 UI 的半透明部分以辅助插帧\n0.0 为自动计算", "Nvngx HUD cutoff tooltip"),
    "OptiSharpen Parameters": ("OptiSharpen 参数", "OptiSharpen settings card"),
    "Please select %s Frame Generation in the game options\n"
    "You might need to select %s first": (
        "请在游戏选项中选择 %s 帧生成\n你可能需要先选择 %s", "Frame generation input hint"),
    "Reset Neural Values": ("重置神经锐化数值", "Neural sharpening reset action"),
    "Reset OptiSharpen Values": ("重置 OptiSharpen 数值", "OptiSharpen reset action"),
    "Select the sharpening filter to apply.\n\n"
    "Upscaler's default: Uses the sharpening provided by the upscaler.\n"
    "RCAS: AMD's RCAS, modified for Contrast and MAS.\n"
    "Depth Aware: Smarter sharpening with fewer artifacts (heavier).\n"
    "Neural (BaBa): Small neural network from the BaBa ReShade shaders. Only changes the luma and\n"
    "skips aliased edges and fireflies. 0.5 strength is the default intensity of the ReShade shader.\n"
    "OptiSharpen: Small neural network trained for OptiScaler. Only changes the luma, works the same\n"
    "for SDR and HDR. 0.5 strength is the trained strength.\n"
    "Neural shaders use RCAS when their shader isn't available for the current API.\n\n"
    "By default uses a sharpening value provided by the game.\n"
    "Select 'Override' under 'Sharpness' and adjust the slider to change it.": (
        "选择要应用的锐化滤镜。\n\n"
        "Upscaler's default：使用超分辨率算法自带的锐化。\n"
        "RCAS：AMD 的 RCAS，针对对比度和 MAS 修改。\n"
        "Depth Aware：更智能的锐化，伪影更少（开销更大）。\n"
        "Neural (BaBa)：来自 BaBa ReShade 着色器的小型神经网络。仅改变亮度，并\n"
        "跳过抗锯齿边缘和萤火虫。0.5 强度对应 ReShade 着色器的默认强度。\n"
        "OptiSharpen：为 OptiScaler 训练的小型神经网络。仅改变亮度，SDR 和 HDR\n"
        "效果一致。0.5 强度即训练强度。\n"
        "当前 API 没有对应着色器时，神经锐化会使用 RCAS。\n\n"
        "默认使用游戏提供的锐化值。\n在“Sharpness”下选择“Override”并调整滑块即可更改。", "Sharpening method tooltip"),
    "Status 7: the driver's window manager doesn't report the swapchain's window\n"
    "in its fullscreen state, the window is likely composed by DWM\n"
    "or shown on an overlay plane": (
        "状态 7：驱动的窗口管理器未将该交换链窗口报告为全屏状态，窗口可能由 DWM 合成\n"
        "或显示在叠加平面上", "Flip meter window not eligible tooltip"),
    "Status 8: a flip came without a flip meter Present, with a target time of 0\n"
    "or with more generated frames than configured": (
        "状态 8：翻转未携带可用的节拍信息，目标时间为 0\n或生成的帧数超过配置", "Flip meter no pacing info tooltip"),
    "Status:": ("状态：", "Frame generation status label"),
    "The driver doesn't see the game as a fullscreen app flipped straight to the display. "
    "Try exclusive fullscreen and closing overlays (Discord, Steam, Game Bar, RTSS) and windows on top of the game.": (
        "驱动未将游戏识别为直接翻转至显示器的全屏应用。请尝试独占全屏，并关闭覆盖层"
        "（Discord、Steam、Game Bar、RTSS）以及游戏上方的窗口。", "Flip meter window not eligible"),
    "The driver got flips without usable pacing info.": (
        "驱动收到的翻转没有可用的节拍信息。", "Flip meter no pacing info"),
    "The driver has no pacing config for the swapchain.": (
        "驱动没有该交换链的节拍配置。", "Flip meter retry"),
    "The driver hasn't reported on the flips yet.": (
        "驱动尚未报告翻转状态。", "Flip meter default status"),
    # Upstream f005b3db dropdown items that aren't caught by the static coverage pass.
    "Model A (standard)": ("模型 A（标准）", "Neural sharpening model"),
    "Model B (edge-enhanced)": ("模型 B（边缘增强）", "Neural sharpening model"),
    "Natural D10": ("自然 D10", "OptiSharpen model"),
    "Crisp D10 p50": ("清晰 D10 p50", "OptiSharpen model"),
    "Natural D10 (fp16 packed)": ("自然 D10（fp16 打包）", "OptiSharpen model"),
    "Crisp D10 p50 (fp16 packed)": ("清晰 D10 p50（fp16 打包）", "OptiSharpen model"),
    "Normal": ("正常", "Debug view mode"),
    "Sharpening map": ("锐化图", "Debug view mode"),
    "Residual map": ("残差图", "Debug view mode"),
    "Change magnitude": ("变化幅度", "Debug view mode"),
    "Neural (BaBa)": ("神经锐化 (BaBa)", "Sharpening method"),
}
