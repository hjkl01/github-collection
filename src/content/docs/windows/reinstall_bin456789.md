
---
title: reinstall
---

### [bin456789 reinstall](https://github.com/bin456789/reinstall)  ![GitHub Repo stars](https://img.shields.io/github/stars/bin456789/reinstall?style=social)

这是一个一键 VPS 系统重装脚本，核心功能总结如下：

1.  **系统重装**：支持 Linux（19 种常见发行版）和 Windows（Vista 至 2025）的一键重装，支持任意方向转换（如 Linux 转 Windows）。
2.  **驱动与镜像**：Windows 安装使用官方原版 ISO，自动查找链接并安装 VirtIO 等公有云驱动；支持 DD Raw 镜像写入硬盘。
3.  **网络配置**：自动设置 IP，智能识别动态/静态，支持 /32、/128、网关不在子网、纯 IPv6 及 IPv4/IPv6 多网卡配置。
4.  **兼容性**：专为低配服务器优化（内存占用少），支持 BIOS/EFI 引导及 ARM 服务器。
5.  **安全性**：使用分区表 ID 识别硬盘，确保不写错硬盘；所有资源实时从镜像源获取，无自制包。
6.  **扩展功能**：支持重启至 Alpine Live OS 或 netboot.xyz 进行手动维护（不删除数据）。

注意：不支持 OpenVZ、LXC 虚拟机。