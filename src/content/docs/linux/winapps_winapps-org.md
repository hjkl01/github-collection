
---
title: winapps
---

### [winapps-org winapps](https://github.com/winapps-org/winapps)  ![GitHub Repo stars](https://img.shields.io/github/stars/winapps-org/winapps?style=social)

WinApps 是一个允许在 GNU/Linux 系统（支持 KDE Plasma、GNOME、XFCE 等）上无缝运行 Windows 应用程序的工具。

主要功能：
1. **跨平台运行**：在 Linux 主机上以原生体验运行 Windows 应用（包括 Microsoft 365、Adobe Creative Cloud 等），支持除内核级反作弊系统外的所有 Windows 应用。
2. **底层机制**：通过 Docker、Podman 或 libvirt 管理 Windows 虚拟机，利用 FreeRDP 后端将应用渲染至 Linux 桌面。
3. **系统集成**：自动创建应用快捷方式，支持文件类型关联（基于 MIME 类型调用 Windows 应用），并实现 Linux 与 Windows 文件系统的互访。
4. **管理工具**：提供可选的 WinApps Launcher 用于管理虚拟机状态及应用启动。
5. **多方式安装**：支持常规脚本安装及 Nix/NixOS 环境部署。