
---
title: wstunnel
---

### [erebe wstunnel](https://github.com/erebe/wstunnel)  ![GitHub Repo stars](https://img.shields.io/github/stars/erebe/wstunnel?style=social)

wstunnel 是一个基于 Rust 开发的高性能网络隧道工具，旨在利用 WebSocket 或 HTTP2 协议绕过防火墙和代理限制。它支持 TCP、UDP、Unix socket、Stdio 的静态隧道转发，以及 Socks5、HTTP 代理和透明代理的动态隧道功能。项目提供客户端和服务端独立二进制文件，支持 TLS/HTTPS 加密、mTLS 双向认证、证书自动重载及 IPv6。通过流量伪装，它可用于 SSH 代理、Wireguard 穿透及访问受限网络资源。