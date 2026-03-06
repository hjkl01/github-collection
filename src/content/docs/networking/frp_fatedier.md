
---
title: frp
---

### [fatedier frp](https://github.com/fatedier/frp)  ![GitHub Repo stars](https://img.shields.io/github/stars/fatedier/frp?style=social)

frp 是一个快速反向代理工具，用于将位于 NAT 或防火墙后的本地服务器暴露至互联网。它支持 TCP、UDP、HTTP、HTTPS 协议以及 P2P 连接模式。系统架构分为服务端（frps）和客户端（frpc）。

核心功能包括：
1. **配置管理**：支持 TOML、YAML、JSON 格式，支持配置热加载和环境变量。
2. **安全与认证**：支持 Token 和 OIDC 认证，提供传输加密（TLS、KCP、QUIC）及压缩。
3. **监控与运维**：内置服务器仪表盘（Dashboard）、Prometheus 监控、服务健康检查。
4. **流量控制**：支持负载均衡、带宽限制、端口复用及 HTTP Host Header 重写。
5. **扩展能力**：提供丰富的客户端插件（如 Unix Domain Socket、静态文件、HTTP/HTTPS 代理）和服务器端管理插件。
6. **高级功能**：支持 SSH 隧道网关、虚拟网络（VirtualNet）及 URL 路由。