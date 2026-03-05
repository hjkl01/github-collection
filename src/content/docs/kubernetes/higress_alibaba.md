
---
title: higress
---

### [alibaba higress](https://github.com/alibaba/higress)  ![GitHub Repo stars](https://img.shields.io/github/stars/alibaba/higress?style=social)

Higress 是一款基于 Istio 和 Envoy 的云原生 AI 原生 API 网关，支持使用 Go/Rust/JS 编写 Wasm 插件进行扩展。

**核心功能：**
1. **AI 网关**：支持国内外主流模型提供商，统一管理 LLM API 和 MCP API，提供认证、限流、可观测性及缓存能力。
2. **Kubernetes Ingress**：兼容 Gateway API 和 Nginx Ingress 注解，资源开销低，路由生效速度快。
3. **微服务网关**：支持多服务注册中心，深度集成 Dubbo、Nacos、Sentinel 等生态。
4. **安全网关**：支持 WAF 防护及多种认证策略（如 JWT、OIDC、Key-Auth 等）。

**核心优势：**
- **生产级**：源自阿里内部实践，配置毫秒级生效，无流量抖动，适配长连接与高并发。
- **流式处理**：支持请求响应体全流式处理，降低高带宽场景内存开销。
- **易扩展**：丰富的 Wasm 插件库，支持热更新与沙箱隔离，业务无感升级。
- **易用安全**：遵循标准 API，提供控制台，支持 Docker 部署及自动证书管理。