
---
title: fish-shell
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/fish-shell/fish-shell?style=social) ](https://github.com/fish-shell/fish-shell)
### [fish-shell fish-shell](https://github.com/fish-shell/fish-shell)

fish 是一个用户友好的交互式命令行 shell，支持 macOS、Linux 等系统，具备语法高亮、实时自动补全、智能提示等功能，无需额外配置即可使用。

**核心功能与特性**  
- 提供交互式命令行体验，支持语法高亮、自动补全和智能提示。  
- 官方网站提供下载、截图和详细文档（https://fishshell.com/）。  

**使用方法**  
- **macOS**：通过 Homebrew（`brew install fish`）、MacPorts 或官网安装。  
- **Linux**：通过 openSUSE Build Service 或 Ubuntu PPA 安装。  
- **Windows**：支持 WSL（Linux 子系统）或 Cygwin/MSYS2 安装。  

**构建依赖**  
- 需要 Rust（1.85+）、CMake（3.15+）、C 编译器、PCRE2（可选）等。  
- 文档构建需 Sphinx，测试需 Python 3.5+、git、diff 等工具。  

**构建方式**  
1. **CMake**：创建构建目录，运行 `cmake` 和 `cmake --build .` 编译，`sudo cmake --install .` 安装。  
2. **Cargo**：使用 `cargo install` 构建，支持跨平台静态链接。  

**其他**  
- 安装后通过 `fish` 命令启动。  
- 支持插件扩展，可通过 `extra_functionsdir` 等参数自定义配置。  
- 问题反馈和协作可通过 GitHub 提交 Issue 或参与社区讨论。