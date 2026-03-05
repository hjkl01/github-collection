
---
title: websockify
---

### [novnc websockify](https://github.com/novnc/websockify)  ![GitHub Repo stars](https://img.shields.io/github/stars/novnc/websockify?style=social)

websockify 是一个为任意应用程序或服务器提供 WebSockets 支持的代理工具。其核心功能是将 WebSockets 流量转换为普通套接字流量，并在客户端与目标之间进行双向转发。

主要功能包括：
1. **加密连接**：支持通过 SSL/TLS 证书启用加密的 WebSocket 连接（wss://）。
2. **程序包装**：可启动本地程序并代理流量至其端口，支持程序退出或守护进程处理策略。
3. **扩展功能**：支持守护进程运行、会话录制、同端口内置 Web 服务器、日志记录、认证插件及基于令牌的多目标路由。
4. **多环境部署**：支持直接安装及 Docker/Podman 容器化运行。