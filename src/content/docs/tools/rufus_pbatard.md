
---
title: rufus
---

### [pbatard rufus](https://github.com/pbatard/rufus)

Rufus 是一个用于格式化和创建可启动 USB 设备的工具，支持以下功能：  
- **格式化** USB、闪存卡等为 FAT/FAT32/NTFS 等多种文件系统；  
- **创建启动盘**，包括 BIOS/UEFI 启动、Windows/Linux 安装盘、Windows To Go 等；  
- **镜像操作**：生成 VHD/VHDX/DD/FFU 镜像，计算文件哈希值；  
- **其他功能**：检查坏块、下载 Windows 官方 ISO、支持持久化 Linux 分区等。  

**使用方法**：通过 Visual Studio 2022 或 MinGW 编译项目（使用 `.sln` 文件或 `configure/make` 命令）。  

**主要特性**：  
- 支持 38 种语言，界面友好；  
- 无需安装，便携运行；  
- 兼容 Secure Boot，开源（GPLv3 许可）；  
- 提供日志和调试信息，便于问题排查。