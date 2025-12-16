
---
title: Win11Debloat
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/Raphire/Win11Debloat?style=social) ](https://github.com/Raphire/Win11Debloat)
### [Raphire Win11Debloat](https://github.com/Raphire/Win11Debloat)

**项目核心内容总结：**  
Win11Debloat 是一个用于优化 Windows 11/10 系统的工具，核心功能包括卸载预装的冗余软件、调整系统设置以提升性能。主要特性：  
1. **卸载预装应用**：默认移除 Microsoft 和第三方的大量预装软件（如 Microsoft 3D Builder、Skype、Netflix 等），部分应用需用户手动选择。  
2. **系统优化**：禁用快速启动、自动更新、后台数据传输等功能，调整文件资源管理器显示设置（如隐藏“3D 对象”文件夹），优化任务栏和锁屏界面。  
3. **自定义配置**：支持通过修改配置文件选择性卸载应用或调整设置，提供详细的日志记录。  
4. **兼容性**：支持 Windows 10 和 11，部分功能区分版本处理（如 Edge 浏览器仅在 EEA 区域可卸载）。  

**使用方法**：  
- 通过 PowerShell 或命令行运行脚本，需管理员权限。  
- 安装后根据提示选择卸载选项或修改配置文件。  
- 部分功能（如禁用 Fast Startup）需重启生效。  

**注意事项**：  
- 卸载 Microsoft Store、OneDrive 等关键应用可能导致系统功能异常，需谨慎操作。  
- 部分预装应用（如 Xbox 相关工具）为游戏或特定功能依赖项，卸载前需确认需求。