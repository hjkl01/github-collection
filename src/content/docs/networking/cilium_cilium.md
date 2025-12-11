
---
title: cilium
---

### [cilium cilium](https://github.com/cilium/cilium)

**Cilium 项目核心内容总结：**

**项目功能**  
Cilium 是一个基于 eBPF 技术的 Kubernetes 网络与安全解决方案，提供高性能的网络策略、加密通信、负载均衡及安全策略实施，支持多种网络模式（如透明代理、IPSec），并深度集成 Kubernetes 生态。

**主要特性**  
1. **高性能网络**：利用 eBPF 实现低延迟、高吞吐的网络通信，支持大规模集群。  
2. **细粒度安全策略**：通过 L3-L7 层策略控制流量，支持加密（IPSec）、身份验证及访问控制。  
3. **可观测性**：集成 Hubble 平台，提供实时流量拓扑、协议分析、DNS 过滤及异常流量诊断。  
4. **Kubernetes 深度集成**：兼容 Gateway API，支持 Ingress、流量分割及路由配置，与 Prometheus、Grafana 等监控工具无缝对接。  
5. **多云与混合云支持**：适配 AWS、Azure、GCP 等云平台，支持跨集群通信与服务网格集成。  

**使用方法**  
- 通过 Helm Chart 或 Kustomize 安装，参考官方文档的安装指南（如 `k8s-install-default`）。  
- 配置网络策略、安全规则及 Gateway API 规则，通过 Kubernetes CRD 声明式管理。  
- 使用 Hubble CLI 或 UI 工具进行流量监控与故障排查。  

**社区与支持**  
- 活跃社区提供 Slack 交流、定期开发者会议（欧洲时间每周三 17:00、亚太时间每月第三周周三 09:00）。  
- 采用 Apache 2.0 许可证，部分 BPF 代码支持 BSD/GPL 双许可。  
- 项目由 Maintainers 管理，治理规则与贡献流程详见官方文档。