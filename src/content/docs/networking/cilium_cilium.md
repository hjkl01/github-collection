
---
title: cilium
---

### [cilium cilium](https://github.com/cilium/cilium)  ![GitHub Repo stars](https://img.shields.io/github/stars/cilium/cilium?style=social)

Cilium 是基于 eBPF 技术的 Kubernetes 网络、可观测性与安全解决方案。主要功能包括：

1. **容器网络**：提供 CNI 插件，支持 Overlay 和原生路由模式，可完全替代 kube-proxy，实现扁平化 L3 网络。
2. **负载均衡**：基于 eBPF 的分布式负载均衡，支持东西向和南北向流量，性能高且扩展性强。
3. **集群网格**：支持 Cluster Mesh 实现跨集群的安全连接和全局服务发现。
4. **安全策略**：基于身份的安全模型，支持 L3-L7 策略（含 DNS/HTTP 过滤），解耦于网络寻址。
5. **服务网格**：集成服务网格能力，支持双向认证、加密及 Kubernetes Gateway API。
6. **可观测性**：内置 Hubble 平台，提供流可视化、服务拓扑及详细的故障排查信息。

支持 AMD64 和 AArch64 架构。