
---
title: quickemu
---

### [quickemu-project quickemu](https://github.com/quickemu-project/quickemu)  ![GitHub Repo stars](https://img.shields.io/github/stars/quickemu-project/quickemu?style=social)

Quickemu 是一个基于 QEMU 的封装工具，旨在简化 Windows、macOS 和 Linux 虚拟机的创建与运行，无需繁琐的手动配置。其核心功能包括：

1.  **自动化配置**：`quickget` 命令自动下载操作系统镜像并生成配置文件，`quickemu` 命令根据主机硬件自动枚举并启动最优配置的虚拟机。
2.  **广泛支持**：支持近 1000 种操作系统，包括 Windows 10/11/Server、macOS 多个版本、Linux 发行版及 BSD 等，支持 ARM64 客户机。
3.  **丰富特性**：提供 SPICE 远程访问、剪贴板共享、多种文件共享（VirtIO/Samba）、USB 及智能卡透传、SSH 端口转发、双工音频和 EFI/Legacy BIOS 启动。
4.  **灵活部署**：主机支持 Linux 和 macOS，虚拟机配置可存储于任意位置，无需提升权限即可运行。