
---
title: ueberzugpp
---

### [jstkdng ueberzugpp](https://github.com/jstkdng/ueberzugpp)  ![GitHub Repo stars](https://img.shields.io/github/stars/jstkdng/ueberzugpp?style=social)

Überzug++ 是基于 C++ 的命令行工具，作为已废弃的 ueberzug 替代品，用于在终端中显示图像。支持 X11、Wayland、sixel、kitty 及 iterm2 等渲染后端。

核心功能：
1. 多环境支持：兼容 Wayland（sway/hyprland）、MacOS、X11 及 tmux，支持无 WINDOWID 终端。
2. 图像性能：支持 GIF 和动画 WEBP，具备 OpenCV 快速缩放、缓存及无内存泄漏特性。
3. 控制接口：提供 `layer` 命令，通过 JSON 对象控制图像显示/移除，支持命令行、配置文件或 Unix Socket 通信。
4. 广泛集成：兼容多种终端应用（如 ytfzf、vifm、yazi 等），可无缝替换原 ueberzug 使用。