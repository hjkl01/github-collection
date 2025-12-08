
---
title: EasyTier
---

### [EasyTier EasyTier](https://github.com/EasyTier/EasyTier)

### 项目核心内容总结

**项目功能**  
EasyTier 是一个基于 Rust 和 Tokio 的去中心化虚拟专用网络（VPN）解决方案，支持跨平台部署（Windows、macOS、Linux、FreeBSD、Android 等），提供安全的端到端加密（AES-GCM/WireGuard），可实现节点间直接通信或通过共享节点中转，适用于私有网络搭建和远程访问场景。

**使用方法**  
1. **安装方式**  
   - 下载预编译二进制文件（推荐）  
   - 通过 Cargo 安装（开发版）  
   - Docker 部署  
   - Linux 一键安装脚本  
   - macOS 使用 Homebrew  
   - OpenWrt 通过 Luci Web UI 安装  

2. **组网方式**  
   - **共享节点组网**：通过指定网络名称和密钥，节点自动发现并连接，无需手动配置路由。  
   - **去中心化组网**：指定节点 IP 启动网络，其他节点通过 `-p` 参数连接至已有节点扩展网络。  
   - **子网代理**：通过 `-n` 参数共享本地子网，实现跨节点网络互通。  
   - **WireGuard 集成**：启用 WireGuard 门户，允许 iOS/Android 设备通过 WireGuard 客户端接入网络。  

**主要特性**  
- **去中心化架构**：无需中心服务器，节点可直接通信或通过共享节点中转。  
- **跨平台支持**：兼容主流操作系统及嵌入式设备。  
- **高性能与安全**：支持 AES-GCM/WireGuard 加密，NAT 穿透技术优化网络连通性。  
- **子网代理**：自动同步子网路由信息，实现跨节点 IP 访问。  
- **零配置部署**：通过命令行参数快速启动网络，支持自托管公共共享节点。  
- **扩展性**：兼容 WireGuard 客户端，支持与现有网络工具（如 ZeroTier、TailScale）协同使用。  

**其他信息**  
- 许可证：LGPL-3.0  
- 赞助方：腾讯 EdgeOne、Langlang Cloud、RainCloud  
- 社区支持：Telegram 群组及 QQ 群（多个群号）