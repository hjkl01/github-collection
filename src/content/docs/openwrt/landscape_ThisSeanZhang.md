
---
title: landscape
---

### [ThisSeanZhang landscape](https://github.com/ThisSeanZhang/landscape)  ![GitHub Repo stars](https://img.shields.io/github/stars/ThisSeanZhang/landscape?style=social)

Landscape 是一款基于 Web 的 Linux 路由器配置工具，采用 Rust、eBPF 和 AF_PACKET 技术构建，旨在帮助用户轻松将 Linux 发行版配置为路由器。

核心功能包括：
1. **流量控制**：支持基于 SIP-CIDR、MAC、DIP、域名及 Geo 规则的流量分流、路由标记，及流量导入 Docker 容器。
2. **网络配置**：涵盖静态 IP、DHCP 客户端/服务端、PPPoE 拨号及 IPv6（DHCPv6-PD/RA）配置。
3. **DNS 管理**：提供每流独立的 DNS 配置与缓存（防止污染和泄露），支持 DoH/DoT/DoQ 上游及 DNS 劫持。
4. **NAT 与路由**：基于 eBPF 实现基础 NAT、端口转发及静态映射。
5. **Geo 管理**：支持管理多个 Geo 数据源并自动更新 GeoIP/GeoSite 数据。
6. **其他特性**：包含 Wi-Fi 接入点管理、连接统计监控、数据库存储配置及 NIC CPU 优化。

系统运行要求 Linux 内核 6.9 及以上并启用 BTF/BPF 功能。