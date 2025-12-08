
---
title: linuxdeploy
---

### [meefik linuxdeploy](https://github.com/meefik/linuxdeploy)

Linux Deploy 是一款用于在 Android 设备上安装和运行 GNU/Linux 操作系统的开源工具。其核心功能包括：通过创建磁盘镜像、目录、分区或 RAM 安装 Linux 发行版（如 Alpine、Arch、Ubuntu 等），支持 ext2/ext3/ext4 文件系统及 arm/x86 等架构。安装后可在 chroot 环境中运行系统应用，并通过 SSH/VNC 等方式控制。主要特性包括多语言界面、自动密码生成、安装过程可视化、支持自定义脚本及服务管理。使用时需从官方镜像下载系统文件，推荐磁盘镜像大小为 1024MB（带 GUI）或 512MB（无 GUI），部分功能需 root 权限。安装过程约需 15 分钟，所有操作可逆，支持卸载。