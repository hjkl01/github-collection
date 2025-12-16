
---
title: optimizer
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/hellzerg/optimizer?style=social) ](https://github.com/hellzerg/optimizer)
### [hellzerg optimizer](https://github.com/hellzerg/optimizer)

**项目核心内容总结：**  
Optimizer 是一款用于提升 Windows 系统隐私与安全的配置工具，主要功能包括：  
- **系统优化**：禁用冗余服务（如 Windows 茶叶、Cortana）、停止自动更新、卸载 UWP 应用、清理系统垃圾。  
- **隐私保护**：关闭 Office 茶叶、禁用 OneDrive、CoPilot AI，移除硬件信息追踪。  
- **网络配置**：快速切换 DNS 服务器、Flush DNS 缓存、Ping IP 及 SHODAN.io 侦查。  
- **高级功能**：编辑 HOSTS 文件、系统变量路径、终止文件锁定进程、启用 UTC 时间。  

**使用方法**：  
1. 下载最新版本（[Releases 页面](https://github.com/hellzerg/optimizer/releases)）并运行 `.exe` 文件。  
2. 支持命令行参数（如 `/disabledefender` 禁用 Defender，`/restart=xxx` 自动执行操作）。  
3. 通过模板文件实现自动化配置（详见 [自动化指南](https://github.com/hellzerg/optimizer/blob/master/AUTOMATION.md)）。  

**主要特性**：  
- 支持 24 种语言，兼容 Windows 7 至 11 及服务器版本（需 `/unsafe` 开关）。  
- 提供系统性能优化、启动项管理、注册表修复等工具。  
- 社区贡献翻译及扩展功能（如 Discord 论坛、PayPal 捐赠支持）。