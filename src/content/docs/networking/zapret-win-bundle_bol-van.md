
---
title: zapret-win-bundle
---

### [bol-van zapret-win-bundle](https://github.com/bol-van/zapret-win-bundle)  ![GitHub Repo stars](https://img.shields.io/github/stars/bol-van/zapret-win-bundle?style=social)

这是一个专为 Windows 平台设计的深包检测（DPI）绕过工具包。核心功能在于整合 zapret1 和 zapret2，利用 windivert 驱动拦截与修改网络流量以规避 DPI 审查。项目包含主程序（winws/winws2）、DPI 分析工具（blockcheck）、系统服务管理脚本及策略示例。支持 Windows 7 至 11/Server 系列（含 ARM64），部分版本需特殊配置（如测试签名模式）。该工具非一键式解决方案，需理解工作原理，需管理员权限运行，且杀毒软件可能误报 windivert 驱动。