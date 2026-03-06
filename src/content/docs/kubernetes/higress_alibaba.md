
---
title: higress
---

### [alibaba higress](https://github.com/alibaba/higress)  ![GitHub Repo stars](https://img.shields.io/github/stars/alibaba/higress?style=social)

Higress 是一款基于 Istio 和 Envoy 的云原生 AI 原生 API 网关，核心功能包括：

1. **AI 网关**：统一接入国内外主流大模型，支持 MCP 服务器托管，提供 LLM 及 MCP API 统一管理能力。
2. **Kubernetes Ingress**：作为 Ingress 控制器兼容 K8s 标准与 Gateway API，资源开销低且路由变更生效快。
3. **微服务网关**：支持多注册中心服务发现，深度集成 Dubbo、Nacos 等微服务生态。
4. **安全网关**：内置 WAF 防护及多种认证授权策略（如 JWT、OIDC）。
5. **可扩展性**：支持 Go/Rust/JS 编写 Wasm 插件，实现内存安全、独立版本升级及流量无损热更新。
6. **生产级特性**：源自阿里内部验证，支持高并发，消除配置重载抖动，支持流式处理，提供 UI 控制台及 Docker、K8s 等多种部署方案。