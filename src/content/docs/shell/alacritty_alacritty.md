
---
title: alacritty
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/alacritty/alacritty?style=social) ](https://github.com/alacritty/alacritty)
### [alacritty alacritty](https://github.com/alacritty/alacritty)

**核心内容总结：**  
Alacritty 是一个基于 OpenGL 的跨平台终端模拟器，支持 Linux、macOS、Windows 和 BSD 系统，提供高性能和可高度自定义的配置。其核心特性包括 GPU 加速渲染、支持滚动回放（scrollback）、跨平台兼容性及简洁的默认配置。  

**使用方法：**  
- 通过包管理器安装（各平台支持）或从 [GitHub 发布页面](https://github.com/alacritty/alacritty/releases) 下载预编译二进制文件。  
- 配置文件需手动创建，支持路径包括 `$XDG_CONFIG_HOME/alacritty/alacritty.toml`、`$HOME/.config/alacritty/alacritty.toml` 等（Windows 为 `%APPDATA%\alacritty\alacritty.toml`）。  

**主要特性：**  
- 基于 GPU 的渲染，提升性能表现；  
- 支持滚动回放、字体渲染优化；  
- 通过 [vtebench](https://github.com/alacritty/vtebench) 基准测试验证性能；  
- 不内置标签页或分割窗口功能，建议结合窗口管理器或终端多路复用器（如 tmux）使用。  

**注意事项：**  
- Windows 需要 Windows 10 1809 或更高版本以支持 ConPTY；  
- 项目处于 beta 阶段，部分功能可能未完善。  

**许可证：** 采用 [Apache License 2.0](https://github.com/alacritty/alacritty/blob/master/LICENSE-APACHE) 开源协议。