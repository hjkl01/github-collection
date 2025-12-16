
---
title: n
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/tj/n?style=social) ](https://github.com/tj/n)
### [tj n](https://github.com/tj/n)

**核心内容总结：**  
**项目功能**：`n` 是一个用于管理 Node.js 版本的工具，支持安装、切换、卸载不同版本的 Node.js，无需依赖子 shell 或复杂配置文件。  

**使用方法**：  
1. **安装**：通过 `npm install -g n` 或直接下载脚本安装；  
2. **版本管理**：使用 `n [版本号]` 安装指定版本（如 `n 14`），支持 `lts`（长期支持版）、`latest`（最新版）等标签；  
3. **卸载与清理**：`n uninstall` 卸载当前版本，`n rm [版本号]` 删除缓存版本，`--cleanup` 安装后自动清理缓存；  
4. **离线使用**：`n --offline [版本号]` 可直接调用已下载的版本；  
5. **自定义操作**：`n run` 运行指定版本的 Node.js，`n exec` 修改环境变量以使用特定版本的 `node`/`npm`。  

**主要特性**：  
- **跨平台支持**：兼容 macOS、Linux（含 WSL）及 Apple Silicon 芯片；  
- **缓存机制**：下载的版本会保存至缓存目录，便于重复使用；  
- **保留 npm**：安装时可通过 `--preserve` 保留当前 `npm` 版本，避免降级；  
- **自定义镜像**：支持通过 `N_NODE_MIRROR` 环境变量切换 Node.js 下载源（如国内镜像）；  
- **架构适配**：自动识别系统架构（如 x64、arm64），支持手动指定（如 `--arch x64`）；  
- **环境变量控制**：通过 `N_PREFIX` 自定义安装路径，`N_USE_XZ` 控制压缩格式等。