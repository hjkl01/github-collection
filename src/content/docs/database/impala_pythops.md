
---
title: impala
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/pythops/impala?style=social) ](https://github.com/pythops/impala)
### [pythops impala](https://github.com/pythops/impala)

**项目核心内容总结：**  
Impala 是一款用于管理 WiFi 的终端用户界面工具（TUI），支持以下功能：  
- **核心特性**：支持 WPA 企业版（802.1X）认证、Station（站点）模式与 Access Point（热点）模式切换、通过 QR 码共享网络。  
- **使用方法**：  
  - **安装**：可通过二进制文件、`crates.io`、Arch Linux 官方仓库、Nixpkgs 或从源码编译安装（需 `cargo` 和 `git`）。  
  - **操作**：使用键盘快捷键（如 `Tab` 切换界面、`j/k` 滚动、`Ctrl+R` 切换模式等）管理网络，支持扫描、连接、共享网络等操作。  
  - **配置**：通过 `~/.config/impala/config.toml` 自定义快捷键和行为。  
- **要求**：需在 Linux 系统上运行，依赖 `iwd` 服务，需禁用 `NetworkManager` 或 `wpa_supplicant` 以避免冲突。  
- **许可证**：遵循 GPLv3 协议。