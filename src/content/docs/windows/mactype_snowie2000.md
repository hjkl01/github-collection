
---
title: mactype
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/snowie2000/mactype?style=social) ](https://github.com/snowie2000/mactype)
### [snowie2000 mactype](https://github.com/snowie2000/mactype)

**核心内容总结：**  
MacType 是一款为 Windows 提供更优字体渲染的工具，支持 Win11 和 CET（中文语言包）。主要特性包括：  
- 支持彩色字体、改进 DirectWrite 渲染、多显示器适配；  
- 新安装程序、降低托盘模式 CPU 占用、优化多语言（含简体中文、繁体中文、韩语等）；  
- 支持通过服务模式避免杀毒软件冲突，修复 Office 2013 兼容性问题；  
- 提供官方网站下载（http://www.mactype.net）和捐赠渠道。  

**使用方法：**  
1. 从 GitHub 发布页面下载最新版本；  
2. 安装后通过配置文件调整参数（如 DirectWrite=0、HookChildProcesses=0）；  
3. 需注意升级前备份配置文件，避免语言选项缺失或与第三方软件（如 WPS）冲突。  

**注意事项：**  
- 部分语言选项可能因翻译文件缺失不完整；  
- 64 位系统需启用服务模式或关闭 HookChildProcesses 以避免杀毒软件拦截；  
- Office 2013 不兼容，建议使用 Office 2010 或 2016+；  
- WPS 会自动卸载 MacType，需通过 Wiki 提供的解决方案修复。