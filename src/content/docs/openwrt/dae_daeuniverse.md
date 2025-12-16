
---
title: dae
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/daeuniverse/dae?style=social) ](https://github.com/daeuniverse/dae)
### [daeuniverse dae](https://github.com/daeuniverse/dae)

**项目核心内容总结：**

dae 是一个基于 Linux 内核 eBPF 技术实现的高性能透明代理方案，支持通过进程名、MAC 地址等规则进行流量分流，实现“真实直连”（无需经过代理转发），显著降低性能损耗。其主要特性包括：自动根据策略（如延迟测试）切换节点、高级 DNS 解析、支持多种代理协议（如 Shadowsocks、Trojan 等）、全锥形 NAT 适配等。项目作为 v2rayA 的继任者，放弃 v2ray-core 以提供更灵活的配置能力。

**使用方法：**  
参考 [Quick Start Guide](./docs/en/README.md) 快速部署。

**注意事项：**  
1. 同机部署 UDP 服务（如 Shadowsocks）时，需为对应端口添加 `must_direct` 规则，避免 UDP 流量被误代理。  
2. 国内用户若遇到首次访问国内网站加载延迟，需检查 DNS 路由规则，避免因使用国外 DNS 导致部分域名（如 `ocsp.digicert.cn`）解析异常。