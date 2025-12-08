
---
title: etcher
---

### [balena-io etcher](https://github.com/balena-io/etcher)

**项目核心内容总结：**  
Etcher是一款用于安全、便捷地将操作系统镜像写入SD卡和USB驱动的工具，支持验证数据写入完整性，防止误操作写入硬盘，并支持Raspberry Pi设备的USB启动模式。  

**使用方法：**  
- **支持系统**：Linux（多数发行版，Intel 64位）、Windows 10及更高版本（Intel 64位）、macOS 10.13及以上（Intel和Apple Silicon）。  
- **安装方式**：  
  - Linux（Debian/Ubuntu）：通过`apt`安装`.deb`包；Redhat/Fedora使用`yum`安装`.rpm`包；Arch/Manjaro通过AUR安装。  
  - Windows：使用WinGet（`winget install balenaEtcher`）或Chocolatey（`choco install etcher`）。  
- **卸载方式**：对应平台使用`apt remove`、`yum remove`、`yay -R`、`winget uninstall`或`choco uninstall`命令。  

**主要特性**：  
- 防止误写硬盘，确保数据写入正确性；  
- 支持直接烧录Raspberry Pi设备（需USB启动模式）；  
- 提供多平台安装包及包管理器支持。