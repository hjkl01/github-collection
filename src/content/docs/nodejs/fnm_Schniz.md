
---
title: fnm
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/Schniz/fnm?style=social) ](https://github.com/Schniz/fnm)
### [Schniz fnm](https://github.com/Schniz/fnm)

**核心内容总结：**

**项目功能**  
`fnm` 是一个用 Rust 编写的快速、简洁的 Node.js 版本管理工具，支持跨平台（macOS、Windows、Linux），可读取 `.node-version` 和 `.nvmrc` 文件自动切换 Node.js 版本。

**主要特性**  
- 跨平台支持（macOS、Windows、Linux）  
- 单文件安装，启动速度快  
- 兼容 `.node-version` 和 `.nvmrc` 文件  
- 支持多种安装方式（脚本、Homebrew、Winget、Scoop、Chocolatey、Cargo、手动下载二进制文件）  

**使用方法**  
1. **安装**  
   - macOS/Linux：通过脚本安装（`curl -fsSL https://fnm.vercel.app/install | bash`），或使用 Homebrew（`brew install fnm`）。  
   - Windows：通过 Winget、Scoop、Chocolatey 安装。  
   - 所有系统：使用 Cargo（`cargo install fnm`）或手动下载二进制文件。  

2. **配置 Shell**  
   安装后需通过 `fnm env` 配置环境变量，不同 Shell（Bash、Zsh、Fish、PowerShell 等）需添加对应代码到配置文件。  

3. **卸载**  
   删除 `.fnm` 文件夹，并从 Shell 配置文件中移除相关代码。  

4. **升级**  
   macOS 使用 `brew upgrade fnm`，其他系统可重复安装流程并添加 `--skip-shell` 参数避免重复配置。