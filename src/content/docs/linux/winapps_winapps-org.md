
---
title: winapps
---

### [winapps-org winapps](https://github.com/winapps-org/winapps)

**项目核心内容总结：**

**功能：**  
WinApps 是一个在 Linux 系统上运行 Windows 应用的工具，通过 RDP 连接 Windows 虚拟机或容器，支持安装、管理和启动预定义应用，提供命令行和图形化操作界面。

**使用方法：**  
1. 安装：通过脚本安装（`bash <(curl ...)`）或 Nix 包管理器安装。  
2. 配置：创建 Windows 虚拟机，运行安装程序配置应用。  
3. 启动应用：使用 `winapps` 命令或图形化工具（可选）启动应用或桌面会话。  
4. 手动运行：通过 `winapps manual` 启动未预定义的 Windows 可执行文件。  
5. 更新：重新运行安装程序更新 WinApps。

**主要特性：**  
- 支持虚拟机（如 KVM）、容器（如 Docker）等后端。  
- 提供自定义应用配置（图标、MIME 类型）并支持社区贡献。  
- 可选图形化工具（系统托盘菜单）管理 Windows 会话和应用。  
- 支持 Nix 安装（包括 NixOS 和 standalone 模式）。  
- 自动处理 RDP 证书，确保连接安全。