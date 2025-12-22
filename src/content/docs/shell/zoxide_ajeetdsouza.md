
---
title: zoxide
---

### [ajeetdsouza zoxide](https://github.com/ajeetdsouza/zoxide)  ![GitHub Repo stars](https://img.shields.io/github/stars/ajeetdsouza/zoxide?style=social)

**项目核心内容总结：**  
zoxide 是一个基于智能算法的目录跳转工具，可替代传统 `cd` 命令，实现更快速、更高效的目录导航。  

**主要功能与特性：**  
1. **智能匹配**：通过路径匹配算法，输入部分路径即可快速定位目标目录。  
2. **跨 Shell 支持**：兼容 Bash、Zsh、Fish 等主流 Shell，提供无缝集成。  
3. **高效操作**：支持 `z`（直接跳转）、`zo`（打开文件管理器）、`zx`（跳转并执行命令）等快捷指令。  
4. **自定义配置**：可通过环境变量调整算法参数（如匹配权重、缓存路径等）。  

**使用方法：**  
- 安装后，使用 `z [路径关键词]` 快速跳转目录。  
- 支持通过 `zoxide init [shell]` 自动配置 Shell 插件。  

**其他亮点：**  
- 提供与 Alfred、Raycast 等 macOS 工具及 Ranger、Neovim 等文件管理器的深度集成。  
- 开源且跨平台，支持 Linux、macOS、Windows 等系统。