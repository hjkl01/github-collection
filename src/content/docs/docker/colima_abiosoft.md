
---
title: colima
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/abiosoft/colima?style=social) ](https://github.com/abiosoft/colima)
### [abiosoft colima](https://github.com/abiosoft/colima)

**项目核心内容总结：**  

Colima 是一个在 macOS 和 Linux 上运行容器的工具，支持 Intel 和 Apple Silicon 设备，提供最小化设置的容器运行时环境。  

**主要功能：**  
- 支持多种容器运行时：Docker（含 Kubernetes）、Containerd（含 Kubernetes）、Incus（支持容器和虚拟机）。  
- 自动端口转发、卷挂载、多实例管理。  
- 支持自定义虚拟机配置（CPU、内存、磁盘大小）。  
- 提供 CLI 界面，通过 `colima start` 快速启动，默认使用 Docker 运行时。  

**使用方法：**  
1. **安装**：支持 Homebrew、MacPorts、Nix、Mise 等方式（如 `brew install colima`）。  
2. **启动**：直接运行 `colima start`，或通过 `--runtime` 参数指定运行时（如 `--runtime containerd`）。  
3. **配置**：使用 `colima start --edit` 编辑配置文件，或通过 `colima template` 修改模板。  
4. **Kubernetes**：启动时添加 `--kubernetes` 参数启用。  

**注意事项：**  
- 从 v0.5.6 升级需先删除旧实例（`colima delete`）。  
- Incus 运行时需 macOS Ventura（13）及以上版本支持 Rosetta 2。  
- 磁盘大小可从 v0.5.3 版本起动态调整。  

**项目目标**：简化 macOS 上容器运行时的部署与管理。