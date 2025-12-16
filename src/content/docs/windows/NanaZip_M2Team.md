
---
title: NanaZip
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/M2Team/NanaZip?style=social) ](https://github.com/M2Team/NanaZip)
### [M2Team NanaZip](https://github.com/M2Team/NanaZip)

**NanaZip 项目核心内容总结：**  

**项目功能**  
NanaZip 是基于 7-Zip 的开源压缩工具，支持 ZIP、7z 等多种格式的文件压缩与解压，提供图形化界面（XAML）和命令行两种使用方式。  

**主要特性**  
1. **跨平台支持**：兼容 Windows 10 2004 及以上版本、Windows Server 2022，支持 x86/x64 和 ARM64 架构。  
2. **安装方式灵活**：可通过 Microsoft Store 安装稳定版或预览版，也可下载 MSIX 包手动安装，支持批量部署（需管理员权限）。  
3. **兼容性优化**：提供 7-Zip 执行别名，便于用户迁移；支持 Windows PE/RE 环境的便携版（NanaZip Classic）。  
4. **安全性增强**：从 3.0 版起需联网验证赞助版授权状态，安装时需开启防火墙。  

**使用方法**  
- **Microsoft Store**：搜索“NanaZip”或“NanaZip Preview”安装。  
- **MSIX 包**：下载后双击安装，或通过 PowerShell/DISM 命令行部署。  
- **便携版**：适用于服务器核心系统或无 Store 环境。  

**已知问题**  
- 右键菜单需重启资源管理器；Windows 10 的 `%AppData%` 路径文件操作会被重定向。  
- 安装失败可能与防火墙或 Store 授权策略相关。  
- ARM64 系统需使用 WinPE 25398+ 镜像以支持 x64 模拟。  

**系统要求**  
- Windows 10 2004（19041）或更高版本，Windows Server 2022（20348）或更高版本。  
- 不支持非 Windows 平台（除 Wine 9.x 和 ReactOS 测试环境）。