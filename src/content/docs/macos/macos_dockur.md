
---
title: macos
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/dockur/macos?style=social) ](https://github.com/dockur/macos)
### [dockur macos](https://github.com/dockur/macos)

**项目核心内容总结**  

**功能**：该项目提供一个基于 Docker 的 macOS 容器镜像，支持通过 KVM 加速运行 macOS 系统，并可通过 Web 浏览器访问。  

**主要特性**：  
- 支持 KVM 加速和 Web 查看器；  
- 自动下载 macOS 安装镜像；  
- 支持自定义 macOS 版本（如 Sonoma、Ventura 等）；  
- 可调整磁盘大小、CPU 核心数、内存大小；  
- 支持通过 macvlan 网络分配独立 IP 地址；  
- 支持 USB 设备、磁盘传递及与宿主机文件共享；  
- 提供 Docker Compose、Docker CLI、Kubernetes 和 GitHub Codespaces 多种部署方式。  

**使用方法**：  
- 通过 Docker Compose 或 CLI 命令启动容器，配置环境变量（如 `VERSION`、`DISK_SIZE` 等）；  
- 使用 Kubernetes 部署需应用 YAML 文件；  
- GitHub Codespaces 可直接打开项目。  

**注意事项**：  
- 仅支持在 Apple 硬件上运行，违反 Apple EULA 的使用属于非法；  
- 部分功能（如多核 CPU 支持）需在安装后验证稳定性；  
- 需确保系统支持 KVM（如 Linux 环境需启用虚拟化扩展）。