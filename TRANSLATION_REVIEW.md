# OptiScaler 全量汉化审查对照表 (共 741 条)

本文档包含 OptiScaler 游戏内菜单界面的 **全部 741 条** 英文文本的简体中文翻译及其专业技术考量背景，供审阅评估。

## 模块 1：导航栏、主标签页与侧边栏 (Navigation, Tabs & Sidebar)（共 18 条）

| 序号 | 英文原文 (Source) | 中文翻译 (Target) | 翻译考量与术语依据 (Rationale) |
| :--- | :--- | :--- | :--- |
| 1 | `ADVANCED` | **高级** | 侧边栏高级设置分组标题，区分基础功能与进阶调优 |
| 2 | `Backend, sharpness and output scaling.` | **后端算法、锐化强度与输出分辨率缩放。** | 超分辨率选项卡副标题描述 |
| 3 | `Boxes picked in Menu > Custom Tab.` | **在“菜单 > 自定义选项卡”中挑选的显示卡片。** | 说明自定义页面内容来源的提示 |
| 4 | `Custom` | **自定义** | 自定义选项卡名称，玩家可把常用卡片固定在此 |
| 5 | `FG` | **帧生成** | 主界面底部或缩写栏中的 Frame Generation 紧凑标识 |
| 6 | `Frame generation source, output and pacing.` | **帧生成输入源、输出目标与帧平滑步进。** | 帧生成选项卡副标题描述 |
| 7 | `Frame limiter, low latency and V-Sync.` | **帧率限制器、低延迟模式与垂直同步。** | 延迟与帧率选项卡副标题描述 |
| 8 | `Game specific quirks applied by OptiScaler and loaded ASI plugins.` | **OptiScaler 应用的游戏专属修复补丁及已加载的 ASI 插件。** | Quirks 选项卡副标题描述 |
| 9 | `Init flags, hooks, plugins and game specific workarounds.` | **初始化标志、API 钩子、插件与游戏专属修复。** | 兼容性选项卡副标题描述 |
| 10 | `MAIN` | **主要** | 侧边栏主要设置分组标题，包含最核心的超分辨率、插帧与延迟选项 |
| 11 | `Menu scale, theme, FPS overlay and keybinds.` | **菜单缩放、界面主题、帧率叠加层与快捷键绑定。** | 菜单选项卡副标题描述 |
| 12 | `Mipmap bias and anisotropic filtering.` | **Mipmap 细节偏移与各向异性过滤。** | 纹理选项卡副标题描述 |
| 13 | `No` | **否** | 状态栏或开关的否定显示值 |
| 14 | `OP` | **补丁插件** | OptiPatcher 状态紧凑标识（用于侧边栏底部状态栏） |
| 15 | `SR` | **超分辨率** | Super Resolution（超分）状态紧凑标识 |
| 16 | `SYSTEM` | **系统** | 侧边栏系统底层分组标题，包含纹理过滤与驱动/API兼容性项 |
| 17 | `Spoof` | **伪装** | 显卡伪装开关紧凑状态标识 |
| 18 | `Support info. Filled dot: on or found, hollow dot: off or missing.` | **支持状态信息。实心圆点：已启用/已检测到，空心圆点：已关闭/缺失。** | 状态栏指示图标图例说明 |

## 模块 2：超分辨率技术 (Upscalers - DLSS / FSR / XeSS)（共 162 条）

| 序号 | 英文原文 (Source) | 中文翻译 (Target) | 翻译考量与术语依据 (Rationale) |
| :--- | :--- | :--- | :--- |
| 1 | `%dx%d -> %dx%d (%.2fx)` | **%dx%d -> %dx%d (%.2fx)** | 分辨率与缩放比率显示（渲染分辨率 -> 显示分辨率，保持格式串） |
| 2 | `%s active, but currently not used by the game\nPlease load into the game` | **%s 已激活，但游戏当前尚未使用\n请加载进入游戏场景** | 提示玩家当前超分已注入但游戏处于主菜单未开始渲染 |
| 3 | `%s%s \| %s \| Input: %s` | **%s%s \| %s \| 输入: %s** | 顶部状态栏：图形API、显卡型号与当前游戏调用超分输入源 |
| 4 | `(Active: %d)` | **(当前生效: %d)** | 指示当前运行时生效的数值项 |
| 5 | `(Active: %s)` | **(当前生效: %s)** | 指示当前运行时生效的字符串/枚举项 |
| 6 | `(DRS)` | **(动态分辨率)** | 动态分辨率缩放（Dynamic Resolution Scaling）标记 |
| 7 | `(Failed to hook)` | **(挂钩失败)** | 指示特定 API 接口的 detours 挂钩注入失败 |
| 8 | `Acc. Added Per Frame` | **每帧新增累积量** | FSR 3.1 历史时域累积每帧增量参数 |
| 9 | `All Ratios` | **全部比例** | 一次性覆盖所有超分辨率挡位缩放比例的设置项 |
| 10 | `Apply Change` | **应用更改** | 确认并应用单项设置参数的按钮 |
| 11 | `Apply Changes` | **应用更改** | 确认并应用整组设置参数的按钮 |
| 12 | `Auto` | **自动** | 让系统根据环境或硬件自动判定的选项 |
| 13 | `Balanced` | **平衡** | 超分辨率平衡挡位（平衡画质与性能，缩放比约 1.7x） |
| 14 | `Bicubic` | **双三次插值** | 经典平滑重采样滤波算法，适合下采样 |
| 15 | `Can't find nvngx.dll and libxess.dll and FSR inputs\nUpscaling support will NOT work.` | **未找到 nvngx.dll、libxess.dll 及 FSR 输入\n超分辨率支持将无法工作。** | 缺失必要驱动动态库时的严重警告提示 |
| 16 | `Catmull-Rom` | **Catmull-Rom 样条** | 保持良好对比度且振铃伪影较少的重采样滤波算法 |
| 17 | `Compatibility` | **兼容性** | 显卡伪装、钩子注入与启动修复选项卡 |
| 18 | `Corresponds to amount of accumulation added per frame\nat pixel coordinate where disocclusion occured or when\nreactive mask value is > 0.0f. Decreasing this and \ndrawing the ghosting object (IE no mv) to reactive mask \nwith value close to 1.0f can decrease temporal ghosting.\nDecreasing this could result in more thin feature pixels flickering.` | **对应在发生遮挡剔除或响应遮罩值 > 0.0 时，\n像素坐标每帧新增的时域累积量。降低此值并将\n残影物体写入响应遮罩可减少鬼影拖尾；\n但过低可能导致细小几何边缘闪烁。** | FSR 3.1 遮挡累积高级调优参数说明 |
| 19 | `Custom Tab` | **自定义选项卡** | 管理自定义主面板所展示的功能卡片 |
| 20 | `DEFAULT` | **默认** | 使用游戏原生内置配置的超分预设 |
| 21 | `DLAA` | **DLAA 原生抗锯齿** | Deep Learning Anti-Aliasing，以 1.0x 渲染分辨率运行 DLSS 降噪与抗锯齿网络 |
| 22 | `DLSS 3.7+, a better D preset\nRemoved on recent versions!` | **DLSS 3.7+ 推荐，更出色的 D 预设改进版\n较新版本驱动中已移除！** | DLSS Preset E 历史版本特性说明 |
| 23 | `Default for Perf mode\n2nd Gen Transformer` | **性能模式默认预设\n第二代 Transformer 架构模型** | DLSS Preset M/第二代网络模型说明 |
| 24 | `Default for Ultra Perf mode\n2nd Gen Transformers` | **超高性能模式默认预设\n第二代 Transformer 架构模型** | DLSS Preset N/第二代网络模型说明 |
| 25 | `Default model, Transformer` | **默认模型，Transformer 架构** | FSR 4 推荐神经网络模型类型 |
| 26 | `Default option.\nGood enough image quality and very fast.` | **默认选项。\n画质优良且运行速度极快。** | 常规重采样滤镜性能兼顾说明 |
| 27 | `Default preset for DLAA/Balanced/Quality modes...\n1st Gen Transformer` | **DLAA/平衡/质量模式默认预设...\n第一代 Transformer 架构模型** | DLSS Preset J 预设架构说明 |
| 28 | `Default preset for Performance/Balanced/Quality modes;\ngenerally favors image stability.\nRemoved on recent versions!` | **性能/平衡/质量模式默认预设；\n通常更偏向画面时域稳定性。\n较新版本中已移除！** | DLSS Preset D 经典稳定性预设说明 |
| 29 | `Default preset for Ultra Performance and DLAA modes\nRemoved on recent versions!` | **超高性能与 DLAA 模式默认预设\n较新版本中已移除！** | DLSS Preset F 预设特性说明 |
| 30 | `Designed primarily for downscaling.\nRetains good contrast with minimal artefacts, but softer than Lanczos.` | **主要针对下采样设计。\n保留良好对比度且瑕疵极少，但比 Lanczos 稍柔和。** | Catmull-Rom 下采样滤镜特性说明 |
| 31 | `Don't Use NTShared` | **禁用 NTShared 共享句柄** | 避免在某些 D3D11on12 游戏中因 NTShared 跨 API 共享纹理导致崩溃 |
| 32 | `Dump (Shift+Del)` | **转储调试信息 (Shift+Del)** | 将当前帧的超分中间纹理和状态写出到磁盘用于故障排查 |
| 33 | `Dx11 with Dx12 Settings` | **DX11 转 DX12 桥接设置** | DX11 游戏借助 D3D11on12 后台设备调用 DX12 超分/插帧的相关参数 |
| 34 | `Each internal FSR4 preset is tuned for a specific resolution.\nSelecting an FSR4 preset won't change the in-game\nupscaler preset!!!\n\nPreset 0 is meant for FSR Native AA\nPreset 1 is meant for Quality/Ultra Quality\nPreset 2 is meant for Balanced\nPreset 3 is meant for Performance\nPreset 4 is meant for DRS\nPreset 5 is meant for Ultra Performance` | **每个 FSR4 内部预设专门针对特定分辨率调优。\n在此选择 FSR4 预设不会更改游戏内的超分挡位！！！\n\n预设 0：专为 FSR 原生抗锯齿设计\n预设 1：适用于质量/超级质量\n预设 2：适用于平衡\n预设 3：适用于性能\n预设 4：适用于动态分辨率(DRS)\n预设 5：适用于超高性能** | FSR4 内部神经网络分辨率匹配预设说明 |
| 35 | `Each render preset has it strengths and weaknesses\nOverride to potentially improve image quality\nPress Apply after enable/disable` | **各渲染预设均有其优缺点\n覆盖预设可改善不同场景下的画质表现\n启用/禁用后请点击“应用更改”** | DLSS 渲染预设覆盖提示说明 |
| 36 | `Each render preset has it strengths and weaknesses\nOverride to potentially improve image quality\nPress apply after enable/disable` | **各渲染预设均有其优缺点\n覆盖预设可改善不同场景下的画质表现\n启用/禁用后请点击“应用更改”** | DLSS 渲染预设覆盖提示说明（小写变体） |
| 37 | `Enable` | **启用** | 开启指定功能的标准开关标签 |
| 38 | `FFX Upscaler` | **FFX 超分辨率** | AMD FidelityFX SDK 原生超分组件名称 |
| 39 | `FSR 3 Upscaler Manual Tuning` | **FSR 3 超分辨率手动微调** | 展开对 FSR3/3.1 内部时域算法参数的手动调节卡片 |
| 40 | `FSR 3.1 Presets:` | **FSR 3.1 预设：** | FSR 3.1 调优预设选择区域标签 |
| 41 | `FSR 4 network to run.\nAuto lets FFX pick the best one the GPU supports.` | **要运行的 FSR 4 神经网络模型。\n“自动”将允许 FFX 选择当前 GPU 支持的最佳模型。** | FSR4 神经网络模型选择说明 |
| 42 | `FSR-FG Inputs` | **FSR-FG 帧生成输入** | 捕获游戏内 FSR 帧生成管线输入参数的模块 |
| 43 | `FSR1` | **FSR 1.0** | AMD 第一代空间空间超分辨率算法（纯空间滤镜） |
| 44 | `FSR4 Model` | **FSR4 神经模型** | 选择 FSR4 机器学习网络模型文件（KPSS、SPLAT等） |
| 45 | `FSR4 Preset` | **FSR4 调优预设** | 选择 FSR4 内部针对特定分辨率训练的参数挡位 |
| 46 | `Fastest traditional option.\nProduces a very soft/blurry image, but might be okay for downscaling.` | **最快速的传统重采样算法。\n画面较柔和模糊，但很适合轻量级下采样场景。** | 双线性/双三次轻量重采样特性说明 |
| 47 | `Find the inputs by pattern matching` | **通过特征码匹配查找输入接口** | 在无符号或脱壳游戏中通过内存模式匹配抓取超分输入结构 |
| 48 | `Frame Gen` | **帧生成** | 帧生成（插帧）主选项卡，行业通用标准术语 |
| 49 | `Heavier version of Lanczos2.\nOffers the sharpest image, but is the most prone to ringing.\nConsidered the best along with Kaiser3.` | **Lanczos2 的高阶高负载版本。\n提供最锐利的边缘重建，但最容易出现边缘过冲振铃。\n与 Kaiser3 一同被公认为最出色的锐化滤波方案。** | Lanczos3 滤镜画质与开销特性说明 |
| 50 | `Help / Status` | **帮助 / 状态** | 调试诊断信息、钩子生效状态与 Wiki 说明 |
| 51 | `Hook the inputs of this API, needed before they can be used` | **挂钩此 API 的输入接口，需挂钩后方可捕获使用** | 开启 API 钩子以拦截超分参数的必要前置说明 |
| 52 | `Increasing this scales FSR3.1 computed shading\nchange value at read to have higher reactiveness.` | **增大此值可放大 FSR3.1 计算的光影变化强度，\n让画面对快速动态光影拥有更高的响应灵敏度。** | FSR 3.1 Shading Scale 着色响应缩放说明 |
| 53 | `Increasing this value may reduce white pixel temporal\nflickering around swaying thin objects that are disoccluding \none another often. Too high value may increase ghosting.` | **增大此值可减少反复遮挡的细小摆动物体边缘\n出现的白点时域闪烁现象。\n但数值过高可能会加重画面拖尾鬼影。** | FSR 3.1 最小遮挡累积参数调优提示 |
| 54 | `Init Flags (active)` | **初始化标志 (当前生效)** | 展示当前超分管线实际已激活的底层标志位 |
| 55 | `Input Color Space` | **输入色彩空间** | 告诉超分算法游戏送入缓冲区的色彩编码（线性或非线性） |
| 56 | `Intended for Performance/Balanced/Quality modes.\nAn older variant best suited to combat ghosting...\nRemoved on recent versions!` | **专为性能/平衡/质量模式设计。\n较早前用于对抗特定运动鬼影的变体...\n较新版本中已移除！** | DLSS Preset A 预设说明 |
| 57 | `Intended for Performance/Balanced/Quality modes.\nGenerally favors current frame information...\nRemoved on recent versions!` | **专为性能/平衡/质量模式设计。\n整体更偏重当前帧信息以减少运动滞后...\n较新版本中已移除！** | DLSS Preset C 预设说明 |
| 58 | `Intended for Ultra Performance mode.\nSimilar to Preset A...\nRemoved on recent versions!` | **专为超高性能模式设计。\n特性类似于预设 A...\n较新版本中已移除！** | DLSS Preset B 预设说明 |
| 59 | `KPSS` | **KPSS** | FSR4 神经网络模型代号（针对特定着色器管线优化） |
| 60 | `Kaiser2` | **Kaiser 2阶** | 基于贝塞尔窗的优质低通重采样滤波算法 |
| 61 | `Kaiser3` | **Kaiser 3阶** | 顶级重采样滤波器，高锐度且振铃抑制比 Lanczos3 更出色 |
| 62 | `Lanczos2` | **Lanczos 2阶** | 基于 sinc 窗函数的两步插值滤波，平衡锐度与性能 |
| 63 | `Lanczos3` | **Lanczos 3阶** | 经典 3 步 sinc 重采样插值，提供极高锐度 |
| 64 | `Latency & FPS` | **延迟与帧率** | 延迟优化（Reflex/Anti-Lag）与帧率上限管理选项卡 |
| 65 | `Latest` | **最新版本** | 指示使用驱动或模型库内包含的最高版本 |
| 66 | `Latest Transformer model\nMust use if DoF guide is needed` | **最新 Transformer 网络模型\n若需要景深(DoF)引导信息则必须使用此模型** | FSR4 最新神经网络特性说明 |
| 67 | `Latest supported by the dll` | **当前 DLL 支持的最高预设** | 让 OptiScaler 自动匹配 DLL 导出的最高预设版本 |
| 68 | `Lets you override each preset's ratio individually\nNote that not every game supports every quality preset\n\n1.5x on a 1080p screen means internal resolution of 720p\n1080 / 1.5 = 720` | **允许单独覆盖各画质挡位的内部缩放比例。\n注意并非所有游戏都支持全部画质预设。\n\n例如在 1080p 屏幕上设置 1.5x 意味着以 720p 渲染：\n1080 / 1.5 = 720** | 分挡位缩放比例自定义提示 |
| 69 | `Lighter and faster than Lanczos3.\nLess prone to ringing artefacts, but slightly blurrier.` | **比 Lanczos3 更轻量迅速。\n不易产生振铃边纹瑕疵，但锐度稍低。** | Lanczos2 滤波算法权衡说明 |
| 70 | `Likely doesn't do much` | **通常影响微弱** | 对某些在当前场景无明显视觉变化的调试参数标注 |
| 71 | `Linear (Default)` | **线性色彩 (默认)** | 标准线性空间颜色传递函数，绝大多数现代渲染管线默认 |
| 72 | `List of upscalers reported by FFX SDK` | **由 FFX SDK 探测报告的超分辨率算法列表** | 说明当前显卡和环境支持的 FidelityFX 超分列表 |
| 73 | `MAGIC` | **MAGIC** | 特殊着色器内部调试模式标识 |
| 74 | `MODEL_3` | **模型 3** | FSR4 神经网络候选模型编号 3 |
| 75 | `MODEL_4` | **模型 4** | FSR4 神经网络候选模型编号 4 |
| 76 | `MODEL_5` | **模型 5** | FSR4 神经网络候选模型编号 5 |
| 77 | `MODEL_6` | **模型 6** | FSR4 神经网络候选模型编号 6 |
| 78 | `Meant for development purpose to test if\nwriting a larger value to reactive mask, reduces ghosting.` | **面向开发调试，用于测试\n向响应遮罩写入更大数值能否减少鬼影拖尾。** | 响应遮罩调试说明 |
| 79 | `Min. Disocclusion Acc.` | **最小遮挡剔除累积量** | FSR3.1 发生遮挡剔除恢复时的保底时域权重 |
| 80 | `Motion` | **运动模式** | 偏向快速镜头运动清晰度的超分辨率预设组合 |
| 81 | `Network Models` | **神经网络模型** | AI 超分辨率（DLSS / FSR4）使用的推理网络模型选择 |
| 82 | `Non-Linear` | **非线性色彩** | gamma 矫正后的非线性色彩空间传递 |
| 83 | `Non-Linear PQ` | **非线性 PQ (HDR)** | 适用于 HDR 感知量化曲线（Perceptual Quantizer）的色彩空间 |
| 84 | `Non-Linear sRGB` | **非线性 sRGB** | 标准 sRGB gamma 曲线的色彩空间 |
| 85 | `Nvngx FG replacement` | **Nvngx FG 替换方案** | 拦截原生 nvngx.dll 的帧生成调用并重定向至目标方案 |
| 86 | `Off` | **关闭** | 开关或特性的关闭状态显示 |
| 87 | `Output Scaling` | **输出分辨率缩放** | 在超分之后对最终画面进行二次超采样或下采样的功能 |
| 88 | `Output Scaling is %s, Target Res: %dx%d (%.2f)\nJitter Count: %d` | **输出缩放为 %s，目标分辨率: %dx%d (%.2f)\n抖动采样计数: %d** | 输出分辨率与抗锯齿亚像素抖动状态显示 |
| 89 | `Override all` | **全局覆盖所有挡位** | 强制所有超分挡位使用统一定制的缩放比例 |
| 90 | `Override per quality preset` | **按画质挡位分别覆盖** | 分别自定义质量/平衡/性能等各个预设的独立缩放比例 |
| 91 | `Overrides every upscaler preset with the set value\n\n1.5x on a 1080p screen means an internal res of 720p\n1080 / 1.5 = 720` | **将所有超分挡位统一覆盖为当前设定的缩放比例。\n\n例如在 1080p 屏幕上设置 1.5x 相当于以 720p 内部渲染：\n1080 / 1.5 = 720** | 全局比例覆盖说明 |
| 92 | `PRESET A` | **预设 A** | NVIDIA DLSS 历史预设 A（抗鬼影变体） |
| 93 | `PRESET B` | **预设 B** | NVIDIA DLSS 历史预设 B（超高性能设计） |
| 94 | `PRESET C` | **预设 C** | NVIDIA DLSS 历史预设 C（偏重即时帧信息） |
| 95 | `PRESET D` | **预设 D** | NVIDIA DLSS 经典默认预设 D（极高时域稳定性） |
| 96 | `PRESET E` | **预设 E** | NVIDIA DLSS 3.7+ 改进预设 E（高细节抗拖尾） |
| 97 | `PRESET F` | **预设 F** | NVIDIA DLSS 超高性能与 DLAA 默认预设 F |
| 98 | `PRESET G` | **预设 G** | NVIDIA DLSS 保留预设 G |
| 99 | `PRESET H` | **预设 H** | NVIDIA DLSS 保留预设 H |
| 100 | `PRESET I` | **预设 I** | NVIDIA DLSS 保留预设 I |
| 101 | `PRESET J` | **预设 J** | NVIDIA DLSS 第一代 Transformer 架构预设 J |
| 102 | `PRESET K` | **预设 K** | NVIDIA DLSS 第一代 Transformer 架构预设 K |
| 103 | `PRESET L` | **预设 L** | NVIDIA DLSS Transformer 架构改良预设 L |
| 104 | `PRESET M` | **预设 M** | NVIDIA DLSS 第二代 Transformer 性能预设 M |
| 105 | `PRESET N` | **预设 N** | NVIDIA DLSS 第二代 Transformer 超高性能预设 N |
| 106 | `PRESET O` | **预设 O** | NVIDIA DLSS 最新预设 O |
| 107 | `Pattern` | **特征码匹配** | 通过扫描内存特征码识别游戏超分调用的匹配模式开关 |
| 108 | `Per shader GPU times` | **各着色器 GPU 耗时** | 展开显示每个特定着色阶段微秒级 GPU 执行时间的性能面板 |
| 109 | `Performance` | **性能** | 超分辨率性能挡位（渲染比率通常为 2.0x，大幅提高帧率） |
| 110 | `Please select %s as upscaler from game options and load a save game to enable Opti settings.\nUpscalers don't always work in menus.` | **请在游戏图形设置中将超分选择为 %s 并载入存档以启用 OptiScaler。\n超分辨率算法在游戏主菜单中通常不处于活动状态。** | 指导玩家进入 3D 渲染场景以激活超分挂钩 |
| 111 | `Preset 0` | **预设 0** | FSR 内部预设 0（原生抗锯齿档） |
| 112 | `Preset 1` | **预设 1** | FSR 内部预设 1（质量档） |
| 113 | `Preset 2` | **预设 2** | FSR 内部预设 2（平衡档） |
| 114 | `Preset 3` | **预设 3** | FSR 内部预设 3（性能档） |
| 115 | `Preset 4` | **预设 4** | FSR 内部预设 4（动态分辨率档） |
| 116 | `Preset 5` | **预设 5** | FSR 内部预设 5（超高性能档） |
| 117 | `Preset A\nRemoved on recent versions!` | **预设 A\n较新版本驱动中已移除！** | DLSS 历史预设 A 淘汰提示 |
| 118 | `Preset B\nRemoved on recent versions!` | **预设 B\n较新版本驱动中已移除！** | DLSS 历史预设 B 淘汰提示 |
| 119 | `Preset C\nRemoved on recent versions!` | **预设 C\n较新版本驱动中已移除！** | DLSS 历史预设 C 淘汰提示 |
| 120 | `Quality` | **质量** | 超分辨率质量挡位（缩放比约 1.5x，最接近原生画质） |
| 121 | `Ratio` | **缩放比例** | 超分辨率渲染分辨率与输出分辨率的比例系数 |
| 122 | `Reactive Scale` | **响应遮罩缩放** | 控制 FSR 动态响应遮罩强度的缩放倍率 |
| 123 | `Render Presets Override` | **渲染预设强制覆盖** | 强制替换游戏默认指定的 DLSS 内部神经网络预设 |
| 124 | `SPLAT` | **SPLAT** | FSR4 高性能神经渲染分支模型名称 |
| 125 | `Save Settings and restart the game for Enable and Pattern changes to apply` | **保存设置并重启游戏以使“启用”和“特征码”更改生效** | 修改底层 API 钩子配置后的重启生效提示 |
| 126 | `Select the input color space that the game uses.\nNon-Linear / sRGB: Might improve FSR4 upscaling quality, might increase ghosting.\nPQ: Rarest, might increase ghosting and break lights.` | **选择游戏所使用的输入色彩空间。\n非线性 / sRGB：可能提升 FSR4 重建画质，但也可能加重鬼影。\nPQ：最罕见，可能导致拖尾并在高光场景出现破损。** | 色彩空间兼容性与画面效果权衡提示 |
| 127 | `Shading Scale` | **着色变化响应比例** | FSR 3.1 内部光影时域变化的响应放大系数 |
| 128 | `Similar to Lanczos2.\nSmoother and less prone to artefacts than Lanczos, but slightly blurrier.` | **与 Lanczos2 类似。\n比 Lanczos 更柔滑平顺、瑕疵更少，但边缘稍显模糊。** | Kaiser2 滤镜对比说明 |
| 129 | `Similar to Lanczos3.\nFar less prone to artefacting than Lanczos3, but much heavier on the GPU.\nConsidered the best along with Lanczos3.` | **与 Lanczos3 类似。\n伪影显著少于 Lanczos3，但 GPU 计算开销更高。\n与 Lanczos3 并列为顶尖画质方案。** | Kaiser3 滤镜对比说明 |
| 130 | `Similar to preset K. Preset J might exhibit slightly\nless ghosting...\n1st Gen Transformer` | **与预设 K 类似。预设 J 表现出的运动鬼影可能稍少一些...\n第一代 Transformer 架构** | DLSS Preset J 预设对比说明 |
| 131 | `Specialised to prevent artifacts.\nEliminates harsh halos for a natural look, but can appear slightly soft.` | **专为消除伪影设计。\n可完全消除突兀的过度锐化光晕，观感更自然，但画面略显柔和。** | 高级无光晕抗伪影重采样滤波特性说明 |
| 132 | `Stability` | **稳定性模式** | 偏向画面静止或慢速移动时时域稳定抗闪烁的超分预设组合 |
| 133 | `Streamline FG Inputs` | **Streamline FG 帧生成输入** | 从 NVIDIA Streamline 框架拦截帧生成参数的输入模块 |
| 134 | `Take the upscaler inputs from this API` | **从此 API 抓取超分辨率输入参数** | 指定主要超分参数来源于哪一路图形 API 挂钩 |
| 135 | `Textures` | **纹理** | 纹理细节层级偏移与各向异性过滤选项卡 |
| 136 | `Theme and Color` | **界面主题与色彩** | 菜单外观主题与主色调设置卡片标题 |
| 137 | `This usually happens due to using tools\nsuch as Nvidia App or Nvidia Inspector` | **这通常是因为使用了诸如 Nvidia App 或 Nvidia Profile Inspector 等外部工具所致** | 诊断系统设置被第三方显卡工具锁死时的提示 |
| 138 | `Top left: Dilated Motion Vectors\nTop middle: Protected Areas\nTop right: Dilated Depth\nMiddle: Upscaled frame\nBottom left: Disocclusion mask\nBottom middle: Reactiveness\nBottom right: Detail Protection Takedown` | **左上: 膨胀运动矢量\n中上: 保护区域遮罩\n右上: 膨胀深度缓冲\n中间: 超分输出画面\n左下: 遮挡剔除遮罩\n中下: 响应遮罩\n右下: 细节保护抑制** | FSR 调试视图 9 宫格画面的各通道内容标注 |
| 139 | `Top left: Dilated Motion Vectors\nTop right: Predicted Blend Factor` | **左上: 膨胀运动矢量\n右上: 预测混合因子** | DLSS 调试视图各通道内容标注 |
| 140 | `Ultra Performance` | **超高性能** | 超分辨率超高性能挡位（缩放比通常为 3.0x，大幅牺牲分辨率换取最高流畅度） |
| 141 | `Ultra Quality` | **超级质量** | 超分辨率超级质量挡位（缩放比约 1.3x，仅轻微缩放，追求极致原生画质） |
| 142 | `Unused` | **未启用** | 当前未被占用的配置项或预留槽位 |
| 143 | `Upscale Ratio Override` | **超分缩放比例覆盖** | 打破游戏内固定的缩放挡位，自定义输入与输出比例 |
| 144 | `Upscaler Debug View` | **超分辨率调试视图** | 在屏幕上分块直观显示运动矢量、深度和遮罩等超分中间缓冲 |
| 145 | `Upscaler GPU time: %.2fms (avg: %.2fms)` | **超分辨率 GPU 耗时: %.2fms (平均: %.2fms)** | 超分辨率阶段实时渲染时间统计 |
| 146 | `Upscaler Inputs` | **超分辨率输入源** | 配置如何捕获游戏中提交给 DLSS/FSR/XeSS 的原生物理缓冲区 |
| 147 | `Upscalers` | **超分方案** | 主面板中配置当前使用何种超分辨率后端的卡片标题 |
| 148 | `Upscales the image internally to a higher output resolution\nthen downscales it back to your display resolution\n\nValues <1.0 make the upscaler cheaper\nValues >1.0 make image sharper at the cost of performance\n\nIf greyed out, please check Git Wiki - Unreal Engine tweaks\n\nTarget res and total ratio at the bottom (max. total 3.0!)` | **先在内部将画面超分重建到更高分辨率，\n再将其下采样回屏幕显示分辨率（DSR/动态超分辨率机制）。\n\n数值 <1.0 降低 GPU 负载提升流畅度\n数值 >1.0 显著提高锐度与清晰度但消耗性能\n\n若显示为灰色不可选，请查阅 Git Wiki 了解虚幻引擎修复技巧\n\n底部显示最终目标分辨率与总倍率（总倍率上限为 3.0！）** | 二次输出缩放与超分辨率下采样原理及性能提示 |
| 149 | `Upscaling` | **超分辨率** | 超分辨率主选项卡，负责核心画质重建与缩放算法设置 |
| 150 | `Use` | **使用** | 勾选以实际启用此接口捕获的数据 |
| 151 | `Use CopyResource for Inputs` | **对输入使用 CopyResource 拷贝** | 通过显卡直接内存复制隔离超分输入纹理，防止游戏异步覆写破坏数据 |
| 152 | `Use CopyResource for Output` | **对输出使用 CopyResource 拷贝** | 通过显卡直接内存复制隔离超分输出纹理，解决部分引擎直出黑屏闪烁 |
| 153 | `Use Generic App Id with DLSS` | **对 DLSS 使用通用应用 ID** | 向 NVNGX 传递统一的通用 Application ID |
| 154 | `Use generic appid with NGX\nFixes OptiScaler preset override not working with certain games\nRequires a game restart` | **向 NGX 传递通用应用 ID\n修复在某些游戏中 OptiScaler 无法成功覆盖 DLSS 预设的问题\n需要重启游戏生效** | 通用 App ID 绕过驱动白名单锁定的原理与提示 |
| 155 | `V-Sync` | **垂直同步** | 垂直同步开关与模式设置 |
| 156 | `Value of 0.0f can improve temporal stability of bright pixels\nLower values are more stable with ghosting\nHigher values are more pixelly, but less ghosting` | **设为 0.0 可改善高亮像素的时域稳定性\n较低数值抗鬼影表现更平稳\n较高数值颗粒感更明显，但能大幅抑制拖尾** | FSR3.1 速度敏感因子调优建议 |
| 157 | `Velocity Factor` | **速度敏感因子** | 控制像素运动速度对时域累积衰减影响的权重系数 |
| 158 | `Vulkan with Dx12 Settings` | **Vulkan 转 DX12 桥接设置** | 在 Vulkan 游戏中通过 DX12 中转设备使用 XeSS 等 DX12 专属超分算法 |
| 159 | `Watermark` | **水印标记** | 在游戏角落显示当前超分辨率算法的官方水印以验证注入成功 |
| 160 | `Whatever the game uses` | **遵从游戏原生设定** | 不改变游戏引擎自己指定的渲染预设或模型 |
| 161 | `XeSS Settings` | **XeSS 专属设置** | 针对 Intel XeSS 架构的专用画质与模型调优项 |
| 162 | `frames` | **帧数** | 输入用于调试或延迟测试的指定帧数计数量 |

## 模块 3：帧生成技术 (Frame Generation - DLSSG / FSR-FG / XeFG / OptiFG)（共 254 条）

| 序号 | 英文原文 (Source) | 中文翻译 (Target) | 翻译考量与术语依据 (Rationale) |
| :--- | :--- | :--- | :--- |
| 1 | `(%d)` | **(%d)** | 纯数字标记括号格式，保持原样 |
| 2 | `(Dynamic)` | **(动态倍率)** | 动态多帧生成（Dynamic Multi-Frame Generation, DMFG）运行状态指示 |
| 3 | `(Mode %u)` | **(模式 %u)** | 当前活动的特定运行模式编号 |
| 4 | `(Off)` | **(已关闭)** | 帧生成或特定子系统处于停用状态 |
| 5 | `(needs the parallax scale)` | **(需要视差比例参数)** | 重投影视差缓存生效前需先获得有效深度视差比例的提示 |
| 6 | `(no usable motion vectors)` | **(无可用运动矢量)** | 指示当前未捕获到有效的运动矢量缓冲区 |
| 7 | `1st person (%.2f, orbit %.2f)` | **第一人称 (%.2f, 环绕 %.2f)** | 重投影视角探测：第一人称视点与环绕视点判断数值 |
| 8 | `Accept First HUDless` | **仅采纳首个无 UI 候选** | 当着色器管线标记多个潜在的无界面缓冲区时，仅使用首个以防止冲突 |
| 9 | `Accept HUDless candidates of any format` | **允许任意像素格式的无 UI 候选** | 放宽对 HUDless 纹理表面格式（如 R11G11B10、RGBA16 等）的严格匹配过滤 |
| 10 | `Active DispatchFlags` | **当前生效调度标志位** | DirectX 12 调度参数中已激活的 DispatchFlags 调试卡片 |
| 11 | `Advanced FG Settings` | **帧生成高级设置** | 包含帧平滑步进、深度修复与资源拷贝的高级插帧参数 |
| 12 | `Advanced FSR FG Settings` | **FSR 帧生成高级设置** | 针对 AMD FidelityFX 帧生成管线的底层专有微调 |
| 13 | `Advanced OptiFG Settings` | **OptiFG 高级设置** | OptiScaler 原创的基于超分管线的通用插帧高级参数 |
| 14 | `Allow Async` | **允许异步计算** | 允许在独立异步计算队列（Async Compute Queue）执行帧生成着色器 |
| 15 | `Allows WaitForSingleObject instead of spinning for fence value` | **允许使用系统事件等待而非忙等待 CPU 自旋检测栅栏值** | 减轻 CPU 在等待 GPU 同步栅栏时的无谓空转占用 |
| 16 | `Allows pacing spinlock to sleep, should reduce CPU usage\nMight cause slow ramp up of FPS` | **允许帧平滑自旋锁在空闲时进入微休眠，可显著降低 CPU 占用\n但在帧率突变时可能导致 FPS 回升反应稍慢** | 平衡平滑锁 CPU 占用与帧率突变响应速度的权衡提示 |
| 17 | `Also limits FPS to the target and uses the lowest\nmultiplier that reaches it.` | **同时将帧率限制在目标值，并自动选用可达到该目标的最低插帧倍率。** | 动态插帧智能限制机制说明 |
| 18 | `Always Track Heaps` | **始终追踪描述符堆** | 强制全面捕获 Direct3D 描述符堆更新以防漏抓中间纹理 |
| 19 | `An active limit of 0 means auto-detect the display refresh rate` | **设为 0 表示自动检测当前显示器的物理刷新率作为限制上限** | 帧率限制器自动跟随显示器刷新率的说明 |
| 20 | `Apply Target` | **应用目标值** | 确认并应用设定的目标帧率数值 |
| 21 | `Apply Timing Changes` | **应用时序更改** | 应用帧平滑等待时长与自旋锁时序参数 |
| 22 | `Around target` | **围绕目标值波动** | 动态插帧倍率取舍策略：允许生成帧率在目标值上下轻微浮动 |
| 23 | `At least target` | **不低于目标值** | 动态插帧倍率取舍策略：倾向于向上取整，确保生成帧率高于或等于目标值 |
| 24 | `At most target` | **至多达到目标值** | 动态插帧倍率取舍策略：严格压低插帧倍率，确保不超出目标值 |
| 25 | `Block rarely used resources from using as HUDless \nto prevent flickers and other issues\n\nHUDfix enable/disable will reset the block list!` | **屏蔽极少使用的非核心资源被误识别为无 UI 画面，\n以防止屏幕闪烁或画面撕裂。\n\n开关 HUD 修复将会重置黑名单列表！** | 动态资源黑名单机制说明 |
| 26 | `Cache parallax scale` | **缓存视差缩放比例** | 重投影时镜头平移视差计算所使用的空间距离尺度缩放系数 |
| 27 | `Can be used with any FG Output\n\nRequires enabling DLSS-FG in game settings\nSupports HUDless out of the box\n\nLimited to games that use Streamline` | **可搭配任意帧生成输出后端使用\n\n需要在游戏画质设置中开启 DLSS 帧生成\n开箱即用原生支持无 UI 纯净画面\n\n仅限于使用了 NVIDIA Streamline 框架的游戏** | Streamline FG 输入源特性与适用范围说明 |
| 28 | `Can be used with any FG Output\n\nRequires enabling FSR-FG in game settings\nSupports HUDless out of the box` | **可搭配任意帧生成输出后端使用\n\n需要在游戏画质设置中开启 FSR 帧生成\n原生开箱即用支持无 UI 纯净画面** | FSR FG 输入源特性与适用范围说明 |
| 29 | `Can be used with any FG Output\n\nRequires enabling XeSS-FG in game settings\nSupports HUDless out of the box` | **可搭配任意帧生成输出后端使用\n\n需要在游戏画质设置中开启 XeSS 帧生成\n原生开箱即用支持无 UI 纯净画面** | XeSS FG 输入源特性与适用范围说明 |
| 30 | `Change FG` | **切换帧生成模式** | 立即重新初始化并切换到新选定的帧生成算法组合 |
| 31 | `Changes the multiplier on the fly to hit the target FPS,\nup to the Frame Gen setting (at 2X: FG on or off).` | **动态实时调节插帧倍率以契合目标帧率，\n最高上限为预设的插帧倍数（在 2X 模式下表现为自动启闭插帧）。** | 动态多帧生成（DMFG）调频逻辑说明 |
| 32 | `Common` | **通用** | 通用基础帧生成参数区域 |
| 33 | `Converts depth distances into the units of the camera position\nso the cache can follow the camera when you walk.\n0 = only follow rotation\nWrong values make the cache fill wobble while walking\nAlso used by the 3rd person detection\nUnreal Engine is usually around 1000` | **将深度距离转换为镜头坐标系单位，\n使重投影缓存能在玩家走动时跟随摄像机移动。\n0 = 仅跟随镜头旋转\n数值错误会导致走动时边缘补帧出现果冻晃动\n该值也用于第三人称视角检测\n虚幻引擎游戏通常在 1000 左右** | 重投影相机视差标定说明 |
| 34 | `Current DLSSG state:` | **当前 DLSSG 状态:** | 原生 DLSS 帧生成接口的运行时激活情况 |
| 35 | `Current FSR-FG state:` | **Current FSR-FG 状态:** | FSR 帧生成后端的运行时活动状态 |
| 36 | `Current Streamline FG state:` | **当前 Streamline FG 状态:** | NVIDIA Streamline 帧生成挂钩当前状态 |
| 37 | `Current XeFG state:` | **当前 XeFG 状态:** | Intel Xe 帧生成后端的运行时活动状态 |
| 38 | `Cutoffs transparency from UI to help with interpolation\nYou can use Show Detected UI to see the difference\n0.0 is auto` | **从 UI 层剔除半透明过渡边缘以辅助光流插帧\n可使用“显示检测到的 UI”直观查看差异\n0.0 为自动计算** | UI 半透明边缘截断说明 |
| 39 | `DE Ver: %d.%d.%d.%d   GB Ver: %d.%d` | **DLSS Enabler 版本: %d.%d.%d.%d   生成桥版本: %d.%d** | 外部帧生成组件 DLSS Enabler 的版本识别串 |
| 40 | `DLSSG Settings` | **DLSSG 专属设置** | NVIDIA DLSS 帧生成相关的专有参数与挂钩配置 |
| 41 | `DLSSG output\nCan be used in conjuction with Nukem's for example` | **DLSSG 输出目标\n可与 Nukem 的 dlssg-to-fsr3 等模组协同工作** | DLSSG 输出桥接特性说明 |
| 42 | `DLSSG via Nvngx` | **DLSSG (通过 Nvngx 拦截)** | 通过替换/拦截原生 nvngx.dll 实现的 DLSS 帧生成调用 |
| 43 | `DLSSG via Streamline` | **DLSSG (通过 Streamline 框架)** | 通过 NVIDIA Streamline 中间件接入的 DLSS 帧生成调用 |
| 44 | `DMFG FPS Target` | **动态多帧生成目标帧率** | Dynamic Multi-Frame Generation 动态调频所瞄准的目标帧率 |
| 45 | `Debug` | **调试** | 开启该模块内部专用调试功能 |
| 46 | `Debug Pacing Lines` | **绘制帧平滑调试线条** | 在画面底部绘制帧平滑步进时间线以分析卡顿波动 |
| 47 | `Debug Reset Lines` | **绘制重置信号指示线** | 在画面上直观标注由于镜头瞬间切换产生的帧生成重置信号 |
| 48 | `Debug Tear Lines` | **绘制撕裂监测参考线** | 在屏幕上可视化监测垂直同步未对齐时的画面撕裂位置 |
| 49 | `Delay HUDless capture, high values might cause crash!` | **延迟抓取无 UI 画面，过高数值可能导致崩溃！** | 调整抓取 HUDless 纹理的渲染管线延迟帧数 |
| 50 | `Depth as ValidNow` | **将深度图标记为即时有效** | 跳过深度纹理生命周期校验，在当前时序直接强制采纳 |
| 51 | `Depth cutoff` | **深度截断阈值** | 区分第一人称近景（如武器、双手）与远景画面的深度距离阈值 |
| 52 | `Depth values will be divided to this value` | **深度值将除以此数值进行归一化** | 将不同引擎各异的非线性深度范围规整到标准区间 |
| 53 | `Direction cache` | **方位角时域缓存** | 重投影在视线偏转时用于边缘补全的视角方向历史缓冲区 |
| 54 | `Disable DI Tracking` | **禁用 DrawIndexed 追踪** | 停止拦截 DrawIndexed 绘制指令以降低 CPU 挂钩开销 |
| 55 | `Disable DII Tracking` | **禁用 DrawIndexedInstanced 追踪** | 停止拦截 DrawIndexedInstanced 实例化绘制指令 |
| 56 | `Disable Dispatch Tracking` | **禁用 Dispatch 计算调度追踪** | 停止挂钩 Compute Shader 的 Dispatch 调度调用 |
| 57 | `Disable HUD/UI interpolation\nReverts back to previous XeFG 2 behaviour\n\nFixes artifacting transparent HUD/UI` | **禁用 UI / HUD 界面插帧\n恢复为上一代 XeFG 2 的处理机制\n\n可有效修复半透明 UI 边缘产生的拉伸伪影** | 避免文字与准星被插帧算法误当成 3D 运动画面的修复说明 |
| 58 | `Disable HUDFix Resource Tracking` | **禁用 HUD 修复资源追踪** | 彻底停止搜索 UI 纹理，节省多线程挂钩开销 |
| 59 | `Disable HUDless` | **禁用纯净画面捕获** | 强制不对无 UI 画面进行分离提取，直接全帧插帧 |
| 60 | `Disable HW Flip Metering` | **禁用硬件翻转度量** | 禁止驱动层硬件 Flip Metering 介入射频调步 |
| 61 | `Disable OM Tracking` | **禁用 OM 输出合并追踪** | 停止挂钩 OMSetRenderTargets 绑定操作 |
| 62 | `Disable RTV Tracking` | **禁用渲染目标视图(RTV)追踪** | 停止追踪 CreateRenderTargetView API 调用 |
| 63 | `Disable SCR Tracking` | **禁用计算根描述符表(SCR)追踪** | 停止追踪 SetComputeRootDescriptorTable 调用 |
| 64 | `Disable SGR Tracking` | **禁用图形根描述符表(SGR)追踪** | 停止追踪 SetGraphicsRootDescriptorTable 调用 |
| 65 | `Disable SRV Tracking` | **禁用着色器资源视图(SRV)追踪** | 停止追踪 CreateShaderResourceView 调用 |
| 66 | `Disable UAV Tracking` | **禁用无序访问视图(UAV)追踪** | 停止追踪 CreateUnorderedAccessView 调用 |
| 67 | `Disable UI texture` | **禁用 UI 独立纹理** | 忽略游戏提交的独立界面层纹理 |
| 68 | `Disable tracking of CreateRenderTargetView\nThis might help filtering of wrong HUDless resources` | **停止追踪 CreateRenderTargetView\n有助于排除被误判为 HUDless 纹理的无关渲染目标** | 过滤错误 UI 纹理的排查提示 |
| 69 | `Disable tracking of CreateShaderResourceView\nThis might help filtering of wrong HUDless resources` | **停止追踪 CreateShaderResourceView\n有助于排除被误判为 HUDless 纹理的无关着色器资源** | 过滤错误 UI 纹理的排查提示 |
| 70 | `Disable tracking of CreateUnorderedAccessView\nThis might help filtering of wrong HUDless resources` | **停止追踪 CreateUnorderedAccessView\n有助于排除被误判为 HUDless 纹理的无关 UAV 缓冲** | 过滤错误 UI 纹理的排查提示 |
| 71 | `Disable tracking of Dispatch\nThis might help filtering of wrong HUDless resources` | **停止追踪 Dispatch 调度\n有助于排除在计算着色器中被错误匹配的临时缓冲** | 过滤错误 UI 纹理的排查提示 |
| 72 | `Disable tracking of DrawIndexedInstanced\nThis might help filtering of wrong HUDless resources` | **停止追踪 DrawIndexedInstanced 实例化绘制调用** | 降低 CPU 钩子开销与纹理误判率 |
| 73 | `Disable tracking of DrawInstanced\nThis might help filtering of wrong HUDless resources` | **停止追踪 DrawInstanced 绘制调用** | 降低 CPU 钩子开销与纹理误判率 |
| 74 | `Disable tracking of OMSetRenderTargets\nThis might help filtering of wrong HUDless resources` | **停止追踪 OMSetRenderTargets 渲染目标绑定** | 排除多重渲染目标切换中的干扰表面 |
| 75 | `Disable tracking of SetComputeRootDescriptorTable\nThis might help filtering of wrong HUDless resources` | **停止追踪计算管线根描述符表绑定** | 针对计算着色器驱动 UI 的游戏优化 |
| 76 | `Disable tracking of SetGraphicsRootDescriptorTable\nThis might help filtering of wrong HUDless resources` | **停止追踪图形管线根描述符表绑定** | 针对常规图形绘制管线的轻量化过滤 |
| 77 | `Disables HUDFix resource tracking and\nreduces CPU overhead.\nUseful for MLFG which deals well with the HUD.\n\nAfter changing, please Save Settings and restart.` | **关闭 HUD 修复资源追踪以降低 CPU 额外开销。\n适用于自带优秀 UI 抗扭曲能力的机器学习插帧模型。\n\n修改后请保存设置并重启游戏。** | 关闭 HUD 追踪提升帧率的说明 |
| 78 | `Display only FSR 3.1 Generated frames` | **仅显示 FSR 3.1 生成的插帧画面** | 过滤掉真实物理渲染帧，仅屏幕上呈现生成的虚拟帧用于检视插帧瑕疵 |
| 79 | `Dithering` | **抖动混色** | 在重投影边缘使用抖动算法消除色带断层 |
| 80 | `Do not use HUDless set at ffxConfig` | **不使用在 ffxConfig 阶段设置的 HUDless 纹理** | 解决特定游戏在初始化阶段预填错误 HUDless 句柄的问题 |
| 81 | `Do not use HUDless set at ffxDispatch` | **不使用在 ffxDispatch 调度时传递的 HUDless 纹理** | 解决部分游戏在每帧调度时传入失效 HUDless 指针的问题 |
| 82 | `Don't use reset signals from FG Inputs` | **忽略来自帧生成输入源的重置信号** | 防止部分游戏因相机微小突变频繁重置插帧管线导致画面顿挫 |
| 83 | `Draw UI over` | **强制在最终画面上方覆映 UI** | 在完成帧生成画面后将 UI 图层强行复合在最顶层 |
| 84 | `Draws UI resource over the final image\nIf no UI visible, enable this!` | **将 UI 资源强制盖印在最终合成图像之上\n如果开启插帧后游戏所有界面消失不见，请务必启用此项！** | 解决界面被插帧底层吞噬的自救提示 |
| 85 | `Enable Async for better FG performance\nMight cause crashes, especially with HUD Fix!` | **开启异步计算队列以提升插帧性能\n在部分显卡或搭配 HUD 修复时可能引发崩溃！** | 异步插帧队列稳定性风险提示 |
| 86 | `Enable Debug View` | **开启调试视图** | 在画面中可视化展示光流矢量、深度与各类遮罩通道 |
| 87 | `Enable FSR3.1-FG Debug view\n\nTop left: Game Motion Vectors\nTop middle: GMV Depth\nTop right: Optical Flow MV\nMiddle: Interpolated frame only\nBottom left: Disocclusion mask\nBottom middle: Interpolation source (w/o UI)\nBottom right: HUDless resource` | **开启 FSR 3.1 帧生成调试视图\n\n左上: 游戏原生运动矢量\n中上: 深度缓冲\n右上: 光流运动矢量\n中间: 纯生成帧画面\n左下: 遮挡剔除遮罩\n中下: 插帧输入源(无UI)\n右下: 提取的 HUDless 纹理** | FSR 3.1 各分屏通道调试图例 |
| 88 | `Enable HUD stability fix, might cause crashes!` | **开启 HUD 稳定性修复，但在某些游戏可能引发崩溃！** | 防止 UI 元素在插帧时跟随 3D 背景扭曲形变的实验性修复 |
| 89 | `Enable Hybrid Spin` | **开启混合自旋锁平滑** | 结合线程睡眠与短时忙等的高精度混合帧间隔平滑调度 |
| 90 | `Enable Tuning` | **开启手动调优** | 解锁底层高阶参数滑块的手动控制权限 |
| 91 | `Enable WaitForSingleObjectOnFence` | **使用内核对象同步等待显卡栅栏** | 调用 Win32 原生同步事件等待 GPU 渲染完成 |
| 92 | `Enable Watermark` | **显示官方水印** | 在角落打上插帧技术的品牌水印验证接入状态 |
| 93 | `Enable XeFG Debug view` | **开启 XeFG 调试视图** | 可视化显示 Intel Xe 帧生成内部的匹配流与置信度 |
| 94 | `Enable reprojection` | **启用重投影抗延迟** | 利用最新鼠标物理采样数据在 GPU 端快速微调画面 |
| 95 | `Enables capturing of resources before shader execution.\nIncrease HUDless capture chances, but might cause capturing of unnecessary resources.` | **在着色器执行之前就提前捕获纹理资源。\n可提升捕捉到无 UI 纯净画面的成功率，但可能引入冗余资源消耗。** | 提前捕获阶段设置说明 |
| 96 | `Estimates the parallax scale from the game's motion vectors\nNeeds some walking around, until then the cache only follows rotation` | **通过分析游戏的运动矢量自动估算相机视差比例\n需要在游戏内走动几步以便算法学习，在此之前仅跟随视角旋转** | 动态视差自适应学习说明 |
| 97 | `Expands the cutoff area by this many depth pixels\nUse only when you see an outline left by the cutoff process` | **将深度截断区域向外扩展指定像素宽度\n仅当截断边缘出现明显的残余轮廓外描边时才需要调高** | 深度边缘轮廓消除说明 |
| 98 | `Extended` | **扩展模式** | 启用扩展的高级控制选项 |
| 99 | `Extended XeFG Settings` | **XeFG 扩展设置** | 针对 Intel Xe 架构插帧的深层定制选项 |
| 100 | `Extended format checks for possible HUDless\nMight cause crashes and slowdowns!` | **对潜在的无 UI 纹理放宽格式排查范围\n在某些引擎中可能导致卡顿或崩溃！** | 宽格式 HUDless 扫描提示 |
| 101 | `FFX + Enabler` | **FFX 与 Enabler 协同混合** | 首尾帧与中间帧交替采用不同引擎生成的混合多倍插帧方案 |
| 102 | `FFX FG` | **FFX 帧生成** | AMD 原生 FidelityFX 官方帧生成算法实现 |
| 103 | `FFX FG Version` | **FFX 帧生成核心版本** | 切换调用的 FSR 帧生成底层 DLL 版本（如 3.0 / 3.1 / 4.0） |
| 104 | `FFX for middle fake frames, and Enabler for the rest\n\n2x - FFX\n3x - Enabler\n4x - FFX + Enabler\n5x - Enabler\n6x - FFX + Enabler` | **中间插帧由 FFX 生成，其余由 DLSS Enabler 补齐\n\n2x - 纯 FFX\n3x - 纯 Enabler\n4x - FFX + Enabler\n5x - 纯 Enabler\n6x - FFX + Enabler** | 混合插帧在不同多倍插帧挡位下的执行引擎分配说明 |
| 105 | `FFX using the DLSSG swapchain` | **通过 DLSSG 交换链运行 FFX 帧生成** | 借助 NVIDIA 的低延迟交换链桥接驱动 AMD FSR 插帧 |
| 106 | `FG Create List` | **帧生成资源创建列表** | 记录插帧管线动态创建的专用纹理清单 |
| 107 | `FG Make Depth Copies` | **深度缓冲独立克隆** | 为插帧单独拷贝一份深度图，避免与后处理着色器产生资源锁死冲突 |
| 108 | `FG Make MV Copies` | **运动矢量独立克隆** | 为插帧单独拷贝一份速度场纹理，防止时序竞态条件损坏数据 |
| 109 | `FG Only Generated` | **纯插帧画面呈现** | 只向显示器输出生成的插值中间帧，用于排查瑕疵 |
| 110 | `FG Rectangle Settings` | **帧生成有效视口矩形** | 在存在上下黑边的带鱼屏或过场动画中手动划定有效插帧区域 |
| 111 | `FG Scale Depth Max` | **深度最大缩放比例** | 限制插帧深度映射的上限极值 |
| 112 | `FG Use List` | **当前使用的帧生成资源** | 当前正在参与光流或合成的显存纹理句柄列表 |
| 113 | `FG Use Mutex for Present` | **帧呈现互斥锁 (Present Mutex)** | 使用操作系统互斥锁串行化画面输出流程，防止多线程撕裂与卡死 |
| 114 | `FSR 3 FG` | **FSR 3 帧生成** | AMD FidelityFX Super Resolution 3 原生帧生成 |
| 115 | `FSR 3 MFG mod` | **FSR 3 多倍插帧模组** | 突破 2X 限制，实现 3X / 4X 多倍生成的 FSR3 修改版 |
| 116 | `FSR 3.0 FG` | **FSR 3.0 帧生成** | 早期第一代 FSR3 插帧技术 |
| 117 | `FSR 3.1 FG` | **FSR 3.1 帧生成** | 解耦超分管线、光流质量显著改善的官方 FSR3.1 插帧 |
| 118 | `FSR 3/4 FG` | **FSR 3/4 帧生成** | 支持升级到新一代 FSR4 架构的通用 AMD 插帧管线 |
| 119 | `FSR 3/4 FG using the FFX upgrade\n\nPartially based on Nukems, uses SL swapchain\nPossibly better performance and frame pacing compared to FSR-FG output` | **采用 FFX 升级特性的 FSR 3/4 帧生成\n\n部分基于 Nukem 架构并借由 Streamline 交换链驱动\n相较常规 FSR-FG 输出可获得更出色的流畅度与帧平滑度** | 全新 FFX-FG 输出后端的特性与优势 |
| 120 | `FSR FG` | **FSR 帧生成** | AMD FSR 帧生成技术统一名称 |
| 121 | `FSR FG Settings` | **FSR 帧生成设置** | FSR 插帧专有的时序、光流与平滑调度配置卡片 |
| 122 | `FSR3/4-FG, RDNA4 autoupgrades to FSR4-FG\n\nFSR4-FG sometimes better/worse than XeFG` | **FSR 3/4 帧生成，在 RDNA4 显卡上会自动升级为 FSR4-FG\n\nFSR4-FG 在不同游戏中表现与 XeFG 互有胜负** | FSR4 架构升级与适用性权衡 |
| 123 | `FT Input` | **输入帧时度量** | 直接采集游戏提交的原始基准帧生成时间 |
| 124 | `Fix broken visuals` | **修复画面渲染破损** | 修正部分 AMD 显卡驱动在特定 DX12 游戏中出现的纹理错乱 |
| 125 | `Fix for DLSS-D wrong depth inputs` | **修复 DLSS 光线重构(DLSS-D)错误的深度输入** | 纠正 DLSS 光线重建管线中传入的反向或缩放失真深度 |
| 126 | `Flip (Unity)` | **Unity 引擎轴向翻转** | 针对 Unity 引擎特有的 Y 轴或速度矢量反转进行专门适配 |
| 127 | `Flip Use Offset` | **翻转采样偏移量** | 在翻转纹理坐标时计入视口边缘偏移 |
| 128 | `Flip Velocity & Depth resources of Unity games` | **翻转 Unity 游戏的速度矢量与深度资源** | 修复 Unity 游戏中插帧严重拉丝、画面彻底崩溃的根本原因 |
| 129 | `Flip metering mode applied in the driver\nFSR only requests it in exclusive or borderless fullscreen` | **显卡驱动层应用的翻转度量模式\nFSR 仅在独占全屏或无边框窗口模式下请求启用该机制** | 驱动层硬件帧间隔调步说明 |
| 130 | `For fine tuning the depth cutoff\nShows UI and depth cutoff areas\nAdjust depth cutoff so that only stuff like your gun and hands are marked` | **用于精细校准近景深度截断阈值\n以高亮色彩直观标注当前被判定为近景的前景遮罩\n请微调数值，直到仅有手中的枪械和手臂等第一人称物件被彩色高亮覆盖** | 校准枪模近景深度遮罩的图文实操说明 |
| 131 | `For when the game sends HUDless, but you want to disable it` | **当游戏原生发送了纯净无 UI 画面，但你想强制禁用它时开启此项** | 排查原生 HUDless 产生瑕疵时的开关 |
| 132 | `For when the game sends a UI texture, but you want to disable it` | **当游戏原生发送了独立 UI 纹理，但你想强制禁用它时开启此项** | 排查原生独立 UI 图层误报时的开关 |
| 133 | `Force Borderless` | **强制无边框窗口化** | 强制将游戏全屏模式转换为无边框窗口以解决多项插帧兼容性 |
| 134 | `Force Dynamic MFG` | **强制开启动态多帧生成** | 强制启用动态多倍插帧以匹配显示器超高刷新率 |
| 135 | `Forces Borderless display mode\n\nFor best results, set fullscreen \nresolution to your display resolution\nMight cause some instability issues.\n\nNEEDS GAME RESTART TO BE ACTIVE!` | **强制启用无边框窗口化显示模式\n\n为达到最佳视觉效果，请确保全屏分辨率\n与你的物理显示器分辨率完全一致\n在极少数游戏中可能带来轻微不稳定。\n\n必须重启游戏方可生效！** | 强制无边框窗口模式的原理与重启提示 |
| 136 | `Frame Ahead` | **超前帧数** | 允许帧生成管线走在游戏逻辑渲染前面的最大帧数缓冲 |
| 137 | `Frame Generation` | **帧生成** | 通过光流网络在真实物理渲染帧之间插入生成帧以翻倍流畅度 |
| 138 | `Frame Generation (Enabler + FFX)` | **帧生成 (DLSS Enabler + FFX)** | 结合两种先进算法的协同多倍插帧模式 |
| 139 | `Frame Generation (FSR-FG Inputs)` | **帧生成 (FSR-FG 原生输入)** | 捕获游戏自身 FSR3 帧生成管线传入的数据作为插帧输入源 |
| 140 | `Frame Generation (FSR3-FG via Nukem's DLSSG)` | **帧生成 (Nukem dlssg-to-fsr3 桥接)** | 将游戏调用的 DLSSG 接口转译桥接至 FSR3 生成帧 |
| 141 | `Frame Generation (FSR3-MFG via DLSS Enabler)` | **帧生成 (DLSS Enabler 多倍插帧)** | 借助 DLSS Enabler 扩展实现 3X / 4X / 5X 多倍生成 |
| 142 | `Frame Generation (FSRFG via FFX)` | **帧生成 (FidelityFX 官方插帧)** | 调用 AMD 官方 FidelityFX 原生管线进行帧生成 |
| 143 | `Frame Generation (Streamline FG Inputs)` | **帧生成 (Streamline FG 框架输入)** | 从 NVIDIA Streamline 拦截并转换帧生成数据 |
| 144 | `Frame Pacing Tuning` | **帧平滑步进微调** | 调优两帧之间的显示间隔，杜绝由插帧引起的卡顿跳帧感 |
| 145 | `Frame generation rectangle, adjust for letterboxed content` | **帧生成裁剪矩形，用于在上下黑边（宽银幕电影比）场景下调整插帧范围** | 黑边过场动画防插帧撕裂设置 |
| 146 | `HUDFix` | **HUD 界面残影修复** | 消除 UI 文字、准星与血条在插帧时产生的拖影与闪烁 |
| 147 | `HUDless as ValidNow` | **将 HUDless 标记为即时有效** | 跳过时序同步，强制在当前上下文采纳无 UI 纯净画面 |
| 148 | `How long to spin if FPTHybridSpin is true. Measured in timer resolution units.\nNot recommended to go below 2. Will result in frequent overshoots` | **当启用混合自旋锁时的忙等轮询时长（以系统高精度定时器周期为单位）。\n不建议低于 2，过低将频繁发生调度超时导致掉帧卡顿。** | 帧平滑混合忙等超时参数说明 |
| 149 | `Hud Cutoff` | **HUD 深度截断** | 通过深度判定把第一人称视角前景强制作为 UI 图层保护 |
| 150 | `Hybrid Spin Time` | **混合自旋等待周期** | 帧平滑自旋锁进入忙等精确定时的时间片长度 |
| 151 | `If UI is too faint, disable this option` | **如果游戏界面图标颜色过淡或透明度异常，请关闭此选项** | 透明度色彩空间预乘校正提示 |
| 152 | `If source tags more than one HUDless, only use the first one` | **如果游戏标记了多个潜在的无 UI 纹理，则仅采纳首个标记** | 多缓冲区竞态筛选原则 |
| 153 | `If you are using an AMD/Intel GPU, then make sure you have Fakenvapi` | **如果你使用的是 AMD 或 Intel 显卡，请确保已正确部署 Fakenvapi 伪装环境** | 非 N 卡运行 DLSSG 必须的前置条件 |
| 154 | `If you are using an AMD/Intel GPU, then make sure you have fakenvapi` | **如果你使用的是 AMD 或 Intel 显卡，请确保已正确部署 Fakenvapi 伪装环境** | 非 N 卡运行 DLSSG 必须的前置条件（大小写变体） |
| 155 | `Ignore Init Checks` | **忽略初始化环境校验** | 绕过驱动或硬件特性支持预检，强制激活插帧管线 |
| 156 | `Ignores all prechecks for XeFG\nDon't use this option to skip MV size warning for UE games!\nIt might cause crashes and bad IQ!` | **跳过针对 Intel XeFG 的所有前置环境检查\n请勿用此选项在虚幻引擎游戏中跳过运动矢量尺寸警告！\n否则极可能引发程序崩溃并使画质严重劣化！** | 强制绕过检查的崩溃风险警告 |
| 157 | `Immediate Capture` | **即时捕获模式** | 不在调度尾部等待，在渲染指令触发的第一时间截取目标纹理 |
| 158 | `Input` | **输入源** | 当前使用的帧生成基础数据来源 |
| 159 | `Interpolated frames only` | **仅呈现插值虚拟帧** | 屏蔽原生真实帧，仅在屏幕显示插帧算法生成的画面 |
| 160 | `Late latch mouse` | **延迟锁存鼠标采样** | 在 GPU 真正开始执行重投影运算前一瞬间才锁存鼠标坐标，压降延迟 |
| 161 | `Let XeFG to handle frametimes` | **交由 XeFG 内部自行度量与调度帧间隔** | 允许 Intel 算法自带的平滑算法管理帧时序 |
| 162 | `Limit` | **帧率上限** | 当前设定的帧率限制极值 |
| 163 | `Limited to variants of FSR FG\n\nRequires enabling DLSS-FG in game settings\nSupports HUDless out of the box\nUses Streamline swapchain for pacing` | **仅限于各类 FSR 帧生成衍生方案\n\n需要在游戏画质设置中开启 DLSS 帧生成\n开箱即用完美支持无 UI 纯净画面\n通过 Streamline 交换链进行帧间隔调步平滑** | DLSSG 转 FSR-FG 架构特性说明 |
| 164 | `List of FGs reported by FFX SDK` | **FidelityFX SDK 探测到的可用帧生成技术列表** | 当前环境支持的 AMD 插帧管线类型列表 |
| 165 | `Make a copy of depth to use with OptiFG\nFor preventing corruptions that might happen` | **为 OptiFG 深度缓冲创建一份独立内存镜像\n以防止与引擎其他异步着色通道发生并发写冲突** | OptiFG 深度独立拷贝防撕裂说明 |
| 166 | `Make a copy of motion vectors to use with OptiFG\nFor preventing corruptions that might happen` | **为 OptiFG 运动矢量创建一份独立内存镜像\n以防止原始运动矢量在插帧完成前被后处理重写破坏** | OptiFG 运动矢量独立拷贝防撕裂说明 |
| 167 | `Makes a copy of the depth buffer\nCan fix broken visuals in some games on AMD GPUs under Windows\nCan cause stutters, so best to use only when necessary` | **在内存中创建一份深度缓冲区的独立拷贝\n可修复 Windows 系统下某些游戏在 AMD 显卡上出现的画面破损闪烁\n但会消耗显存带宽导致微小掉帧，建议仅在画面异常时开启** | 深度拷贝修复兼容性与性能代价说明 |
| 168 | `Might be required for some sets of DispatchFlags` | **当特定调度标志位组合激活时可能必须开启此项** | 调度标志关联提示 |
| 169 | `Needs HUDless texture to compare with final image.\nUI elements and ONLY UI elements should have a pink tint!` | **需要与最终画面比对以提取无 UI 纯净层。\n在调试画面中，应该有且仅有各类 UI 文字图标带有粉色高亮色调！** | HUDless 提取正确性验证指南 |
| 170 | `Noise` | **噪声抖动填充** | 重投影画面边缘填充时使用高频噪声扰动掩盖接缝 |
| 171 | `None` | **无 / 关闭** | 不启用任何插帧输入或输出 |
| 172 | `None (Real DLSSG)` | **无 (使用原生真实 DLSSG)** | 不进行任何转译，直接运行 NVIDIA 原生 DLSS 帧生成 |
| 173 | `Not updating camera rotation` | **未更新镜头旋转角** | 重投影因缺少有效姿态数据暂停了视线调整 |
| 174 | `Nukem's` | **Nukem 方案** | 由 Nukem 社区大神编写的著名 dlssg-to-fsr3 转译架构 |
| 175 | `Number of frames the FG is allowed to be ahead of the game\nMight prevent FG on/off switching, but also might cause issues` | **允许帧生成算法超前于游戏渲染的最大提前帧数\n可防止插帧在帧率临界点频繁启闭闪烁，但过高会引入操作延迟** | 超前帧数机制与负面效应说明 |
| 176 | `Opti` | **Opti 度量** | 使用 OptiScaler 自研算法计算出的精确帧生成时间 |
| 177 | `OptiFG (Upscaler)` | **OptiFG (基于超分辨率)** | OptiScaler 原创方案：从超分管线抓取运动矢量与深度进行通用插帧，兼容性极广 |
| 178 | `OptiFG Settings` | **OptiFG 专属设置** | OptiScaler 自研超分插帧方案的专有调优选项 |
| 179 | `Overrides the AMD hardware flip metering requested by FSR` | **覆盖由 FSR 请求的 AMD 显卡硬件底层翻转度量行为** | 解决部分 AMD 驱动帧率调步锁死 60 帧的问题 |
| 180 | `Pause in 3rd person` | **在第三人称视角时自动暂停** | 检测到第三人称越肩视角时暂停重投影，防止主角身体跟随准星扭曲 |
| 181 | `Please select DLSS Frame Generation in the game options\nYou might need to select DLSS first` | **请在游戏画面设置中开启“DLSS 帧生成”\n在部分游戏中可能需要先将超分切换为 DLSS 才能解锁该开关** | 引导玩家在游戏原生菜单中解锁插帧的提示 |
| 182 | `Please select FSR Frame Generation in the game options\nYou might need to select FSR first` | **请在游戏画面设置中开启“FSR 帧生成”\n在部分游戏中可能需要先将超分切换为 FSR 才能解锁该开关** | 引导玩家在游戏原生菜单中解锁插帧的提示 |
| 183 | `Presented FPS to aim for, never above the FPS limit.\nAuto: the FPS limit, or just under the refresh rate.` | **插帧后期望呈现的目标帧率，绝不会超出设定的帧率上限。\n自动：紧跟帧率限制值，或刚好保持在显示器物理刷新率稍下方。** | 目标输出帧率与动态防撕裂机制说明 |
| 184 | `Raw DispatchFlags:` | **原始调度标志位:** | 显示当前 DX12 调度底层十六进制标志位数值 |
| 185 | `Reads the mouse right when the GPU starts the reprojection\ninstead of when the frame is presented on the CPU.\nLowers latency, especially when GPU bound` | **在 GPU 即将开始重投影着色的一瞬间才读取最新鼠标坐标，\n而非在 CPU 呈现帧的早期阶段。\n可大幅压降输入延迟，在显卡满载瓶颈时效果尤为显著。** | 重投影极速鼠标采样抗延迟原理 |
| 186 | `Real DLSSG, For RTX 40xx and above` | **原生真实 DLSSG，适用于 RTX 40 系列及更高架构显卡** | 必须具备第 4 代 Tensor Core 与光流加速器的原生 N 卡方案 |
| 187 | `Rebuild the HUDless by removing the UI texture from the frame\nFSR-FG gets the UI only this way, DLSSG also takes the UI texture directly` | **通过从整幅画面中反向剔除 UI 纹理来重构无 UI 纯净画面\nFSR 帧生成仅支持此种方式剔除界面，而 DLSSG 亦可直接接收 UI 纹理** | UI 反向剔除与无 UI 纯净层重建原理 |
| 188 | `Rect Height` | **矩形高度** | 有效插帧视口区域的高度（像素） |
| 189 | `Rect Left` | **矩形左边距** | 有效插帧视口区域距离左侧边缘的横向偏移（像素） |
| 190 | `Rect Top` | **矩形顶边距** | 有效插帧视口区域距离顶部边缘的纵向偏移（像素） |
| 191 | `Rect Width` | **矩形宽度** | 有效插帧视口区域的宽度（像素） |
| 192 | `Rectangle Settings` | **插帧视口矩形设置** | 自定义插帧渲染画面的有效矩形边界范围 |
| 193 | `Relax resolution checks for HUDless by 32 pixels \nHelps games which use black borders for some \nresolutions and screen ratios (e.g. Witcher 3)` | **对无 UI 画面纹理的分辨率匹配放宽 32 像素容差\n有助于兼容在特定带鱼屏或宽高比下带有黑边填充的游戏（例如《巫师 3》）** | HUDless 分辨率容差机制说明 |
| 194 | `Relaxed Resource Check` | **放宽资源匹配校验** | 适度允许微小分辨率差异的纹理作为候选，改善兼容性 |
| 195 | `Remembers what was around the camera in previous frames\nand uses it to fill the screen edges and the area under your hands.\nEdge fill mode is only used where the cache has nothing.\nShown with a blue tint in debug mode` | **记录前几帧镜头周围的历史画面信息，\n用于补全视线快速转动时屏幕边缘暴露出未知空白区及手臂下方盲区。\n仅在历史缓存未覆盖的死角才会启用边缘拉伸补色。\n在调试模式中以蓝色调直观显示。** | 重投影全景环绕历史缓存与边缘填补机制 |
| 196 | `Reprojection (WIP)` | **画面重投影 (开发中)** | 利用传感器/鼠标瞬时移动数据在 GPU 呈现端校正视角的实验性超低延迟特性 |
| 197 | `Reprojection Settings` | **重投影设置** | 调优基于最新鼠标输入的瞬时视角微调与边缘填补参数 |
| 198 | `Reprojection would swing the character around with the camera,\nso it gets paused while something in the middle of the screen follows the camera.\nUses the game's motion vectors and the cache parallax scale.\nVehicle cockpits can count as 3rd person too.\nDisable to keep reprojection always active` | **在第三人称下重投影会导致主角身体随镜头旋转发生诡异撕扯，\n因此当检测到屏幕中央有物体固定跟随镜头时算法会自动休眠。\n载具座舱有时也会被视作第三人称。\n关闭此项可保持重投影强制常开。** | 第三人称视角智能休眠保护机制 |
| 199 | `Reprojects the game image using new mouse data\nKinda like Reflex 2, perceived latency improvement\n\n- REQUIRES DLSSG VIA STREAMLINE AS INPUT\n- Only works with first person perspective games\n- Only mouse, no controller\n- If possible, disable any mouse/camera smoothing in the game\n` | **使用最新的鼠标即时输入数据在渲染管线尾部重新投影游戏画面\n类似于下一代 Reflex 2 技术，带来肉眼可见的操作跟手度爆发式提升\n\n- 必须以“通过 Streamline 的 DLSSG”作为输入源\n- 目前仅适用于第一人称视角射击/动作游戏\n- 仅支持物理鼠标，暂不支持手柄摇杆\n- 建议在游戏内关闭任何鼠标平滑与相机滤波\n** | 重投影超低延迟技术全景指引与前置要求 |
| 200 | `Required for Debug flags to work correctly` | **调试标志位正常解析并生效所必需的前置依赖项** | 依赖说明 |
| 201 | `Requires Nukem's dlssg_to_fsr3 dll` | **需要系统中存在 Nukem 的 dlssg_to_fsr3.dll 组件** | 依赖文件缺失提示 |
| 202 | `Reset FG Rect` | **重置帧生成矩形** | 将插帧视口边界复位为屏幕全屏尺寸 |
| 203 | `Reset List` | **重置过滤列表** | 清空资源黑名单与误判过滤规则列表 |
| 204 | `Reset Target` | **重置目标帧率** | 将动态插帧的目标帧率复位为系统默认值 |
| 205 | `Resets Frame generation rectangle` | **重置帧生成有效矩形到默认全屏** | 操作提示 |
| 206 | `Resource Blocking` | **资源黑名单拦截** | 阻止非预期的显存纹理被插帧管线误采纳 |
| 207 | `Resource Settings` | **资源与管线设置** | 配置各种中间缓冲区的生命周期与拷贝行为 |
| 208 | `Safety Margins in ms` | **安全时间裕量 (毫秒)** | 在帧率平滑调度中为系统让出的微秒级安全缓冲时间 |
| 209 | `Safety margins in millisecons\nFSR default value: 0.1ms\nOpti default value: 0.01ms` | **以毫秒为单位的安全时间裕量\nFSR 官方默认值: 0.1ms\nOptiScaler 推荐优化值: 0.01ms** | 平衡输入延迟与突发掉帧撕裂的安全裕量提示 |
| 210 | `Scale Depth to fix DLSS RR` | **缩放深度以修复 DLSS 光线重构(RR)** | 将深度缓冲区尺度调整至符合 DLSS-RR 重构神经网络的预期范围 |
| 211 | `Select DLSS-FG in-game` | **在游戏画质选项中选择开启 DLSS 帧生成** | 游戏内设置指引 |
| 212 | `Select FSR-FG in-game` | **在游戏画质选项中选择开启 FSR 帧生成** | 游戏内设置指引 |
| 213 | `Select source for frametime\nMight help frame pacing and stutter issues` | **选择用于计算插帧间距的基准帧时间源\n有助于解决插帧后的微小卡顿与帧步进跳跃问题** | 帧间隔时钟源选择说明 |
| 214 | `Selects how many elements close to the camera\nshould be shown over the reprojected image.\nThis prevents your gun from being moved in weird ways.\n\nUse \"Show static elements\" to help you adjust it\nUnreal Engine games are usually around 0.10\nCyberpunk is around 0.02` | **选择在重投影画面上方保留多少贴近镜头的近景物体层。\n可防止你手中的枪械在快速转动时发生奇怪的错位形变。\n\n可借助“显示静态近景元素”高亮区域辅助校准\n虚幻引擎游戏通常推荐在 0.10 左右\n《赛博朋克 2077》推荐在 0.02 左右** | 第一人称武器近景保护深度调节实用技巧 |
| 215 | `Show Debug` | **显示调试信息** | 在屏幕上开启该模块的各项状态参数文本 |
| 216 | `Show Detected UI` | **高亮显示已检测到的 UI 区域** | 以明显彩色蒙版在屏幕上直观标出算法捕捉到的 UI 元素，便于检验界面是否被完整保留 |
| 217 | `Show static elements` | **高亮显示静态近景元素** | 以纯色蒙版显示当前被保护的手持枪械等近距离画面 |
| 218 | `Skip Config for HUDless` | **在 Config 配置阶段跳过 HUDless 绑定** | 防止某些驱动在管线装配期提前锁定不成熟的界面资源 |
| 219 | `Skip Dispatch for HUDless` | **在 Dispatch 调度阶段跳过 HUDless 处理** | 跳过计算着色器中的无 UI 分离过程 |
| 220 | `Skip Reset` | **忽略所有管线重置信号** | 无论游戏场景如何突变，始终强制维持帧生成连续运行 |
| 221 | `Soft edge` | **柔和边缘羽化填充** | 在重投影边缘出现视野死角时，对最外圈像素进行高斯模糊羽化平滑过渡 |
| 222 | `Soft edge and strech fill the screen edges with the edge pixels,\nsoft edge blurs them more the further out it goes\nDither and noise use the unprojected image as fill\nand then some blending on the edges to fool the eye` | **“柔化边缘”和“拉伸边缘”会使用画面边界像素来填补屏幕边缘空白，\n柔化边缘越靠近外侧模糊程度越高；\n“抖动”与“噪声”则取用未经重投影的原始画面作为基底，\n随后在接缝处进行视觉混色以欺骗人眼。** | 重投影快速甩枪时 4 种边缘补全模式的视觉算法解析 |
| 223 | `Strech edge` | **拉伸边缘填充** | 快速转动视角时向外单向延展边缘像素填充空隙 |
| 224 | `Syncing Settings` | **GPU 渲染同步设置** | 配置帧生成与游戏渲染线程之间的栅栏等待机制 |
| 225 | `The FG that you will actually be using` | **你最终实际在显卡上运行的真实帧生成底层算法** | 输出目标解释 |
| 226 | `The data source to be used for FG\nThe native FG which the game supports` | **供给帧生成管线使用的原始数据源\n通常对应于游戏原生支持并已在菜单开启的插帧类型** | 输入源解释 |
| 227 | `Tracking Settings` | **资源与钩子追踪设置** | 配置如何监测游戏对 DirectX 资源的创建和调度 |
| 228 | `Turns frame generation off when the game\nalone gets close enough to the target.` | **当游戏自身原生渲染帧率已经足够逼近目标值时，\n自动关闭帧生成以完全消除插帧产生的输入延迟与轻微伪影。** | 动态插帧智能省电与降延迟逻辑 |
| 229 | `UI Composition` | **UI 画面多层复合** | 在插帧输出后对原始界面进行二次高精度 Alpha 重新混合 |
| 230 | `UI Premult. alpha` | **UI 预乘 Alpha 通道** | 告知算法游戏 UI 纹理在送入时是否已经过透明度预乘运算 |
| 231 | `UI Texture` | **独立 UI 纹理** | 直接利用游戏引擎单独传递的纯透明界面纹理图层 |
| 232 | `Unblend UI` | **UI 反混色剔除运算** | 通过反向数学算法从已合成画面的像素中精确剔除 UI 颜色 |
| 233 | `Uncommon` | **特殊冷门选项** | 仅在少数特殊引擎或非常规黑客配置下才需用到的选项 |
| 234 | `Updated camera rotation by: %.1fms` | **相机旋转角补偿更新: %.1fms** | 重投影根据最新鼠标输入向前补偿的旋转时差 |
| 235 | `Upscaler is not active` | **超分辨率当前未处于活动状态** | 超分未工作因此无法为基于超分的插帧提供矢量 |
| 236 | `Upscaler must be enabled\n\nCan be used with any FG Output, but might be imperfect with some\nTo prevent UI glitching, HUDfix required` | **必须在游戏中开启超分辨率\n\n可与任意帧生成输出后端搭配，但在部分配置下可能不够完美\n为防止界面产生闪烁形变，强烈建议开启 HUD 修复** | 基于超分的 OptiFG 前置条件与防变形建议 |
| 237 | `Use Game's Reflex Markers` | **使用游戏原生的 Reflex 标记点** | 直接沿用游戏内部代码埋点的 Reflex 测量标记，获得最精准的平滑步进 |
| 238 | `Use height difference as offset` | **使用高度差作为采样偏移** | 在非标准宽高比下将视口高度差作为纹理偏移依据 |
| 239 | `Use if FSR4-FG is supported, otherwise stick to Enabler\n\nFFX used for the middle fake frame, Enabler for the rest\n\n2x - FFX\n3x - Enabler\n4x - FFX + Enabler\n5x - Enabler\n6x - FFX + Enabler\n\nDue to pacing, only odd number of fake frames are able to use FFX` | **如果显卡支持 FSR4-FG 则推荐使用，否则建议维持 Enabler\n\nFFX 用于生成正中央的一帧，其余虚拟帧由 Enabler 补齐\n\n2x - 纯 FFX\n3x - 纯 Enabler\n4x - FFX + Enabler\n5x - 纯 Enabler\n6x - FFX + Enabler\n\n受帧平滑机制制约，仅有奇数个生成帧才能启用 FFX 介入** | 高倍多帧生成混合引擎调度规律与建议 |
| 240 | `Use mutex to prevent desync of FG and crashes\nDisabling might improve the perf but decrease stability` | **使用互斥锁防止帧生成管线不同步与游戏偶发崩溃\n禁用此项可能轻微提高帧率，但会显著降低运行稳定性** | Present 互斥锁权衡提示 |
| 241 | `Use the UI texture the game blends on the frame in its last compute pass` | **使用游戏在最终计算通道中混合到画面上的界面纹理** | 针对计算着色器后处理合成界面的游戏 |
| 242 | `Uses frametimes calculated by Opti` | **使用 OptiScaler 自主计算的高精度帧生成时间** | 时钟源选项：Opti 自主计算 |
| 243 | `Variance Factor` | **方差敏感因子** | 控制帧间隔时间波动平滑算法对抗抖动的敏感度权重 |
| 244 | `Variance factor\nFSR default value: 0.1\nOpti default value: 0.3` | **帧平滑方差因子\nFSR 官方默认值: 0.1\nOptiScaler 推荐优化值: 0.3** | 方差因子推荐设置与说明 |
| 245 | `Velocity as ValidNow` | **将速度矢量标记为即时有效** | 跳过运动矢量生命周期校验，在当前管线立即采纳 |
| 246 | `What backend to use instead of the real DLSSG` | **选用哪种第三方先进算法来替代原生的 NVIDIA DLSSG** | 插帧替代方案选择说明 |
| 247 | `Where FPS may land, as multipliers only come in steps:\nat most, around or at least the target FPS.` | **由于插帧倍率仅能以整数倍（2X、3X、4X）为阶梯递进，\n在此选择最终生成帧率偏向于：至多达到、围绕波动、或至少达到目标 FPS。** | 动态多帧生成（DMFG）取整策略深入解析 |
| 248 | `Which copium do you choose?` | **你想选择哪款插帧方案？** | 带有极客自嘲幽默的插帧方案选择小提示 |
| 249 | `Will use more VRAM, but Uniscaler needs this\nMaybe some other games might need too` | **会占用稍多显存，但 Uniscaler 必须开启此项方可工作\n某些特殊游戏也可能需要此特性解决资源丢失** | Uniscaler 显存克隆依赖说明 |
| 250 | `Will use more VRAM, but some games might need this` | **会略微增加显存占用，但某些游戏必须开启此项方能正常渲染** | 显存资源克隆提示 |
| 251 | `XeFG` | **Intel XeFG 帧生成** | Intel XeSS 系列的高质量通用帧生成技术 |
| 252 | `XeFG - heaviest, but best universal FG\n\nXeFG 3 overall deals best with HUD\n\nEnable UI Composition if HUD ghosting` | **XeFG - 算力开销最高，但也是综合表现最出色的通用插帧方案\n\nXeFG 3 在应对各种复杂的 UI 界面时整体效果最佳\n\n若发现界面出现拖影，可配合开启“UI 画面多层复合”** | XeFG 全面特性解析与防伪影指南 |
| 253 | `XeFG Settings` | **XeFG 专属设置** | 针对 Intel XeFG 专有的时序、锐度与平滑微调卡片 |
| 254 | `Zero` | **归零 (由算法内部自主接管)** | 向插帧管线传递 0 帧时，完全由下游算法自主判断间隔 |

## 模块 4：低延迟与帧率管理 (Low Latency, Reflex, Anti-Lag, FPS Limiter)（共 49 条）

| 序号 | 英文原文 (Source) | 中文翻译 (Target) | 翻译考量与术语依据 (Rationale) |
| :--- | :--- | :--- | :--- |
| 1 | `Active input: %s` | **当前生效输入: %s** | 当前正在提供低延迟采样的输入接口 |
| 2 | `Active output: %s` | **当前生效输出: %s** | 当前正在执行低延迟调步的底层后端 |
| 3 | `Aggressive` | **激进模式** | 最积极压低渲染管线排队队列以换取极低延迟的调步策略 |
| 4 | `Allows XeLL to work without FG on non-Intel cards.\n\nDisables FG options\n\nRequires a restart` | **允许非 Intel 显卡在不开启帧生成的情况下单独使用 XeLL 低延迟。\n\n会禁用插帧选项\n\n需要重启游戏生效** | 独立运行 XeLL 降低输入延迟的说明 |
| 5 | `AntiLag Vk` | **Anti-Lag (Vulkan)** | 在 Vulkan 图形 API 下调用的 AMD 原生 Anti-Lag 低延迟管线 |
| 6 | `Apply Limit` | **应用限制** | 确认并应用设定的帧率上限值 |
| 7 | `Best when can be used, some games are not compatible (e.g. Cyberpunk)\nand will fallback to Aggressive` | **最理想的工作模式，但在极少数不兼容的游戏（如《赛博朋克 2077》）中\n会自动平稳回退至“激进模式”** | 最佳调步模式的兼容性回退提示 |
| 8 | `By default, FSR Anti-Lag 2.0/XeLL is used when available.\nThis setting lets you force LatencyFlex instead` | **默认情况下优先选用 FSR Anti-Lag 2.0 或 XeLL。\n此选项允许你强制改用通用的开源 LatencyFlex 方案** | 替换低延迟后端说明 |
| 9 | `Calculated Cap: %.1f` | **计算得出的帧率上限: %.1f** | 根据当前刷新率精准算出的防撕裂帧率上限 |
| 10 | `Conservative` | **保守模式** | 优先保证平稳帧率输出，轻度减少渲染排队的温和低延迟模式 |
| 11 | `Controls the DXGI Present sync interval, which determines how\nthe swap chain waits for vertical refresh.\n\n0  = Present immediately, no VSync wait.\n1  = Sync to every refresh, normal VSync.\n2+ = Present every N refreshes, reducing effective frame rate.\n\nHigher values can reduce tearing but may increase latency and cap FPS.\nFor most games, use 0 for lowest latency or 1 for normal VSync.` | **控制 DXGI Present 呈现同步间隔，决定交换链如何\n等待显示器的垂直刷新信号。\n\n0  = 立即呈现，不等待垂直同步（最低延迟，可能撕裂）。\n1  = 同步到每一次刷新，即标准垂直同步。\n2+ = 每隔 N 次垂直刷新才呈现一次画面，成倍压低帧率。\n\n较高数值可杜绝画面撕裂但会增加操作延迟并锁定帧率。\n绝大多数游戏建议选 0 以追求最低延迟，或选 1 保证画面平滑无撕裂。** | DXGI 垂直同步间隔参数原理与实用建议 |
| 12 | `Current method: %s` | **当前采用的方法: %s** | 当前生效的锐化或平滑计算方法 |
| 13 | `FPS Limit` | **帧率上限** | 设定游戏最高允许运行的 FPS 限制 |
| 14 | `FPS Limiter` | **帧率限制器** | 通过高精度 CPU/GPU 协同自旋锁将帧率锁定在指定数值 |
| 15 | `FSR Anti-Lag 2.0` | **FSR Anti-Lag 2.0** | AMD 新一代驱动级抗延迟技术，直接挂钩游戏主循环以消除排队 |
| 16 | `FSR Anti-Lag 2.0 is the new name for AntiLag 2\nDon't ask me why` | **FSR Anti-Lag 2.0 是 AMD 对 AntiLag 2 的官方重命名\n别问我为什么改名（官方任性）** | 幽默科普 AMD 品牌更名背景 |
| 17 | `Follow in-game` | **跟随游戏内置设定** | 遵从游戏自身设置菜单里的低延迟开关状态 |
| 18 | `Force Disable` | **强制禁用** | 无视游戏内部设定，强行彻底关闭该特性 |
| 19 | `Force Enable` | **强制开启** | 无视游戏内部设定，强行激活该特性 |
| 20 | `Force LatencyFlex` | **强制启用 LatencyFlex** | 强制接入不受显卡品牌限制的开源低延迟中间件 |
| 21 | `Force V-Sync On/Off & Sync Interval options` | **强制开闭垂直同步及同步间隔配置** | 覆盖游戏本身的 VSync 行为 |
| 22 | `Force XeLL` | **强制启用 Intel XeLL** | 强制调用 Intel Xe Low Latency 低延迟 SDK |
| 23 | `Force override the game's V-Sync settings.\n\nUseful for example when XeFG is locked to V-sync\nframe cap despite toggling Vsync off (e.g. Nioh 3)\n\nAfter changing, please Save Settings and restart.` | **强制覆盖游戏原本的垂直同步行为。\n\n非常适合用于修复诸如在《仁王 3》等游戏中，即便在游戏设置里关闭了垂直同步，\n开启 XeFG 依然会被死死锁在屏幕刷新率上限的顽疾。\n\n修改后请保存设置并重启游戏。** | 强制 V-Sync 覆盖解决顽固锁帧的说明 |
| 24 | `Framerate` | **帧率控制** | 管理帧率上限与防撕裂刷新率同步 |
| 25 | `Improves latency, but in some cases will lower FPS more than expected` | **可显著改善输入跟手度，但在某些场景下可能导致平均帧率下降略微超出预期** | 激进低延迟策略的性能权衡提示 |
| 26 | `Incompatible: %s` | **不兼容: %s** | 指示当前硬件或 API 与选定特性存在冲突 |
| 27 | `LatencyFlex` | **LatencyFlex** | 开源跨平台的通用 GPU 渲染队列等待压降方案 |
| 28 | `Low Latency` | **低延迟模式** | 通过动态拦截渲染循环消除 CPU 向 GPU 提交帧的排队等待 |
| 29 | `Only limits the FPS` | **仅限制帧率数值** | 不介入渲染步进调优，仅做硬性帧率截断 |
| 30 | `OptiScaler` | **OptiScaler 原生** | 使用 OptiScaler 自研内置的平滑与限制算法 |
| 31 | `Override Vsync` | **覆盖垂直同步设置** | 接管游戏交换链的 Present 标志以自由控制垂直同步 |
| 32 | `Reflex` | **NVIDIA Reflex** | NVIDIA 官方超低延迟 SDK |
| 33 | `Reflex ID` | **Reflex 实例标识** | 游戏代码内部标记的 Reflex 运行时对象编号 |
| 34 | `Refresh Rate` | **显示器刷新率** | 当前输出显示器的物理硬件垂直刷新频率（Hz） |
| 35 | `Reset Limit` | **重置帧率限制** | 将帧率限制恢复为无上限（0 / 自动） |
| 36 | `Save Settings and restart the game: XeFG keeps the low latency output it started with` | **保存设置并重启游戏：XeFG 将保持其启动时锁定的低延迟输出后端** | 切换延迟后端后的重启提示 |
| 37 | `Set as FPS Limit` | **设为当前帧率上限** | 将计算得出的防撕裂最佳帧率应用到限制器 |
| 38 | `Set by XeFG: the game's own keeps its XeLL` | **由 XeFG 自动管理：游戏自身保留专属的 XeLL 低延迟管线** | XeFG 内部托管低延迟状态 |
| 39 | `Set by XeFG: the game's own keeps its XeLL (only the FPS limit is OptiScaler's)` | **由 XeFG 自动管理：游戏保留自带的 XeLL（仅帧率上限由 OptiScaler 接管）** | 混合模式状态说明 |
| 40 | `Sync Int.` | **同步间隔** | DXGI 垂直同步间隔步进（0: 关, 1: 逐帧对齐, 2: 半帧率同步） |
| 41 | `The safest, but might not reduce latency well` | **运行最稳定安全，但降低延迟的幅度相对温和有限** | 保守调步模式的特性 |
| 42 | `UeLowLatency` | **虚幻引擎低延迟** | 虚幻引擎原生内置的输入延迟压降机制 |
| 43 | `Uses Reflex when possible\nOn AMD/Intel cards, you can use Fakenvapi to substitute Reflex` | **在支持的环境下优先调用 Reflex\n在 AMD / Intel 显卡上，可配合 Fakenvapi 伪装环境将 Reflex 转译调用** | A/I 卡使用 Reflex 转译的原理提示 |
| 44 | `V-Sync Off` | **垂直同步：关闭** | 关闭垂直同步，允许画面自由超频渲染（可能出现水平撕裂） |
| 45 | `V-Sync On` | **垂直同步：开启** | 开启垂直同步，将输出帧与显示器硬件扫描严格同步 |
| 46 | `V-Sync Settings` | **垂直同步设置** | 配置画面垂直刷新同步模式与步进间隔 |
| 47 | `VRR Frame Cap Calculator` | **可变刷新率(VRR)最佳防撕裂帧率计算器** | 为 G-Sync / FreeSync 用户计算刚好处于可变刷新率窗口上限内、永不产生撕裂且无传统垂直同步高延迟的最佳锁帧上限（通常为刷新率减 3~4 帧） |
| 48 | `XeLL` | **Intel XeLL** | Intel Xe Low Latency 超低延迟技术 |
| 49 | `fakenvapi` | **FakeNvapi 伪装** | 模拟 NVIDIA 专有 Nvapi 驱动接口的兼容层 |

## 模块 5：图像锐化、纹理与画质过滤 (Sharpening, Mipmap Bias, Anisotropy, Magnifier)（共 74 条）

| 序号 | 英文原文 (Source) | 中文翻译 (Target) | 翻译考量与术语依据 (Rationale) |
| :--- | :--- | :--- | :--- |
| 1 | `(Current: %.3f)` | **(当前值: %.3f)** | 指示当前实际生效的浮点参数数值 |
| 2 | `(Current: disabled)` | **(当前状态: 已禁用)** | 指示特定纹理覆盖处于未激活状态 |
| 3 | `(Currently following cursor)` | **(当前跟随鼠标指针)** | 放大镜调试窗口正跟随光标移动 |
| 4 | `Advanced DA Parameters` | **深度感知(DA)锐化高级参数** | 深度感知智能边缘锐化的高阶控制滑块 |
| 5 | `Anisotropic Filtering` | **各向异性过滤** | 大幅提升斜向视线远处地表与墙面纹理清晰度的材质采样技术 |
| 6 | `Apply override value as scale multiplier\nWhen using scale mode, please use positive\noverride values to increase sharpness!` | **将覆盖值作为等比缩放倍率应用\n在使用倍率模式时，请使用正数覆盖值来增加锐度！** | 锐化倍率模式调节指引 |
| 7 | `Apply same override value to all textures` | **对所有类型的纹理强制统一应用相同的 Mipmap 偏移覆盖** | 全局纹理清晰度统一覆盖开关 |
| 8 | `Areas that are more red will have more sharpness applied\nGreen areas will get reduced sharpness` | **偏红色的区域将获得更高强度的锐化处理，\n偏绿色的区域将降低锐化强度以防噪点滋生。** | 调试热力图色彩含义说明 |
| 9 | `Border Size` | **边框粗细** | 放大镜窗口边框的像素宽度 |
| 10 | `Calculate Mipmap Bias` | **自动计算理论最佳 Mipmap 偏移** | 根据当前超分缩放比例通过对数公式（log2(渲染/显示)）自动算出最契合的负偏移量 |
| 11 | `Can help with blurry textures in broken games\nNegative values will make textures sharper\nPositive values will make textures more blurry\n\nHas a small performance impact` | **可修复部分游戏在使用超分后远处地面纹理模糊发虚的通病。\n负值会让贴图纹理更清晰锐利，\n正值会让贴图更加柔和模糊。\n\n对显卡性能影响极小。** | Mipmap 偏移原理与调谐技巧指南 |
| 12 | `Clamp Output` | **输出色域截断限制 (0~1)** | 将着色器最终输出像素的色彩值严格限制在标准 [0, 1] 动态区间内 |
| 13 | `Clamps the final image to the [0, 1] range.\n\nPrevents overshoot artifacts such as bright halos or negative colors.\nRecommended for LDR pipelines; optional for HDR depending on tone-mapping.\n\nWhen not set OptiScaler controls it via upscalers HDR flag` | **将合成后的最终画面色彩强制钳位在 [0, 1] 标准区间。\n\n可有效消除锐化算法产生的过度过冲白色亮边或负色反常伪影。\n强烈建议在标准动态范围(SDR)下开启；HDR 模式下视色调映射而定。\n\n未手动指定时，OptiScaler 将根据超分辨率的 HDR 标志位自动接管。** | 防白边与过冲伪影的色域钳位机制解析 |
| 14 | `Contrast` | **局部对比度抑制** | 根据像素邻域对比度动态抑制过度锐化 |
| 15 | `Contrast Enabled` | **开启对比度自适应** | 允许算法感知局部明暗对比度动态调整滤波权重 |
| 16 | `Controls how strongly sharpening is reduced across depth edges.\n\nHigher values more aggressively prevent sharpening across object boundaries (reduces halos).\nLower values allow more sharpening to pass across edges (sharper but riskier).` | **控制在深度突变边缘（物体与背景分界线）处降低锐化强度的剧烈程度。\n\n较高数值会更强力地抑制物体轮廓边缘的锐化，极大减少亮白光晕；\n较低数值允许锐化穿透物体边缘，画面更锐利但更容易出现白边。** | 深度锐化边缘抑制机制说明 |
| 17 | `Controls sharpness at high contrast areas.` | **控制在明暗强烈对比区域（如灯光、窗框）的局部锐化强度。** | 高对比度防过冲控制说明 |
| 18 | `Current : %.3f / %.3f` | **当前值 : %.3f / %.3f** | 当前参数与对照参数双值显示 |
| 19 | `Current : %.3f / %.3f, Target: %.3f` | **当前值 : %.3f / %.3f，目标值: %.3f** | 当前参数与目标设定值 |
| 20 | `Current : %.3f / %.3f, Target: Base * %.3f` | **当前值 : %.3f / %.3f，目标值: 基准 * %.3f** | 基准倍率运算显示 |
| 21 | `Current : %.3f / %.3f, Target: Base + %.3f` | **当前值 : %.3f / %.3f，目标值: 基准 + %.3f** | 基准增量运算显示 |
| 22 | `Cursor Offset X` | **光标水平偏移 X** | 放大镜窗口相对于鼠标物理光标的横向像素距离 |
| 23 | `Cursor Offset Y` | **光标垂直偏移 Y** | 放大镜窗口相对于鼠标物理光标的纵向像素距离 |
| 24 | `DA + MAS Debug` | **深度感知 + 运动自适应双调试视图** | 同屏同时展示深度边缘热力图与运动自适应锐化遮罩 |
| 25 | `Defines the motion range over which the effect ramps from zero to full strength.\n\nValues above the threshold are mapped into this range.\nLarger values make the response smoother and more gradual.\nSmaller values make the effect react more quickly and aggressively.` | **定义动态锐化从零强度平滑爬升到全开强度的运动速度动态区间。\n\n超出阈值的运动矢量将被映射到该区间内。\n较大数值使过渡更丝滑自然；\n较小数值使锐化对细微动作的反应更迅猛激进。** | 动态运动自适应过渡区间参数详解 |
| 26 | `Depth Aware (DAS)` | **深度感知锐化 (DAS)** | 基于原生深度缓冲识别三维物体轮廓的智能低瑕疵防白边锐化 |
| 27 | `Depth Aware (RCAS)` | **深度感知 RCAS** | 结合了 AMD 鲁棒对比度感知与三维深度几何边缘保护的顶级混合锐化 |
| 28 | `Depth Bias` | **深度容差阈值** | 在做边缘检测前忽略过小的深度微弱起伏，避免粗糙材质表面产生噪点 |
| 29 | `Depth Scale` | **深度缩放倍率** | 控制跨越不同物体的深度边界识别反差敏锐度 |
| 30 | `Enable DA + MAS debug views\nBlue tint for DA detected edges\n\nMore red areas will have more sharpness applied\nGreen areas will get reduced sharpness` | **开启深度感知与运动自适应调试复合视图\n蓝色高亮代表检测到的三维物体几何轮廓边缘\n\n红色区域代表被算法强化锐化的静态高细节区\n绿色区域代表因镜头快速转动而被主动抑制锐化的运动防噪区** | 锐化调试视图书签色彩解析 |
| 31 | `Enable Magnifier` | **启用放大镜工具** | 在屏幕上开启高倍率局部像素放大监视窗，用于像素级对齐与抗锯齿画质鉴赏 |
| 32 | `Enable Motion Adaptive Sharpness` | **启用运动自适应动态锐化 (MAS)** | 静止时保持极致锐度，镜头剧烈运动时自动降低锐化以消除闪烁噪点 |
| 33 | `Enables sharpness adjustments according to the motion` | **根据画面的即时运动速度动态实时增减锐化强度** | 运动自适应动态锐化开关 |
| 34 | `Force Anisotropic Filtering` | **强制覆盖各向异性过滤 (AF)** | 无视游戏内部低等级设定，强制显卡执行高达 16x 的全开各向异性采样 |
| 35 | `Ignores small depth differences before edge detection.\n\nHigher values reduce flickering and noise from minor depth changes, but may soften real geometry edges.\nLower values preserve fine detail but can cause unstable or noisy edge detection.` | **在执行轮廓识别前忽略微小的深度起伏。\n\n较高数值可减少起伏表面上的噪点闪烁，但可能轻度软化真实几何边缘；\n较低数值完整保留细微几何反差，但可能导致复杂纹理表面产生颗粒噪点。** | 深度容差平衡取舍指南 |
| 36 | `Ignores the value sent by the game\nand uses the value set below` | **强制忽略游戏引擎提交的默认数值，\n改用下方手动自定义的参数配置** | 强制接管参数开关提示 |
| 37 | `MAS Debug` | **运动自适应锐化(MAS)调试视图** | 用色彩直观高亮屏幕各个局部的动态运动强度 |
| 38 | `MB Fixed Override` | **Mipmap 固定绝对值覆盖** | 强制将所有材质的采样偏移锁定为指定固定绝对数值 |
| 39 | `MB Override All Textures` | **Mipmap 覆盖全部纹理** | 打破常规限制，无差别覆盖所有三维材质的细节层级 |
| 40 | `MB Scale Override` | **Mipmap 比例倍乘覆盖** | 在游戏原有 Mipmap 偏移基础上乘以设定的倍率系数 |
| 41 | `Magnifier` | **画质放大镜** | 在游戏内弹窗实时局部无损放大像素的调试工具卡片 |
| 42 | `Maximum amount of sharpness that motion can add or remove.\n\nNegative values reduce sharpening in motion (recommended).\nPositive values increase sharpening in motion.\n\nThe final adjustment scales with motion and is capped at this value.` | **运动状态下允许调整的最大锐度极值。\n\n负数：镜头转动时主动降低锐度（强烈推荐，可消灭运动噪点）；\n正数：镜头转动时进一步激进加锐；\n\n最终调节量随速度动态线性插值，最高不会突破该绝对值上限。** | 运动锐度极值调校技巧 |
| 43 | `Method` | **锐化计算方法** | 切换所使用的锐化滤镜数学内核算法 |
| 44 | `Minimum motion required before motion-based sharpening adjustment begins.\n\nHigher values ignore small movements (more stable).\nLower values react to subtle motion (more sensitive).` | **触发运动锐度调节所需的最低运动速度门槛。\n\n较高数值会忽略角色的细微呼吸晃动（更加沉稳）；\n较低数值对哪怕轻微的视线转动都能迅速响应。** | 动态锐化动作死区门槛说明 |
| 45 | `Mipmap Bias` | **纹理细节层级偏移 (Mipmap Bias)** | 调整距离摄影机不同远近的材质贴图清晰度层级，负值可使远景纹理更清晰锐利 |
| 46 | `Modify Compare` | **拦截修改比较采样器** | 将各向异性过滤应用范围扩展至阴影与比较类型的纹理采样器 |
| 47 | `Modify Min/Max` | **拦截修改最小/最大值采样器** | 将各向异性过滤扩展至特殊极值重采样阶段 |
| 48 | `MotionRange` | **动态响应平滑区间** | 速度越过阈值后从静止过渡到全开状态的过渡速度跨度 |
| 49 | `MotionSharpness` | **动态锐度调节极值** | 在最高速运动状态下所允许削减或追加的锐度上限 |
| 50 | `MotionThreshod` | **运动触发门槛阈值** | 画面运动速度必须超过此数值才开始动态改变锐化 |
| 51 | `Override` | **强制覆盖** | 启用手动自定义数值以替换原生参数 |
| 52 | `Override all textures mipmap values\nNormally OptiScaler only overrides\nbelow zero mipmap values!` | **强制覆盖所有纹理的 Mipmap 数值\n常规情况下 OptiScaler 仅安全覆盖负偏移区域的采样器！** | 强制全量贴图覆盖的适用场景与安全说明 |
| 53 | `Positioning` | **定位模式** | 选择放大镜窗口在屏幕上的固定坐标或鼠标吸附 |
| 54 | `Positive values decrease sharpness at high contrast areas.\nNegative values increase sharpness at high contrast areas.` | **正数：在明暗强烈边缘主动压低锐化以防刺眼白边。\n负数：在明暗边缘进一步强调锐化让线条更加突出刺眼。** | 局部对比度防光晕正负极性调节指南 |
| 55 | `RCAS` | **RCAS 鲁棒对比度自适应锐化** | AMD 官方的高性能对比度自适应锐化算法，在大幅提锐的同时几乎不破坏画面阶调 |
| 56 | `Reset` | **重置** | 将当前模块参数恢复为默认预设 |
| 57 | `Reset Depth Values` | **重置深度参数** | 将深度截断、容差与缩放恢复为标准安全默认值 |
| 58 | `Reset Static Position (Follow Cursor)` | **重置为鼠标跟随模式** | 取消屏幕绝对坐标吸附，恢复让放大镜紧随鼠标指针移动 |
| 59 | `Select the sharpening filter to apply.\n\nUpscaler's default: Uses the sharpening provided by the upscaler.\nRCAS: AMD's RCAS, modified for Contrast and MAS.\nDepth Aware: Smarter sharpening with fewer artifacts (heavier).\n\nBy default uses a sharpening value provided by the game.\nSelect 'Override' under 'Sharpness' and adjust the slider to change it.` | **选择要应用的图像锐化算法内核。\n\n超分辨率默认：直接使用超分算法自带的默认锐化通道；\nRCAS：AMD 官方经典的鲁棒对比度自适应锐化，支持扩展对比度与运动感知；\n深度感知(DA)：利用三维深度几何体智能规避白边伪影的顶级锐化方案（算力开销较高）。\n\n默认状态下沿用游戏自身在画质菜单里下发的锐化强度；\n若要手动微调，请在“锐化强度”下方勾选“强制覆盖”后拖动滑块自定义。** | 多款锐化滤镜工作原理与自定义调谐详尽指导 |
| 60 | `Set` | **设定** | 确认当前手动指定的数值 |
| 61 | `Set Static Position` | **固定当前屏幕坐标** | 将放大镜窗口永久锚定在当前显示的屏幕位置，不再跟随鼠标游走 |
| 62 | `Sharpness` | **图像锐度** | 控制整个渲染画面的整体边缘清晰度与反差 |
| 63 | `Size` | **视窗尺寸** | 放大镜窗口的物理正方形长宽像素大小 |
| 64 | `Skip Point Filters` | **跳过近邻点采样器** | 对像素点采样滤波类型不进行各向异性过滤强制提升，防止破坏复古游戏像素感 |
| 65 | `Skip updating of point filters` | **不对点采样滤镜应用各向异性过滤更新** | 保留特定点阵图的原汁原味 |
| 66 | `Static Pos X` | **固定横坐标 X** | 放大镜锚定在屏幕上的绝对水平像素位置 |
| 67 | `Static Pos Y` | **固定纵坐标 Y** | 放大镜锚定在屏幕上的绝对垂直像素位置 |
| 68 | `Strength` | **锐化强度** | 锐化滤镜的总体混合权重滑块 |
| 69 | `Update comparison filters` | **拦截更新比较采样器** | 强制向阴影贴图深度比对阶段注入各向异性过滤参数 |
| 70 | `Update min/max filters` | **拦截更新极值采样器** | 强制向极值采样阶段注入各向异性过滤参数 |
| 71 | `Upscaler's default` | **超分辨率默认锐化** | 直接使用 DLSS/FSR/XeSS 算法自带的锐化通路 |
| 72 | `Will be applied after RESOLUTION/PRESET change !!!` | **将在下次切换分辨率或画质预设后正式生效！！！** | 全局 Mipmap 链重建时机说明 |
| 73 | `Will might be applied after RESOLUTION/PRESET change !!!` | **可能需要在切换分辨率或画质预设后方可完整生效！！！** | 全局 Mipmap 链重建时机说明（带可能字样） |
| 74 | `Zoom Factor` | **放大倍率** | 放大镜内部画面的像素级放大倍数（如 2x, 4x, 8x） |

## 模块 6：兼容性、伪装与底层挂钩 (Compatibility, Spoofing, Hooks, Plugins)（共 39 条）

| 序号 | 英文原文 (Source) | 中文翻译 (Target) | 翻译考量与术语依据 (Rationale) |
| :--- | :--- | :--- | :--- |
| 1 | `Allows the use of a Reactive mask\nKeep in mind that a Reactive mask sent to DLSS\nwill not produce a good image in combination with FSR/XeSS` | **允许使用动态响应遮罩(Reactive Mask)\n注意直接为 DLSS 生成的响应遮罩，\n如果强行传递给 FSR/XeSS 有时可能导致画面瑕疵或闪烁** | 响应遮罩跨算法兼容性提醒 |
| 2 | `Auto Exposure` | **自动曝光计算** | 指示超分算法根据画面亮度直方图自主计算测光曝光参数 |
| 3 | `Check for Update` | **自动检查新版本** | 在启动时连线 GitHub 检查 OptiScaler 是否发布了新版 |
| 4 | `DRS Override Maximum` | **强制覆盖动态分辨率(DRS)最大缩放上限** | 锁定动态分辨率调节范围的最大缩放极值 |
| 5 | `DRS Override Minimum` | **强制覆盖动态分辨率(DRS)最小缩放下限** | 锁定动态分辨率调节范围的最小缩放底限 |
| 6 | `DXGI Spoofing` | **DXGI 显卡伪装** | 在系统 DXGI 层面将当前显卡型号伪装为 NVIDIA RTX 显卡，从而在任意显卡上解锁游戏菜单中的 DLSS / DLSS-FG 灰显开关 |
| 7 | `Depth Inverted` | **反向深度缓冲 (Inverted Depth)** | 告知超分算法游戏使用了现代游戏常用的浮点反向深度管线（近处 1.0，远处 0.0） |
| 8 | `Disable Overlays` | **禁用可能冲突的外部叠加层** | 在呈现链路上屏蔽 RTSS、Steam 等外部三方 OSD，避免画面闪烁或崩溃 |
| 9 | `Disable Reactive Mask` | **强制禁用响应遮罩** | 彻底切断游戏发送的响应遮罩，改由超分内部纯时域算法推算 |
| 10 | `Disable Splash message` | **禁用启动提示横幅** | 在游戏加载启动时隐藏 OptiScaler 的版本提示小浮窗 |
| 11 | `Display Res. MV` | **显示分辨率级别的运动矢量** | 告知算法游戏提交的速度场矢量是基于显示分辨率而非内部渲染分辨率生成的 |
| 12 | `Dynamic Res. (DRS)` | **动态分辨率缩放 (DRS)** | 支持游戏根据当前显卡负载在每一帧动态拉伸或缩小内部渲染尺寸 |
| 13 | `Enable Extended Limits` | **解锁缩放比例极限范围 (0.1x ~ 6.0x)** | 打破常规超分辨率 1.0x~3.0x 的安全限制，允许极端的微缩渲染或超采样 |
| 14 | `Enable if the game uses dynamic resolution\nPrevents FSR 4 from switching models when the render size changes` | **如果游戏内部开启了动态分辨率，请务必启用此项\n可防止渲染尺寸波动时 FSR 4 频繁重新加载神经网络模型引发剧烈卡顿** | 动态分辨率与神经网络模型重载防卡顿说明 |
| 15 | `Fix for games that send motion data with preapplied jitter` | **修复某些游戏在提交运动矢量时已经预先附带了亚像素抖动偏移的问题** | 预抖动运动矢量修复原理说明 |
| 16 | `HDR` | **高动态范围 (HDR)** | 告知超分算法当前呈现输出是处于 HDR 高宽容度色彩管线中 |
| 17 | `Init Flags` | **初始化标志位** | DirectX / Vulkan 超分管线在创建时传入的核心 Feature Flags 集合 |
| 18 | `Jitter Cancellation` | **抖动消除** | 在采样前反向扣除摄像机抗锯齿抖动矩阵以获得纯净画面 |
| 19 | `Load ASI plugins` | **加载外部 ASI 插件** | 自动加载放入 plugins 目录的第三方功能补丁（如 OptiPatcher、Special K 等） |
| 20 | `Might help with purple hue in some games` | **有助于解决某些特殊游戏中画面偶现的紫屏或紫雾偏色瑕疵** | 修复色彩空间通道错位的提示 |
| 21 | `Mostly a fix for Unreal Engine games\nTop left part of the screen will be blurry` | **主要用于修复虚幻引擎游戏在某些分辨率下，\n屏幕左上角区域异常模糊不清的常见渲染 BUG** | 虚幻引擎视口对齐修复提示 |
| 22 | `Ntdll Hooks` | **Ntdll 系统级底层钩子** | 在 Windows ntdll 核心层拦截驱动枚举以保证伪装彻底不穿帮 |
| 23 | `Option disabled because the game doesn't provide a Reactive mask` | **该选项显示为灰色不可用，因为当前游戏的原生管线并未生成并提交响应遮罩** | 缺少原生前置资源提示 |
| 24 | `Plugins / Startup` | **外部插件与启动行为** | 配置 ASI 模块自动加载与游戏启动时的提示窗口行为 |
| 25 | `React. Mask Bias` | **响应遮罩权重偏置** | 人为向响应遮罩增减全局敏感度偏移 |
| 26 | `Resource Barriers` | **DirectX 12 显存资源屏障** | 配置底层 GPU 显存纹理在渲染、写入、采样各阶段之间的同步状态屏障覆盖 |
| 27 | `Restore Compute Root Signature` | **还原计算管线根签名 (Root Signature)** | 在执行完超分计算后将 Direct3D 12 根签名状态精确还原，防止游戏后续着色器报错崩溃 |
| 28 | `Restore Graphic Root Signature` | **还原图形管线根签名 (Root Signature)** | 在执行完图形着色后将 Direct3D 12 根签名精确还原，彻底解决跨通道状态污染导致的死锁崩溃 |
| 29 | `Root Signatures` | **根签名状态还原** | 管理 Direct3D 12 根签名的保存与恢复机制 |
| 30 | `Shaders / Limits` | **着色器管理与数值极限** | 配置预编译着色器缓存及缩放比率上下限 |
| 31 | `Some Unreal Engine games need this\n\nTry using if colours flickering or\nobjects have ghosting trails` | **某些虚幻引擎游戏需要勾选此项\n\n若遇到画面色彩频闪或移动物体身后留下严重彩色鬼影，建议开启尝试** | 虚幻引擎运动矢量色彩异常修复建议 |
| 32 | `Spoofing / Hooking` | **显卡伪装与底层挂钩** | 跨硬件解锁各大厂商专有技术的伪装环境卡片 |
| 33 | `Use Binary Reactive Mask` | **使用二值化黑白响应遮罩** | 将响应遮罩强制压制为非 0 即 1 的布尔掩码，消除半透明残影 |
| 34 | `Use Precompiled Shaders` | **使用预编译二进制着色器** | 直接加载随模组打包好的离线预编译着色器字节码，杜绝游戏首次加载时的卡顿与黑屏 |
| 35 | `Use Reactive Mask as Transparency Mask` | **将响应遮罩复用为透明度图层遮罩** | 让插帧算法根据响应遮罩保护半透明特效不被撕裂 |
| 36 | `VLK Extension Spoofing` | **Vulkan 驱动扩展伪装** | 向游戏伪装报告当前环境具备 NVIDIA 专有的 Vulkan 驱动扩展指令集 |
| 37 | `VLK Spoofing` | **Vulkan 显卡硬件伪装** | 在 Vulkan 渲染底层伪装 GPU 设备厂商 ID（Vendor ID） |
| 38 | `Values above 0 activate usage of Reactive mask` | **设置大于 0 的数值将强制激活对响应遮罩的使用** | 响应遮罩开启门槛说明 |
| 39 | `You shouldn't need to change it` | **在通常情况下你完全不需要修改该项参数（保持默认即可）** | 安全默认值建议 |

## 模块 7：DirectX 12 资源屏障与游戏专属修复 (Resource Barriers & Quirks)（共 36 条）

| 序号 | 英文原文 (Source) | 中文翻译 (Target) | 翻译考量与术语依据 (Rationale) |
| :--- | :--- | :--- | :--- |
| 1 | `ALL_SHADER_RESOURCE` | **ALL_SHADER_RESOURCE (全局着色器资源)** | 可供管线中所有阶段着色器并发绑定的 SRV 只读纹理状态 |
| 2 | `ASI` | **ASI 插件** | 放置在 plugins 文件夹下的第三方功能扩展动态链接库 |
| 3 | `AUTO` | **自动判断 (AUTO)** | 由系统根据上下文自动推断最适合的显存屏障状态 |
| 4 | `Active Quirks` | **当前已激活的专属修复补丁** | OptiScaler 自动识别游戏并启用的专有兼容垫片列表 |
| 5 | `Barriers overridden` | **已覆盖的显存资源屏障总数** | 显示当前被 OptiScaler 人为接管重定向的屏障转换次数 |
| 6 | `COMMON` | **COMMON (通用状态)** | DirectX 12 默认基础显存布局状态，支持在只读/写入之间进行平滑过渡 |
| 7 | `COPY_DEST` | **COPY_DEST (数据拷贝目标)** | 显存直接内存传输（CopyResource）的目的端纹理 |
| 8 | `COPY_SOURCE` | **COPY_SOURCE (数据拷贝源)** | 显存直接内存传输（CopyResource）的源端纹理 |
| 9 | `DEPTH_READ` | **DEPTH_READ (深度缓冲区只读)** | 深度模板缓冲区供着色器采样的只读状态 |
| 10 | `DEPTH_WRITE` | **DEPTH_WRITE (深度缓冲区写入)** | 深度模板缓冲区供光栅化阶段写入深度值的状态 |
| 11 | `GENERIC_READ` | **GENERIC_READ (通用只读组合)** | DirectX 12 常见的顶点+常量+着色器资源组合只读状态 |
| 12 | `Hooks / Config` | **底层钩子与配置项生效状态** | 检查各个关键系统函数挂钩是否成功拦截 |
| 13 | `INDEX_BUFFER` | **INDEX_BUFFER (网格索引缓冲)** | 图元索引缓冲区只读状态 |
| 14 | `INDIRECT_ARGUMENT` | **INDIRECT_ARGUMENT (间接绘制参数)** | 供 GPU ExecuteIndirect 调用的间接绘制参数缓冲 |
| 15 | `Loaded ASI Plugins` | **已成功加载的 ASI 插件清单** | 展示游戏启动时被正确注入的插件 DLL 列表 |
| 16 | `NON_PIXEL_SHADER_RESOURCE` | **NON_PIXEL_SHADER_RESOURCE (非像素着色器资源)** | 供顶点/几何/外壳/计算着色器绑定的只读缓冲 |
| 17 | `PIXEL_SHADER_RESOURCE` | **PIXEL_SHADER_RESOURCE (像素着色器资源)** | 供像素阶段（材质贴图采样）绑定的只读纹理 |
| 18 | `PREDICATION` | **PREDICATION (条件执行谓词)** | 供 GPU 进行条件跳过执行的谓词判断缓冲 |
| 19 | `PRESENT` | **PRESENT (交换链呈现等待)** | 已完成渲染、等待垂直同步并送往显示器的交换链纹理状态 |
| 20 | `Quirks` | **游戏专有兼容补丁** | 针对个别已知游戏特殊引擎架构的专门修补方案 |
| 21 | `Quirks / ASI` | **专属补丁 / ASI 插件** | 游戏特性补丁与外部扩展模块综合卡片 |
| 22 | `RAYTRACING_ACCELERATION_STRUCTURE` | **RAYTRACING_ACCELERATION_STRUCTURE (光追加速结构)** | 供 DXR 光线追踪求交遍历的 BVH 加速结构显存状态 |
| 23 | `RENDER_TARGET` | **RENDER_TARGET (色彩渲染目标)** | 光栅化阶段写入像素颜色的主渲染目标缓冲 |
| 24 | `RESOLVE_DEST` | **RESOLVE_DEST (MSAA 解析目标)** | 多重采样抗锯齿解析至普通单采样纹理的目的表面 |
| 25 | `RESOLVE_SOURCE` | **RESOLVE_SOURCE (MSAA 解析源)** | 包含多重采样原始样本的多采样源纹理 |
| 26 | `SHADING_RATE_SOURCE` | **SHADING_RATE_SOURCE (可变着色率源)** | 用于指导可变速率着色(VRS)粗糙度分布的遮罩纹理 |
| 27 | `STREAM_OUT` | **STREAM_OUT (几何流式输出)** | 几何着色阶段向显存流式写回顶点的缓冲区 |
| 28 | `System` | **硬件与系统诊断** | 当前操作系统、驱动版本与显卡能力清单卡片 |
| 29 | `UNORDERED_ACCESS` | **UNORDERED_ACCESS (无序并发访问 UAV)** | 供计算着色器进行高并发读写的数据缓冲区状态 |
| 30 | `VERTEX_AND_CONSTANT_BUFFER` | **VERTEX_AND_CONSTANT_BUFFER (顶点与常量缓冲)** | 供顶点装配或常量寄存器读取的只读状态 |
| 31 | `VIDEO_DECODE_READ` | **VIDEO_DECODE_READ (视频解码读取)** | 视频硬件解码引擎所读取的压缩数据源缓冲 |
| 32 | `VIDEO_DECODE_WRITE` | **VIDEO_DECODE_WRITE (视频解码写入)** | 视频硬件解码引擎输出非压缩画面的目标表面 |
| 33 | `VIDEO_ENCODE_READ` | **VIDEO_ENCODE_READ (视频编码读取)** | 视频硬件编码引擎读取待压缩原始画面的表面 |
| 34 | `VIDEO_ENCODE_WRITE` | **VIDEO_ENCODE_WRITE (视频编码写入)** | 视频硬件编码引擎写出压缩码流的缓冲 |
| 35 | `VIDEO_PROCESS_READ` | **VIDEO_PROCESS_READ (视频后处理读取)** | 视频处理器进行缩放去交错等操作的输入源 |
| 36 | `VIDEO_PROCESS_WRITE` | **VIDEO_PROCESS_WRITE (视频后处理写入)** | 视频处理器完成滤波处理的输出目标 |

## 模块 8：菜单界面、主题、快捷键与性能监控 (Menu UI, Theme, Keybinds, FPS Overlay)（共 59 条）

| 序号 | 英文原文 (Source) | 中文翻译 (Target) | 翻译考量与术语依据 (Rationale) |
| :--- | :--- | :--- | :--- |
| 1 | `%-12s %4.1fms` | **%-12s %4.1fms** | 性能指标标签与毫秒时间格式化字符串，保持原样 |
| 2 | `Accent Colour` | **界面强调主色调** | 控制菜单中复选框勾选、滑块与高亮边框的强调色 |
| 3 | `Background Alpha` | **背景不透明度** | 控制菜单面板与悬浮叠加层的背景透明度 |
| 4 | `Background Blur` | **毛玻璃背景模糊** | 在菜单面板底层应用实时高斯模糊，营造高级半透明亚克力质感 |
| 5 | `Background Colour` | **背景底色** | 自定义菜单面板的基础背景底色 |
| 6 | `Blue` | **海蓝色** | 经典冷蓝色主题配色预设 |
| 7 | `Blur Strength` | **模糊半径强度** | 调节毛玻璃背景模糊的扩散半径强度 |
| 8 | `Bottom Left` | **左下角** | 叠加层锚定在屏幕左下角 |
| 9 | `Bottom Right` | **右下角** | 叠加层锚定在屏幕右下角 |
| 10 | `DLSSG` | **DLSSG 帧生成** | NVIDIA DLSS 帧生成技术标志 |
| 11 | `Detailed` | **详细性能信息** | 展示帧率、平均帧率、当前超分与插帧模式详细文本 |
| 12 | `Detailed + Graph` | **详细信息 + 帧生成时间曲线图** | 在详细性能文本下方附带平滑绘制的实时微秒级帧生成时间图表 |
| 13 | `Enabler` | **DLSS Enabler 框架** | DLSS Enabler 外部插帧转译桥接框架 |
| 14 | `Error` | **错误** | 日志输出级别：仅记录严重错误与异常 |
| 15 | `Escape to cancel, Backspace to unbind` | **按 Esc 键取消监听，按退格键(Backspace)清除解绑快捷键** | 修改热键时的底部操作引导说明 |
| 16 | `FGId: %llu, RfxId: %llu` | **插帧实例ID: %llu, Reflex实例ID: %llu** | 帧生成底层上下文句柄与 Reflex 实例句柄展示 |
| 17 | `FPS Overlay` | **性能监视叠加层 (OSD)** | 在游戏画面角落实时悬浮显示帧率、帧生成时间与超分工作状态的 HUD 叠加层 |
| 18 | `FPS Overlay Enabled` | **启用性能监视叠加层** | 开闭屏幕角落帧率与渲染状态悬浮窗 |
| 19 | `Full` | **全面全景信息** | 展示所有耗时细节、延迟、超分辨率类型与模型信息 |
| 20 | `Full + Graph` | **全面信息 + 帧生成时间曲线图** | 展示全套性能度量指标并叠加实时走势折线图 |
| 21 | `Gray` | **深空灰** | 简约耐看的黑灰极客主题配色预设 |
| 22 | `Green` | **荧光绿** | 富有科技感的绿色主题配色预设 |
| 23 | `Horizontal` | **水平横排布局** | 将性能监控数据从上下竖排改为水平横向一字排布 |
| 24 | `Information` | **常规信息** | 日志输出级别：记录主要流程执行与状态汇报 |
| 25 | `Just FPS` | **仅显示帧率数值 (FPS)** | 极简模式，屏幕仅呈现当前帧率数字，最大程度避免画面遮挡 |
| 26 | `Key combinations are currently NOT supported!` | **当前版本暂不支持多键组合快捷键（如 Ctrl+Shift+X）！** | 绑定单键时的提示说明 |
| 27 | `Keybinds` | **快捷键绑定** | 配置呼出菜单、开关插帧、切换监控模式的热键 |
| 28 | `Light Theme` | **明亮浅色主题** | 将整体菜单风格切换为浅色明亮配色 |
| 29 | `Log Level` | **日志输出级别** | 设定控制台或日志文件记录的严重等级门槛 |
| 30 | `Logging` | **运行日志输出** | 配置诊断日志的记录级别与写出目标 |
| 31 | `Low latency timings, whole frame: %.1fms` | **低延迟时序，整帧总耗时: %.1fms** | 低延迟子系统全帧端到端耗时 |
| 32 | `Menu` | **菜单** | 菜单相关设置卡片 |
| 33 | `Menu Theme and Color` | **菜单主题与个性化色彩** | 自定义 OptiScaler 设置面板的视觉外观、底色与强调高亮 |
| 34 | `OptiScaler - %s for menu` | **OptiScaler - 按 %s 键打开设置菜单** | 游戏启动时左上角浮现的操作提示通知横幅 |
| 35 | `Orange` | **落日橙** | 温暖醒目的橙色主题配色预设 |
| 36 | `Overlay Position` | **叠加层屏幕锚点位置** | 选择性能监视悬浮窗固定在显示器的哪个角落 |
| 37 | `Overlay Type` | **叠加层信息详略等级** | 选择仅显示帧率、详细指标或是附带实时走势图 |
| 38 | `Presets:` | **配色预设：** | 快速选用推荐的经典色彩搭配 |
| 39 | `Purple` | **霓虹紫** | 赛博朋克风格的暗紫色主题配色预设 |
| 40 | `Red` | **赤焰红** | 醒目鲜艳的红色主题配色预设 |
| 41 | `Reflex timings` | **Reflex 延迟拆解指标** | 展示输入轮询、模拟、渲染准备等各个管线阶段的细分延迟 |
| 42 | `Reflex timings, whole frame: %.1fms` | **Reflex 延迟度量，整帧耗时: %.1fms** | Reflex 汇报的整帧端到端耗时统计 |
| 43 | `Reset Accent Color` | **重置强调色** | 恢复官方默认的强调主色调 |
| 44 | `Reset BG Colour` | **重置背景底色** | 恢复官方默认的半透明黑色面板背景 |
| 45 | `Same as menu` | **跟随主菜单缩放** | 让悬浮叠加层的字体尺寸严格同步菜单面板的大小 |
| 46 | `Scale` | **界面缩放比例** | 自定义设置菜单与字体的大小比例（支持 1.0x ~ 2.0x） |
| 47 | `Shows the current render -> output resolution and upscale ratio in the overlay` | **在悬浮层中实时显示“渲染分辨率 -> 输出分辨率”及具体缩放倍率** | 增强性能监控显示维度的选项说明 |
| 48 | `Simple` | **简洁概览** | 显示帧率与平均帧率，简洁明了 |
| 49 | `Single File` | **单一日志文件** | 将所有会话日志写入同一个文件中便于翻查 |
| 50 | `Teal` | **青碧色** | 清新淡雅的青绿色主题配色预设 |
| 51 | `To Console` | **输出到调试控制台** | 将实时运行日志输出至挂载的终端控制台窗口 |
| 52 | `To File` | **输出到磁盘日志文件** | 将运行诊断日志写入 OptiScaler.log 文本中 |
| 53 | `Top Left` | **左上角** | 叠加层锚定在屏幕左上角 |
| 54 | `Top Right` | **右上角** | 叠加层锚定在屏幕右上角 |
| 55 | `Trace` | **详细追踪 (Trace)** | 日志输出级别：记录最底层极细致的调用堆栈与入参 |
| 56 | `Upscale Ratio` | **显示超分缩放倍率** | 在性能监控叠加层中打印当前超分辨率的具体比例 |
| 57 | `Use Theme Colors` | **悬浮层应用主题配色** | 让角落的性能监视文字颜色与当前菜单主题高亮色保持一致 |
| 58 | `Warning` | **警告 (Warning)** | 日志输出级别：记录异常警告及可能的性能隐患 |
| 59 | `Yellow` | **琥珀黄** | 明亮醒目的黄色主题配色预设 |

## 模块 9：通用按钮、状态与交互控件 (Common Buttons, States & Dialogs)（共 50 条）

| 序号 | 英文原文 (Source) | 中文翻译 (Target) | 翻译考量与术语依据 (Rationale) |
| :--- | :--- | :--- | :--- |
| 1 | `%08x, %s->%s, Count: %llu, %s` | **%08x, %s->%s, 次数: %llu, %s** | 调试日志中记录显存资源状态转换轨迹的格式串 |
| 2 | `Active` | **当前活动生效** | 指示某项功能正在实时处理数据 |
| 3 | `Affects both FSR-FG & Upscalers` | **此设置将同时作用于 FSR 帧生成及超分辨率管线** | 跨子系统联动参数提示 |
| 4 | `Allow 1X` | **允许 1.0X 原生分辨率运行** | 允许在无内部降采样的原生分辨率下直接调用超分或插帧通道 |
| 5 | `Boxes to show` | **自定义选项卡勾选卡片** | 展开勾选要在自定义快速面板中显示的模块列表 |
| 6 | `Camera Far` | **相机远裁剪面** | 游戏三维投影相机的远距离视野剔除平面 |
| 7 | `Camera Near` | **相机近裁剪面** | 游戏三维投影相机的近距离视野裁剪平面 |
| 8 | `Clear` | **清空清除** | 清空当前已配置的数据或列表记录 |
| 9 | `Click to open the OptiScaler Wiki page\nin your default browser\n\nCompatibility list with known game issues\nand workarounds, FG options explained\nand other useful info` | **点击在默认浏览器中打开 OptiScaler 官方 Wiki 百科页面\n\n内含详尽的游戏兼容性已知问题与绕过技巧、\n各类插帧选项的深度原理解析等珍贵资料** | 帮助中心直跳 Wiki 指引 |
| 10 | `Close` | **关闭退出** | 关闭当前弹出卡片或退出设置菜单 |
| 11 | `Debug View` | **调试分屏视图** | 在画面中分屏可视化呈现底层运算图层 |
| 12 | `Default` | **系统默认** | 使用系统标准出厂预设值 |
| 13 | `Detected` | **系统检测报告** | 显示当前硬件与环境探测到的各项功能支持度 |
| 14 | `Display Width` | **物理显示宽度 (像素)** | 显示器当前实际输出的水平分辨率像素点数 |
| 15 | `Dynamic MFG` | **动态多帧生成 (DMFG)** | 根据实时渲染负载动态智能变速的多倍插帧技术 |
| 16 | `Extra shaders:` | **附加着色器模块:** | 列出管线中附带加载的辅助运算着色器 |
| 17 | `FSR Common Settings` | **FSR 通用参数设置** | 同时影响 FSR 超分辨率与 FSR 帧生成的共有参数控制卡片 |
| 18 | `FoV & Camera Values` | **视场角(FoV)与相机几何参数** | 手动微调三维镜头几何参数以解决插帧视差不匹配问题 |
| 19 | `Frame Generation mode` | **帧生成工作模式** | 选择当前使用的插帧模式类型 |
| 20 | `Frame Generation mode\nDefault follows the game's DLSS FG setting` | **帧生成工作模式\n默认模式将严格遵从游戏原生画质菜单中的 DLSS 帧生成开关** | 遵从游戏设定的模式说明 |
| 21 | `Frametime: %.2fms / %.1ffps (avg: %.1ffps)` | **帧生成时间: %.2fms / 实时: %.1ffps (平均: %.1ffps)** | 底部状态栏高精度实时帧率与微秒帧耗时统计 |
| 22 | `Horz. FOV` | **水平视场角 (Horz. FoV)** | 游戏相机水平方向的广角视野范围（度） |
| 23 | `Menu Scale` | **主菜单缩放比例** | 调整 OptiScaler 设置面板整体大小尺寸的控制卡片 |
| 24 | `Might help achieve better image quality` | **可能有助于在特定场景下获得更出色的画面质感** | 画质调优建议 |
| 25 | `Might help achieve better image quality\nAnd potentially less ghosting` | **可能有助于提升画质纯净度，\n并有望显著降低运动物体边缘的拖尾鬼影** | 防鬼影调优建议 |
| 26 | `Motion Adaptive Sharpness` | **运动自适应动态锐化 (MAS)** | 静止极锐、运动防噪的动态图像锐化技术卡片 |
| 27 | `Near: %.1f Far: %.1f` | **近景截断: %.1f 远景截断: %.1f** | 相机近景与远景平面的实时截断数值 |
| 28 | `None of the picked boxes are available right now` | **当前选定要展示的功能卡片在当前游戏上下文中均处于不可用状态** | 自定义面板空状态提示 |
| 29 | `Nothing picked yet, choose the boxes in Menu > Custom Tab` | **尚未挑选任何功能卡片，请前往“菜单 > 自定义选项卡”中勾选需要常驻展示的卡片** | 引导初次使用自定义面板的操作提示 |
| 30 | `Open Wiki` | **打开官方 Wiki 指南** | 点击在浏览器中访问 OptiScaler 完整文档知识库 |
| 31 | `Open release page` | **打开发布下载页面** | 点击在浏览器中访问 GitHub Releases 页面下载最新稳定版 |
| 32 | `Press any key...` | **请按下任意键...** | 正在监听键盘或鼠标输入以捕获新的快捷键 |
| 33 | `R` | **重置 (R)** | 将单项参数快速复位为出厂默认值的快捷按钮 |
| 34 | `Range: %.2f ms - %.2f ms` | **波动范围: %.2f ms - %.2f ms** | 帧生成时间波动的最低值与最高值范围区间 |
| 35 | `Render Width` | **内部渲染宽度 (像素)** | 送入超分辨率算法前的底层三维实际渲染水平宽度 |
| 36 | `Res` | **分辨率重置** | 快速恢复默认分辨率设定的操作按钮 |
| 37 | `Reset Camera Values` | **重置相机几何参数** | 将视场角 FoV 与裁剪面复位为游戏引擎原生自动探测值 |
| 38 | `Save Settings` | **保存当前所有设置** | 将本次在菜单中所做的所有修改永久固化写入 OptiScaler.ini 配置文件 |
| 39 | `Show Custom tab` | **在侧边栏显示自定义选项卡** | 控制是否在左侧导航栏最顶部开启专属的自定义常用收藏页面 |
| 40 | `Target FPS` | **目标帧率 (FPS)** | 动态调频插帧所期望达到的平稳帧率目标 |
| 41 | `Upscaler Quality` | **超分辨率画质预设挡位** | 选择质量、平衡、性能等官方标准缩放倍率档位 |
| 42 | `Upscaler Ratio` | **超分辨率精细缩放比率** | 以任意精细步长自由设定超分辨率的内部几何缩放系数 |
| 43 | `Use FSR Input Values` | **直接沿用 FSR 输入的原始几何参数** | 不进行二次矫正，直接相信游戏传递给 FSR 的参数 |
| 44 | `Use Horz. Fov` | **以水平视场角(Horz. FoV)为基准进行空间计算** | 在带鱼屏或超宽屏下锁定水平视场比例 |
| 45 | `Use Value` | **强制应用自定义绝对数值** | 放弃算法自动预估，强行锁定为用户手动指定的数值 |
| 46 | `Use Vert. Fov` | **以垂直视场角(Vert. FoV)为基准进行空间计算** | 绝大多数三维引擎默认遵从垂直视场角体系 |
| 47 | `Use as FPS limit` | **直接同步设为当前帧率限制上限** | 将当前计算出的平滑目标同步写入帧率限制器 |
| 48 | `Uses frametimes provided by\nDLSSG or FSR-FG` | **直接采纳 DLSS 帧生成或 FSR 帧生成官方传递的基准帧生成时间** | 时钟源选项：采纳输入源数据 |
| 49 | `Vert. FOV` | **垂直视场角 (Vert. FoV)** | 游戏相机垂直方向的三维视野范围（度） |
| 50 | `nvngx.ini detected, please move over to using OptiScaler.ini and delete the old config` | **检测到目录中存在已废弃的旧版 nvngx.ini 配置文件，请迁移所有自定义配置至 OptiScaler.ini 并删除该残留文件以防配置冲突** | 旧版配置文件废弃与迁移警示 |

