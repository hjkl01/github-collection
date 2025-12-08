
---
title: mullvadvpn-app
---

### [mullvad mullvadvpn-app](https://github.com/mullvad/mullvadvpn-app)

**核心内容总结：**  
Mullvad VPN App 是一款开源的隐私保护型虚拟私人网络（VPN）客户端，采用 Rust 和 Electron 等技术开发，支持多平台（Windows、Linux、macOS、Android、iOS）。其核心功能包括：  
1. **隐私与匿名性**：通过 `talpid` 库实现的通用隐私保护型 VPN 客户端，不依赖 Mullvad 专有信息（如账户 API 或服务器列表）。  
2. **模块化架构**：分为 `talpid`（通用 VPN 功能）和 `mullvad`（Mullvad 特定功能）两部分，代码结构清晰，包含桌面应用（Electron + React）、后台守护进程（Rust 编写的 `mullvad-daemon`）及打包工具。  
3. **配置与使用**：支持通过环境变量（如 `MULLVAD_SETTINGS_DIR`）自定义设置、日志、缓存路径；提供图形界面（GUI）和命令行界面（CLI）两种控制方式。  
4. **开源与合规**：源代码遵循 GPL-3 许可证，但 iOS 版本在 Apple App Store 上采用 Apple 的 EULA 协议。  
5. **安全审计**：通过第三方渗透测试和安全审查，确保代码安全性，相关报告可在 `audits/` 目录中查阅。  

**主要特性**：  
- 支持多平台部署与跨系统兼容性；  
- 提供详细的文件路径配置和日志管理；  
- 使用模块化设计，便于扩展和维护；  
- 包含图形界面、命令行工具及系统服务集成。