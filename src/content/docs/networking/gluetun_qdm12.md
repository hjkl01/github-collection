
---
title: gluetun
---

### [qdm12 gluetun](https://github.com/qdm12/gluetun)  ![GitHub Repo stars](https://img.shields.io/github/stars/qdm12/gluetun?style=social)

**项目核心内容总结：**  

**项目功能**  
Gluetun 是一个轻量级的多协议 VPN 客户端，支持 OpenVPN 和 WireGuard 协议，兼容 40+ VPN 服务商（如 NordVPN、ExpressVPN、Private Internet Access 等）。内置 DNS over TLS、广告过滤、防火墙杀开关、Shadowsocks 代理和 HTTP 代理功能，支持自定义端口转发及多 DNS 提供商分流。  

**使用方法**  
通过 Docker 部署，提供 `docker-compose.yml` 示例，需配置环境变量（如 VPN 服务商、账户信息）并挂载存储卷。支持多种架构（amd64、ARM、PPC 等），可作为 Kubernetes 侧车容器使用。  

**主要特性**  
- 基于 Alpine Linux，Docker 镜像仅 41.1MB；  
- 支持 WireGuard（部分服务商）和 OpenVPN；  
- 内置广告/恶意域名过滤，DNS 阻止功能每日更新；  
- 支持 LAN 设备及容器联网，提供端口转发配置；  
- 兼容多平台，适配主流硬件架构。  

**其他**  
项目托管于 GitHub，提供 Wiki 文档和常见问题解答，采用 MIT 许可证。