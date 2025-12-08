
---
title: archinstall
---

### [archlinux archinstall](https://github.com/archlinux/archinstall)

**核心内容总结：**  

**项目功能：**  
`archinstall` 是一个用于安装 Arch Linux 的引导式/自动化安装工具，同时提供 Python 库功能，支持在安装后管理服务、软件包等系统配置（通常从 Live 环境运行）。  

**使用方法：**  
1. **安装方式：**  
   - 通过 `pacman` 安装：`pacman -Sy archinstall`  
   - 通过 `pip` 安装：`pip install --upgrade archinstall`  
   - 克隆仓库后运行：`python -m archinstall`  

2. **运行安装：**  
   - 直接运行 `archinstall`（需在 Live ISO 或已安装系统中使用）。  
   - 使用配置文件安装：`archinstall --config <配置文件路径或URL> --creds <凭证文件路径或URL>`。  

3. **高级功能：**  
   - 支持通过 `--advanced` 参数启用高级选项。  
   - 可生成配置文件（通过安装过程保存）。  

**主要特性：**  
- **多语言支持：** 提供多种语言界面（需手动设置字体以支持非拉丁字符）。  
- **配置文件加密：** 用户凭证（如密码）默认使用 `yescrypt` 哈希存储，可选择加密存储。  
- **预设配置文件：** 提供桌面和服务器安装的默认配置（如软件包选择）。  
- **脚本化安装：** 支持交互式和完全自动化的脚本安装（示例脚本可参考仓库）。  
- **日志与调试：** 安装日志存储于 `/var/log/archinstall/install.log`，便于问题排查。  

**其他：**  
- 提供中文等多语言支持（需手动选择）。  
- 支持通过 QEMU 等工具在本地测试安装流程。