### [agentgateway](https://github.com/agentgateway/agentgateway) ![GitHub Repo stars](https://img.shields.io/github/stars/agentgateway/agentgateway?style=social)

Agentgateway 是一个面向智能体 AI 的开源连接代理，基于 MCP 和 A2A 等 AI 原生协议，为智能体与大语言模型、工具以及其他智能体之间的通信提供统一的安全、可观测性和治理能力，适用于各种框架和部署环境。

核心功能包括：通过兼容 OpenAI 的统一 API 接入多个主流大模型服务商，并支持预算控制、提示增强、负载均衡和故障切换；通过 MCP 将大模型连接到工具和外部数据源，支持工具联邦、多种传输方式、OpenAPI 集成和 OAuth 认证；通过 A2A 实现安全的智能体间通信，支持能力发现、模态协商和任务协作；支持面向自托管模型的智能推理路由，可根据 GPU 利用率、KV 缓存、LoRA 适配器和队列深度进行决策；提供多层内容防护能力，包括正则过滤、OpenAI 审核、AWS Bedrock Guardrails、Google Model Armor 和自定义 Webhook；同时具备认证、细粒度 RBAC、限流、TLS 以及基于 OpenTelemetry 的指标、日志和链路追踪等安全与观测能力。它还内置可视化界面，便于查看智能体与工具、智能体与智能体之间的连接情况。