
---
title: quickemu
---

### [quickemu-project quickemu](https://github.com/quickemu-project/quickemu)  ![GitHub Repo stars](https://img.shields.io/github/stars/quickemu-project/quickemu?style=social)

**Quickemu 项目总结**

**核心功能**
基于 QEMU 的自动化工具，旨在无需繁琐配置即可快速创建和运行优化后的 Windows、macOS 及 Linux 虚拟机。

**使用方法**
1.  **下载与配置**：使用 `quickget` 命令自动下载操作系统 ISO 镜像并生成虚拟机配置文件。
2.  **启动虚拟机**：使用 `quickemu` 命令加载配置文件，自动检测硬件并启动虚拟机。

**主要特性**
*   **广泛支持**：支持 Windows 10/11/Server、macOS (多个版本)、Ubuntu 及近 1000 种 Linux 发行版，以及 BSD 等系统。
*   **架构兼容**：支持 x86_64 和 ARM64 来宾系统（ARM 宿主机上原生运行，x86 宿主机上模拟）。
*   **硬件与性能**：支持 USB 及智能卡直通、VirGL 图形加速、全双工音频、网络端口转发及 SSH 端口转发。
*   **交互与共享**：支持 SPICE 协议（含剪贴板共享）、VirtIO-webdav/9p 及 Samba 文件共享。
*   **启动与安全**：支持 TPM 2.0、EFI (含安全启动) 及传统 BIOS 启动，包含 QEMU Guest Agent 支持。

**宿主机环境**
支持 Linux 和 macOS 系统。