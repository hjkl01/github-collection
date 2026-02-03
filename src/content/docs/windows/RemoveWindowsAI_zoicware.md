
---
title: RemoveWindowsAI
---

### [zoicware RemoveWindowsAI](https://github.com/zoicware/RemoveWindowsAI)  ![GitHub Repo stars](https://img.shields.io/github/stars/zoicware/RemoveWindowsAI?style=social)

**项目核心内容总结**  
该项目旨在移除Windows 11 25H2及后续版本中的AI功能，提升系统隐私、安全性和性能。主要功能包括：  
- **禁用AI功能**：移除Copilot、Recall、输入洞察、AI语音效果等AI组件，删除注册表项和系统策略。  
- **防止AI组件回滚**：通过自定义Windows Update包阻止AI组件重新安装。  
- **清理AI文件**：彻底删除AI应用包、CBS存储中的隐藏组件及残留文件。  
- **替换经典应用**：提供替换记事本、画图、截图工具等现代AI应用为经典版本的选项。  

**使用方法**  
- **PowerShell运行**：以管理员身份执行脚本，支持交互式界面或非交互模式（如`-nonInteractive`参数）。  
- **命令行选项**：通过参数控制功能（如`-Options`指定禁用项，`-InstallClassicApps`安装经典应用）。  
- **备份与回滚**：启用`-backupMode`可备份系统，`-revertMode`可恢复原设置。  

**注意事项**  
- 部分杀毒软件可能误报脚本为恶意程序，需临时关闭或设置排除。  
- 建议在虚拟机中测试脚本以避免系统风险。  
- 项目持续更新以适配微软新增AI功能，用户可提交新发现的AI组件以完善脚本。