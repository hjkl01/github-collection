
---
title: shadowsocks-rust
---

### [shadowsocks shadowsocks-rust](https://github.com/shadowsocks/shadowsocks-rust)  ![GitHub Repo stars](https://img.shields.io/github/stars/shadowsocks/shadowsocks-rust?style=social)

shadowsocks-rust 是 Shadowsocks 协议的 Rust 语言实现，用于提供绕过防火墙的快速隧道代理服务。主要功能包括：

1. **核心工具**：提供 sslocal（客户端）、ssserver（服务端）、ssmanager（管理端）等二进制工具。
2. **代理模式**：支持 SOCKS5、HTTP、Tunnel、透明代理（Redir）、TUN 接口及 DNS 代理等多种模式。
3. **安全与扩展**：支持多种加密算法（含 AEAD-2022）、插件机制（SIP003/2022）、ACL 访问控制及在线配置更新。
4. **网络特性**：具备多服务器负载均衡、自动延迟检测及 HTTP/HTTPS 代理协议支持。
5. **部署支持**：跨平台兼容（Linux、macOS、Windows、BSD 等），支持 Docker 容器及 Kubernetes 部署。