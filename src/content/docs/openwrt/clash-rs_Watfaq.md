
---
title: clash-rs
---

### [Watfaq clash-rs](https://github.com/Watfaq/clash-rs)  ![GitHub Repo stars](https://img.shields.io/github/stars/Watfaq/clash-rs?style=social)

ClashRS 是一款基于规则的自定义协议网络代理软件，主要功能如下：

- 支持灵活的流量路由规则（基于源/目的 IP、域名、GeoIP 等）。
- 提供本地反欺骗 DNS 服务，支持 UDP/TCP/DoH/DoT。
- 可作为 HTTP/Socks5 代理或 utun 设备网关运行。
- 支持多种出站协议（Hysteria2、Shadowsocks、Trojan、Vmess、Wireguard 等）及多种传输层（gRPC/TLS/WebSocket 等）。
- 支持动态远程规则与代理加载，集成 Jaeger 追踪。
- 兼容 Linux、macOS、Windows 及 iOS 平台，支持配置文件运行、Docker 部署及源码构建。