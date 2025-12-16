
---
title: Microsoft-Activation-Scripts
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/massgravel/Microsoft-Activation-Scripts?style=social) ](https://github.com/massgravel/Microsoft-Activation-Scripts)
### [massgravel Microsoft-Activation-Scripts](https://github.com/massgravel/Microsoft-Activation-Scripts)

**项目功能**：  
Microsoft Activation Scripts (MAS) 是一款开源工具，支持通过 HWID、Ohook、TSforge、在线 KMS 等方法激活 Windows、Office 及扩展更新（ESU），并提供高级故障排除功能。

**使用方法**：  
1. **PowerShell 方法**（适用于 Windows 7/8/10/11）：  
   - 执行 `irm https://get.activated.win | iex`（若被 ISP/DNS 阻挡，可使用 DoH 替代命令）。  
   - 激活菜单出现后，选择绿色高亮选项完成激活。  
2. **传统方法**（适用于 Vista 及以上版本）：  
   - 下载并运行 `MAS_AIO.cmd` 文件，按提示操作。  

**主要特性**：  
- 支持多种激活方式（HWID/KMS 等）及多版本 Windows/Office。  
- 提供无网络依赖的离线激活选项。  
- 包含故障排除指南及命令行参数支持（如无人值守模式）。  

**注意事项**：  
- 执行 PowerShell 命令前需验证 URL 安全性，避免恶意软件伪装。  
- 若网络被封锁，可通过启用 DNS-over-HTTPS（如 1.1.1.1）绕过限制。  
- 部分产品（如 macOS Office、Windows XP）需参考额外激活链接。  

**版本信息**：3.9（2025 年 11 月 19 日发布）。