
---
title: xdotool
---

### [jordansissel xdotool](https://github.com/jordansissel/xdotool)

**项目核心内容总结：**

`xdotool` 是一个基于 X11 的自动化工具，主要用于模拟键盘输入、鼠标操作，以及窗口管理（如移动、调整大小、关闭窗口等）。其功能依赖于 X11 的 XTEST 扩展和 Xlib 函数，**不兼容 Wayland 系统**（需注意：Wayland 用户需使用替代工具如 `ydotool` 或 `dotool`）。

**主要功能：**
- 模拟键盘输入（如 `xdotool type "文本"`）；
- 发送按键事件（如 `xdotool key ctrl+l`）；
- 操作窗口（搜索、关闭、调整大小、切换桌面等）；
- 支持通过命令组合实现复杂操作（如自动聚焦浏览器地址栏）。

**安装方式：**
支持主流 Linux 发行版（Debian/Ubuntu/Fedora/FreeBSD/OpenSUSE）及 macOS（通过包管理器安装）。

**使用限制：**
- **Wayland 系统不兼容**，部分功能（如窗口搜索、输入模拟）无法正常工作；
- 需确保系统已安装 X11 相关库（如 `xlib`、`xtst` 等）以编译源码。