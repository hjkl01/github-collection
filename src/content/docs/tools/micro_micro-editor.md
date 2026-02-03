
---
title: micro
---

### [micro-editor micro](https://github.com/micro-editor/micro)  ![GitHub Repo stars](https://img.shields.io/github/stars/micro-editor/micro?style=social)

**项目核心内容总结：**  
micro 是一款基于终端的文本编辑器，旨在提供直观易用的体验，同时利用现代终端功能。其核心特性包括：  
- **无需依赖**：单个静态二进制文件，即装即用。  
- **跨平台支持**：兼容所有 Go 支持的平台（Windows、Linux、macOS 等）。  
- **功能丰富**：多光标编辑、常见快捷键（如 Ctrl-s、Ctrl-c）、语法高亮（支持 130+ 语言）、True Color 显示、插件系统（Lua 编写）、持久撤销、自动 linting、剪贴板支持等。  
- **易用性**：类似 nano 的菜单提示、鼠标操作（拖拽选中、双击选词、三击选行）、内置帮助系统。  

**使用方法**：  
- 安装方式包括下载预编译二进制、通过 Homebrew/Snap 等包管理器安装，或从源码构建。  
- 启动方式：`micro 文件路径` 或 `micro` 新建文件；支持通过管道从 stdin 创建缓冲区（如 `ip a | micro`）。  

**注意事项**：  
- macOS 建议使用 iTerm2 以获得更好的鼠标和键盘支持。  
- Windows 下推荐使用 Windows Terminal，避免默认终端的字体问题。  
- 若终端不支持 256 色，可通过 `Ctrl-e` 设置为 `simple` 色彩方案。  
- Cygwin、Mingw 等环境需通过 `winpty` 工具运行。