
---
title: NanaZip
---

### [M2Team NanaZip](https://github.com/M2Team/NanaZip)  ![GitHub Repo stars](https://img.shields.io/github/stars/M2Team/NanaZip?style=social)

NanaZip 是一款基于 7-Zip 开发的面向现代 Windows 体验的开源文件归档工具。

**主要功能：**
- **界面与体验**：支持深色模式、Mica 效果、多 DPI 感知及国际化（i18n）；提供智能解压与解压后打开文件夹选项。
- **系统集成**：支持 Windows 10/11 资源管理器右键菜单、文件关联、MSIX 打包及 7-Zip 执行别名。
- **压缩与格式**：继承 7-Zip 全部功能，支持多种扩展编解码器（如 Zstandard、Brotli、LZ4 等）及特殊归档格式（如 ROMFS、WASM、Electron Archive 等）。
- **安全与算法**：提供丰富的哈希算法（MD2-512、SHA 系列、EDON-R 等）；启用 CFG、CET、签名返回等安全缓解措施；支持策略机制（Policies）。
- **版本发布**：包含 NanaZip（现代 MSIX 版，功能完整）和 NanaZip Classic（便携 Win32 版，适用于 Server Core/PE 等环境，开发中）。

**系统要求：**
Windows 10 2004+ (Build 19041) 或 Server 2022+，支持 x86、x64 及 ARM64 架构。