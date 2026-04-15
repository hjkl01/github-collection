### [AXe](https://github.com/cameroncooke/AXe) ![GitHub Repo stars](https://img.shields.io/github/stars/cameroncooke/AXe?style=social)

AXe 是一个面向 iOS 模拟器的单文件命令行自动化工具，基于 Apple 无障碍 API 与 HID 能力，核心功能包括：

- **触控与手势自动化**：支持坐标点击、按无障碍元素点击、滑动、底层 touch down/up、长按，以及预设手势（上下左右滚动、四边缘滑动）。
- **文本与键盘输入**：支持文本输入（直接输入 / stdin / 文件）、单键按压、按键序列、组合键（如 Cmd+A）。
- **硬件按键模拟**：支持 Home、Lock/Power、Side Button、Siri、Apple Pay 按键。
- **精细时序控制**：支持动作前后延迟、手势/按键持续时长、序列间隔，便于复杂多步骤自动化。
- **批处理链式执行**：可一次执行多步操作（命令行、文件或 stdin 输入步骤），默认失败即停，也可设置继续执行。
- **截图与视频能力**：支持截图、视频流输出（MJPEG/JPEG/ffmpeg/BGRA）和直接录制 MP4（H.264），可调帧率、质量和缩放。
- **无障碍与设备信息**：支持获取全屏或指定点的 UI 无障碍树信息，并可列出可用模拟器。

项目定位上，AXe 相比 idb 更轻量：**无需客户端/服务端架构、无守护进程、易脚本集成**，专注 UI 自动化并覆盖完整 HID 能力。