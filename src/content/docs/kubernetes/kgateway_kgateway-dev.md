
---
title: kgateway
---

### [kgateway-dev kgateway](https://github.com/kgateway-dev/kgateway)  ![GitHub Repo stars](https://img.shields.io/github/stars/kgateway-dev/kgateway?style=social)

**kgateway 核心内容总结**  

**项目功能**  
kgateway 是 Kubernetes 中最广泛部署的网关，支持微服务和 AI 代理的统一 API 连接。基于 Kubernetes Gateway API，它同时兼容 Envoy 和 agentgateway 两个数据平面，提供从传统 HTTP/gRPC 服务到 AI 推理的全场景支持。  

**使用场景**  
- 作为高级入口控制器和下一代 API 网关，实现认证、限流等能力；  
- 作为 AI 网关，管理大模型（LLM）访问安全与合规；  
- 支持生成模型的推理路由；  
- 实现代理间通信与模型上下文协议（MCP）服务联邦；  
- 支持混合架构应用迁移（微服务、Serverless、遗留系统）。  

**主要特性**  
- **双控制平面架构**：兼容 Envoy 和 agentgateway，适配多种场景；  
- **高扩展性**：从轻量级微网关到亿级请求的中心化网关；  
- **AI 集成**：支持 AI 推理、安全防护与数据治理；  
- **多云兼容**：适配任意云环境与技术栈；  
- **开源生态**：基于 Kubernetes Gateway API，集成开源项目（如 Envoy）。  

**其他信息**  
- 项目由 CNCF 沙盒支持，社区驱动；  
- 原为 Solo.io 于 2018 年推出的 Gloo，现更名为 kgateway。