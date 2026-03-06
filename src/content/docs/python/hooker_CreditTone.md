
---
title: hooker
---

### [CreditTone hooker](https://github.com/CreditTone/hooker)  ![GitHub Repo stars](https://img.shields.io/github/stars/CreditTone/hooker?style=social)

Hooker 是一个基于 Frida 实现的 Android 逆向分析工具包，旨在为开发者提供舒适的命令行交互体验。核心功能包括：

1. **自动化脚本生成**：支持 1 秒内根据类名和方法名自动生成带详细备注和堆栈追踪的 Frida Hook 脚本。
2. **证书校验绕过**：内置 Frida 版 JustTrustMe 及 boringssl unpinning 脚本，通杀全网 App 的 SSL Pinning。
3. **便捷网络代理**：通过命令行快捷设置 Socks5 代理，实现应用层无感知流量转发。
4. **调试环境管理**：自动管理目标应用工作目录，支持脚本列表、attach/spawn 执行、文件拉取、应用重启及进程信息查询。
5. **安全对抗与探测**：提供绕过 Root、Frida Server、VPN 检测的脚本，支持内存漫游探测 Activity/Service 及反调试 SO 库识别。
6. **辅助分析工具**：集成 R0Capture SSL 抓包、自动脱壳（Dump Dex）、加密算法 Hook、WebView 调试、设备指纹获取及 APK 加壳扫描。
7. **环境配置与更新**：自动部署 Frida-server，支持 Linux/Mac 原生运行，Windows 需配合 WSL 使用，支持项目一键升级。