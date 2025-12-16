
---
title: kong
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/Kong/kong?style=social) ](https://github.com/Kong/kong)
### [Kong kong](https://github.com/Kong/kong)

**Kong Gateway** 是一个云原生、平台无关的高性能 API 网关，支持 API、大型语言模型（LLM）和机器编排平台（MCP）流量管理，具备高可扩展性和插件生态。其核心功能包括：  
- **API 管理**：代理、路由、负载均衡、健康检查、认证授权（JWT、OAuth 等）。  
- **AI 能力**：支持多 LLM 提供商（如 OpenAI、Anthropic 等），提供语义安全、流量治理和可观测性。  
- **插件系统**：60+ 插件用于流量控制、日志、监控、请求/响应转换等，支持 Lua、Go、JavaScript 开发。  
- **部署灵活**：支持 Kubernetes 原生部署、声明式无数据库部署、混合部署等。  

**使用方法**：  
1. 通过 Docker Compose 安装，执行 `KONG_DATABASE=postgres docker-compose --profile database up` 启动。  
2. 访问 `localhost:8000`（服务流量）、`localhost:8001`（Admin API）、`localhost:8002`（管理界面）。  
3. 可通过 [Kong AI Gateway 文档](https://developer.konghq.com/ai-gateway/) 配置 LLM/MCP 功能。  

**主要特性**：  
- 支持 L4/L7 代理、SSL/TLS 终止。  
- 提供 MCP 自动生成、语义路由、AI 缓存等 60+ AI 特性。  
- 社区插件市场（[Plugin Hub](https://docs.konghq.com/hub/)）提供扩展功能。  

**许可证**：Apache 2.0 开源协议。