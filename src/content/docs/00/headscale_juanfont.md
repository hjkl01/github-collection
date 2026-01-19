
---
title: headscale
---

### [juanfont headscale](https://github.com/juanfont/headscale)  ![GitHub Repo stars](https://img.shields.io/github/stars/juanfont/headscale?style=social)

**项目简介**  
Headscale 是一个开源的、自托管的 Tailscale 控制服务器实现，旨在为个人用户和小型开源组织提供替代 Tailscale 服务的解决方案。它基于 WireGuard 构建，支持节点密钥交换、IP 分配、用户边界划分和路由共享等功能。

**功能与使用方法**  
- **核心功能**：管理 Tailscale 网络（tailnet），实现节点间的安全通信，支持多用户协作和路由共享。  
- **运行方式**：通过官方文档（[稳定版](https://headscale.net/stable/) 或 [开发版](https://headscale.net/development/)）部署，NixOS 用户可使用提供的模块（`nix/` 目录）。  
- **开发与测试**：需安装 Go、Buf 和 Protobuf 工具，推荐使用 `nix develop` 管理依赖，通过 `make test` 和 `make build` 进行测试和构建。

**主要特性**  
- **开源免费**：除 Tailscale 官方 GUI 客户端外，所有代码均开放。  
- **轻量级设计**：仅支持单个 Tailscale 网络，适合个人或小型团队使用。  
- **兼容性**：支持主流操作系统客户端，具体可参考文档。  
- **社区驱动**：由社区维护，部分贡献者来自 Tailscale 公司但遵循开源原则。

**注意事项**  
- 不支持通过反向代理或容器运行 Headscale。  
- 文档与代码版本需严格对应，避免使用 `main` 分支的未发布功能。