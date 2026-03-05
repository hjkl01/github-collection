
---
title: gpt-load
---

### [tbphp gpt-load](https://github.com/tbphp/gpt-load)  ![GitHub Repo stars](https://img.shields.io/github/stars/tbphp/gpt-load?style=social)

GPT-Load 是一款基于 Go 语言开发的高性能企业级 AI API 透明代理服务，专为需要集成多个 AI 服务的企业和开发者设计。

主要功能：
- **透明代理**：完整保留 OpenAI、Google Gemini、Anthropic Claude 等原生 API 格式，支持 Azure OpenAI 及兼容服务。
- **智能密钥管理**：支持高性能密钥池、分组管理、自动轮换及故障恢复。
- **负载均衡**：多上游端点加权调度，提升服务可用性。
- **动态配置**：系统设置与分组配置支持热重载，无需重启。
- **企业级架构**：支持分布式主从部署、水平扩展及高可用集群。
- **可视化管理**：基于 Vue 3 的 Web 管理界面，提供实时统计、健康检查及详细请求日志。
- **安全机制**：支持 API 密钥加密存储及管理与代理双重认证。

支持 Docker、源码构建及集群部署，用户通过替换 API 地址与密钥即可无缝迁移调用。