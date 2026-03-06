
---
title: bifrost
---

### [maximhq bifrost](https://github.com/maximhq/bifrost)  ![GitHub Repo stars](https://img.shields.io/github/stars/maximhq/bifrost?style=social)

Bifrost AI Gateway 是一个高性能的 AI 网关，通过单一兼容 OpenAI 的 API 统一接入 15+ 个 AI 服务提供商（如 OpenAI、Anthropic、AWS Bedrock、Google Vertex 等），旨在构建高可用且永不宕机的 AI 应用。

核心功能包括：
1. **多供应商统一接入**：支持多个大模型提供商，提供零配置启动和 Web UI 可视化配置。
2. **高可用保障**：具备自动故障转移、智能负载均衡及语义缓存能力。
3. **企业级特性**：支持预算管理、SSO 集成、细粒度访问控制、可观测性（Prometheus 指标、分布式追踪）及安全密钥管理。
4. **灵活集成**：提供 HTTP 网关（带实时监控和分析）和 Go SDK，支持作为现有 API 的无缝替换。
5. **极致性能**：请求延迟开销极低（微秒级），支持高并发请求（5k RPS 下 100% 成功率）。