
---
title: nvm
---

### [nvm-sh nvm](https://github.com/nvm-sh/nvm)

**项目核心内容总结：**

**1. 项目功能**  
nvm（Node Version Manager）是一款用于管理Node.js版本的工具，支持安装、切换和管理多个Node.js版本，适用于开发环境中的版本兼容需求。

**2. 使用方法**  
- 通过命令行安装：使用 `curl` 或 `wget` 下载安装脚本并执行（如 `curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.40.3/install.sh | bash`）。  
- 安装后可通过 `nvm install <版本号>` 安装指定版本，`nvm use <版本号>` 切换版本。  
- 支持列出已安装版本（`nvm ls`）和查看可用版本（`nvm ls-remote`）。

**3. 主要特性**  
- **多版本管理**：支持同时安装多个Node.js版本，并快速切换。  
- **跨平台兼容**：适用于Linux、macOS、Windows（WSL）等系统。  
- **自动适配**：自动处理依赖库（如zlib）的编译问题。  
- **特殊场景支持**：针对Apple Silicon芯片的Mac提供编译旧版本Node.js的解决方案（需通过Rosetta 2）。  

**4. 注意事项**  
- 安装旧版本Node.js（如v16以下）时，需在Rosetta 2环境下编译。  
- WSL用户若遇到网络问题，需手动配置DNS（如设置 `nameserver 8.8.8.8`）。  
- 项目仅维护最新版本，旧版本需通过商业支持获取安全更新。