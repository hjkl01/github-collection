
---
title: frp
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/fatedier/frp?style=social) ](https://github.com/fatedier/frp)
### [fatedier frp](https://github.com/fatedier/frp)

**项目核心内容总结：**

frp 是一个用于内网穿透的高性能反向代理应用，支持 TCP、UDP、HTTP、HTTPS 等多种协议。其主要功能是将内网服务通过公网服务器暴露到互联网，便于远程访问。

**主要特性：**
- 支持多种协议（TCP、UDP、HTTP、HTTPS）。
- 提供端口映射、虚拟网络（VirtualNet）、SSH 隧道网关等功能。
- 支持插件扩展，如 HTTP 代理、静态文件服务、SOCKS5 等。
- 支持端口范围映射，简化多个端口配置。
- 支持通过代理（如 HTTP_PROXY）连接服务器。
- 支持 TCP 端口复用（通过 HTTP CONNECT 方法）。
- 提供负载均衡、URL 路由、虚拟主机等功能。
- 支持功能开关（Feature Gates），用于控制实验性功能的启用或禁用。
- 提供轻量级客户端（tiny-frpc）适合资源受限设备使用。

**使用方法：**
- 部署 frps（服务端）和 frpc（客户端）。
- 配置 frpc.toml 和 frps.toml 文件，定义映射规则和连接信息。
- 启动服务端和客户端，即可实现内网服务的远程访问。

**适用场景：**
- 内网服务的远程访问。
- 企业内部系统对外提供服务。
- 跨网络的设备通信。

**项目特点：**
- 高性能、低延迟。
- 配置灵活，支持多种高级功能。
- 拥有丰富的插件生态和社区支持。
- 支持通过 SSH 建立隧道，实现无需客户端的代理。

---

**注意事项：**
- 需要根据实际网络环境配置防火墙和路由规则。
- 实验性功能（如 VirtualNet）默认禁用，需在配置中启用。
- 使用插件时需确保插件与 frp 版本兼容。