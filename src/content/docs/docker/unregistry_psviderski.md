
---
title: unregistry
---

### [psviderski unregistry](https://github.com/psviderski/unregistry)  ![GitHub Repo stars](https://img.shields.io/github/stars/psviderski/unregistry?style=social)

**项目核心内容总结：**

**功能**  
Unregistry 是一个轻量级容器镜像仓库，支持通过 SSH 直接将 Docker 镜像推送到远程服务器，无需依赖外部注册表。其核心功能是使用 `docker pussh` 命令，仅传输镜像的缺失层，提升推送效率。

**使用方法**  
1. 安装方式：支持 Homebrew、直接下载、Debian 包或通过 WSL（Windows 不直接支持）。  
2. 基础命令：`docker pussh [镜像名] [用户@服务器]`，支持 SSH 密钥、自定义端口（如 `user@server:2222`）、指定平台（如 `--platform linux/amd64`）。  
3. 高级用法：可运行独立的 Unregistry 实例作为本地镜像仓库，或通过自定义 SSH 配置文件简化操作。

**主要特性**  
- **无需中间注册表**：直接推送至远程服务器，减少依赖。  
- **高效传输**：仅传输镜像缺失的层，节省带宽和时间。  
- **兼容性**：支持多平台镜像、containerd 存储（避免重复存储），适用于 CI/CD、生产部署及隔离网络环境。  
- **灵活性**：支持自定义 SSH 选项、远程镜像版本控制等。

**注意事项**  
- 远程服务器需安装 Docker，且 SSH 用户需有 `docker` 权限（或 `sudo` 权限）。  
- 若需避免镜像重复存储，建议启用 containerd image store。  
- 首次使用需确保服务器可访问 `ghcr.io` 拉取 Unregistry 镜像。