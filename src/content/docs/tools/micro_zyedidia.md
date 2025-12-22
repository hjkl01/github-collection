
---
title: micro
---

### [zyedidia micro](https://github.com/zyedidia/micro)  ![GitHub Repo stars](https://img.shields.io/github/stars/zyedidia/micro?style=social)

**项目核心内容总结：**  

**micro** 是一款基于终端的文本编辑器，旨在提供直观易用的体验，同时利用现代终端的功能。其特点包括：  
- **功能特性**：支持多光标、常见快捷键（如 Ctrl-s、Ctrl-c）、分屏/标签、鼠标操作（选中文本、单词、行）、跨平台（支持 Go 兼容系统，但不支持 Cygwin/Mingw/Plan9）、130+ 语法高亮、真彩色、系统剪贴板、插件系统（Lua 编写）、持久撤销、自动 linting 等。  
- **使用方法**：通过 `micro 文件路径` 或 `micro` 打开空文件；支持从 stdin 创建缓冲区（如 `ip a | micro`）。  
- **安装方式**：提供预编译二进制文件、第三方脚本（如 `curl https://micro-editor.com/install.sh | sh`）、包管理器（Homebrew、Snap）及源码构建（需 Go 环境）。  
- **注意事项**：Linux 需安装 xclip/xsel 或 wl-clipboard 以启用系统剪贴板；macOS 建议使用 iTerm2；Windows WSL 推荐使用 Windows Terminal。  

**主要优势**：无需依赖项、轻量级、支持插件扩展、语法高亮丰富，适合终端用户及远程开发场景。