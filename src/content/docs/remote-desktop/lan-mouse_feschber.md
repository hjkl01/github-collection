
---
title: lan-mouse
---

### [feschber lan-mouse](https://github.com/feschber/lan-mouse)  ![GitHub Repo stars](https://img.shields.io/github/stars/feschber/lan-mouse?style=social)

Lan Mouse 是一款跨平台的鼠标和键盘共享软件（软件 KVM 切换器），允许用户使用一套键鼠控制多台电脑，功能类似于 Apple 通用控制或 Synergy。

主要功能与特点：
- **核心用途**：跨操作系统共享输入设备，实现多机无缝协作，作为专有工具的开源替代方案。
- **技术实现**：基于 Rust 编写以保证高性能，使用 DTLS 加密网络流量，提供 GTK 图形前端。
- **系统兼容**：全面支持 Windows、macOS 及 Linux（包括 GNOME、KDE、Wayland/Wlroots 等）。
- **使用模式**：支持图形界面、命令行、守护进程及 Systemd 服务，配置支持 TOML 文件。
- **其他说明**：包含 Android/iOS 概念验证版作为远程控制，Linux X11 当前仅支持接收端。