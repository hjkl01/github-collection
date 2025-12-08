
---
title: shadPS4
---

### [shadps4-emu shadPS4](https://github.com/shadps4-emu/shadPS4)

**shadPS4** 是一个早期的 PlayStation 4 模拟器，支持 Windows、Linux 和 macOS，使用 C++ 编写。其核心功能为模拟 PS4 硬件和系统，但本身不含图形界面，用户需通过 [QtLauncher](https://github.com/shadps4-emu/shadps4-qtlauncher/releases) 启动游戏。

**主要特性**：
- 当前可运行《血源诅咒》《黑暗之魂重制版》等部分游戏。
- 支持通过命令行启动游戏（如 `shadPS4 CUSA00001`），并提供参数自定义（如 `--fullscreen`、`--config-clean`）。
- 支持 Xbox 和 DualShock 控制器，键盘映射可通过设置菜单自定义（如 F10 显示帧率、F11 全屏）。
- 需要手动放置特定固件模块（如 `libSceFont.sprx` 等）至 `sys_modules` 文件夹，且模块需从合法 PS4 主机提取。

**注意事项**：
- macOS 需 15.4 及以上版本，Intel Mac 存在显卡兼容性问题。
- 项目处于早期开发阶段，复杂游戏可能无法稳定运行。
- 问题反馈可通过 Discord 服务器、Twitter（@shadps4）或官网（[shadps4.net](https://shadps4.net/)）获取支持。

**许可证**：采用 [GPL-2.0](https://github.com/shadps4-emu/shadPS4/blob/main/LICENSE) 开源协议。