
---
title: zapret-win-bundle
---

### [bol-van zapret-win-bundle](https://github.com/bol-van/zapret-win-bundle)  ![GitHub Repo stars](https://img.shields.io/github/stars/bol-van/zapret-win-bundle?style=social)

### 项目核心内容总结

**项目名称**：zapret winws 窗体（zapret1 和 zapret2 的 Windows 合并版本）

**项目功能**：  
该项目是一个用于 Windows 的 DPI（深度数据包检测）绕过工具，结合了 zapret1 和 zapret2 两个版本，适用于绕过网络审查。项目包括一个最小化的 Cygwin 环境和 blockcheck 工具，用于检测和测试 DPI 绕过方法。

**使用方法**：  
- 需要管理员权限和系统配置调整（如禁用 Secure Boot、启用 TestSigning 模式等）。
- 包含多个 `.cmd` 脚本用于启动示例策略、安装服务、管理 Windivert 驱动等。
- 使用 `blockcheck` 工具分析 DPI 检测方式，但必须在关闭所有绕过工具的情况下运行。
- 提供了针对不同 Windows 版本的配置脚本（如 WIN7、ARM64 等）。

**主要特性**：  
- 支持 Windows 7 x64、Windows 8+、Windows 11 ARM64 等系统（需特定设置）。
- 使用 Windivert 驱动实现网络包过滤，类似 Linux 的 iptables。
- 包含 winws.exe（zapret1）和 winws2.exe（zapret2）两个核心组件。
- 提供服务模式和交互式模式。
- 需要用户具备一定网络和系统知识，不是一键式解决方案。

**注意事项**：  
- Windivert 可能被杀毒软件误报，需设置白名单或暂时禁用杀毒软件。
- 安装前需确保系统满足要求，如启用测试模式、安装无线网络功能等。
- 项目不提供“一键打开网站”功能，需自行配置策略。