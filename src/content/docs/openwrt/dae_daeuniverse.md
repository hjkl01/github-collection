
---
title: dae
---

### [daeuniverse dae](https://github.com/daeuniverse/dae)  ![GitHub Repo stars](https://img.shields.io/github/stars/daeuniverse/dae?style=social)

dae（鹅）是一款基于 Linux 内核 eBPF 技术的高性能透明代理解决方案，作为 v2rayA 的继任者，它通过实现“实直连”流量分流，使直连流量绕过代理应用转发，从而最小化性能损耗和资源消耗。

主要功能包括：
- 支持实直连流量分流（需开启 ipforward）。
- 支持按本地进程名和局域网 MAC 地址进行流量分流。
- 支持反义匹配规则。
- 支持基于策略自动切换节点（支持 TCP/UDP/IPv4/IPv6 延迟测试）。
- 支持高级 DNS 解析。
- 支持 shadowsocks、trojan 和 socks5 的全锥 NAT。
- 支持多种主流代理协议。