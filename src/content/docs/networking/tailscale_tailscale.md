
---
title: tailscale
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/tailscale/tailscale?style=social) ](https://github.com/tailscale/tailscale)
### [tailscale tailscale](https://github.com/tailscale/tailscale)

**Tailscale 核心内容总结**  

**项目功能**  
Tailscale 是一个用于创建私有 WireGuard 网络的开源工具，提供 `tailscaled` 守护进程和 `tailscale` 命令行工具，支持 Linux、Windows、macOS、FreeBSD 和 OpenBSD 等平台。iOS 和 Android 应用使用其代码，但不包含移动 GUI。  

**使用方法**  
- 通过 [https://pkgs.tailscale.com](https://pkgs.tailscale.com/) 获取各平台预编译包。  
- 使用 `go install tailscale.com/cmd/tailscale{,d}` 安装（需 Go 1.25）。  
- 打包发行版时，使用 `build_dist.sh` 生成带版本信息的二进制文件。  

**主要特性**  
- 跨平台支持（含桌面和部分 BSD 系统）。  
- 开源代码包含核心功能，但移动应用 GUI 非开源。  
- 提供 Android、Synology、QNAP 等第三方集成仓库。