
---
title: edit
---

### [microsoft edit](https://github.com/microsoft/edit)

**项目核心内容总结：**

Edit 是一款灵感源自经典 MS-DOS 编辑器的现代文本编辑器，界面和操作逻辑类似 VS Code，旨在为非终端用户提供建易用的编辑体验。  

**功能与特性：**  
- 支持跨平台（Windows、macOS、UNIX 等）；  
- 提供基础文本编辑功能，包含搜索与替换（依赖 ICU 库）；  
- 支持多语言配置（通过环境变量指定语言包）。  

**使用方法：**  
- **安装**：Windows 用户可通过 WinGet 命令 `winget install Microsoft.Edit` 安装，或从 GitHub 发布页下载二进制文件；  
- **构建**：需安装 Rust 及 nightly 工具链，通过 `cargo build` 指令编译（需根据 Rust 版本选择不同配置文件）。  

**构建配置选项：**  
- 可通过环境变量自定义 ICU 库路径、语言包范围等，适应不同系统环境（如 macOS/UNIX 的动态库版本控制）。  

**注意事项：**  
- 包维护者建议将可执行文件命名为 `msedit` 以避免与系统命令冲突；  
- ICU 库依赖需根据系统动态库命名规则调整环境变量配置。