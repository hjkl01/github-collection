
---
title: wstunnel
---

### [erebe wstunnel](https://github.com/erebe/wstunnel)  ![GitHub Repo stars](https://img.shields.io/github/stars/erebe/wstunnel?style=social)

wstunnel 是一款基于 Rust 开发的网络隧道工具，利用 WebSocket 协议兼容 HTTP 的特性来绕过防火墙和代理限制。它支持 TCP、UDP、Unix socket 及 Stdio 的静态转发，Socks5、HTTP 代理及透明代理的动态转发，同时具备反向隧道功能。项目核心特性涵盖 TLS/HTTPS 及 mTLS 认证、证书自动重载、IPv6 支持、WebSocket 与 HTTP2 传输协议。提供独立静态二进制文件，无需安装依赖。适用于 SSH 代理、企业网络穿透、Wireguard 流量隐蔽及透明代理等场景，并支持自定义配置以优化流量隐蔽性。