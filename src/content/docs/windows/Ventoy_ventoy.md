
---
title: Ventoy
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/ventoy/Ventoy?style=social) ](https://github.com/ventoy/Ventoy)
### [ventoy Ventoy](https://github.com/ventoy/Ventoy)

**Ventoy核心内容总结：**

Ventoy是一款开源工具，用于创建可启动USB驱动器，支持ISO/WIM/IMG/VHD(x)/EFI等文件类型。其核心功能包括：
- **无需反复格式化**：只需将镜像文件复制到USB设备，即可生成启动菜单并直接引导安装。
- **广泛兼容性**：支持MBR/GPT分区、x86/UEFI/ARM64架构、Secure Boot，兼容Windows/Linux等主流系统。
- **高级特性**：支持Linux持久化存储、Windows/Linux自动安装、菜单自定义（主题/提示信息/密码保护）、运行时文件注入、动态替换配置文件。
- **灵活安装**：可安装于USB/SSD/NVMe/SD卡等设备，不影响设备正常使用，升级时数据不丢失。
- **多平台支持**：涵盖1200+测试镜像，支持浏览本地磁盘文件并引导，提供插件框架（如VentoyPlugson图形化配置器）。

**使用方法**：  
1. 通过官方文档（[安装指南](https://www.ventoy.net/en/doc_start.html)）安装Ventoy到目标设备。  
2. 将ISO等镜像文件复制到设备，重启后通过启动菜单选择对应系统安装。  
3. 高级功能需配合插件配置（如自定义主题、自动安装脚本等）。