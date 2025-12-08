
---
title: bluetui
---

### [pythops bluetui](https://github.com/pythops/bluetui)

**项目功能**  
bluetui 是一个基于终端的用户界面（TUI），用于在 Linux 系统上管理蓝牙设备，支持适配器控制、设备配对/连接/重命名、扫描控制等功能。

**使用方法**  
- **安装方式**：提供多种安装途径，包括下载二进制文件、通过 crates.io 安装、Arch Linux 软件仓库、Gentoo Overlay、x-cmd 工具或从源码编译。  
- **操作快捷键**：通过键盘控制界面（如 `Tab`/`Shift+Tab` 切换区域，`s` 开始/停止扫描，`p`/`o`/`d` 控制适配器状态，`u`/`Space`/`Enter` 等操作设备）。  
- **配置自定义**：支持通过 `~/.config/bluetui/config.toml` 文件调整布局、窗口宽度、快捷键绑定等参数。

**主要特性**  
- 支持主流 Linux 发行版（Arch、Gentoo 等）及包管理工具。  
- 提供丰富的终端交互功能（如配对、连接、信任管理、设备重命名）。  
- 配置灵活，支持自定义快捷键和界面布局。  
- 遵循 GPLv3 开源协议。  

**相关项目**  
若需管理 WiFi，可参考同作者开发的 TUI 工具 [impala](https://github.com/pythops/impala)。