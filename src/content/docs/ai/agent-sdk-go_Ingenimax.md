
---
title: agent-sdk-go
---

### [Ingenimax agent-sdk-go](https://github.com/Ingenimax/agent-sdk-go)  ![GitHub Repo stars](https://img.shields.io/github/stars/Ingenimax/agent-sdk-go?style=social)

Agent Go SDK 是一个构建生产级 AI 代理的 Go 框架，集成了内存管理、工具执行、多模型支持与企业级功能。

**核心能力**
- **多模型支持**：无缝集成 OpenAI、Anthropic、Google Vertex AI、DeepSeek、Ollama 及 vLLM。
- **工具生态**：支持模块化扩展（如 Web 搜索），通过 HTTP/stdio 集成 MCP 服务器（支持懒加载/急加载）。
- **内存管理**：提供持久化对话追踪，支持缓冲和向量检索模式。
- **企业特性**：内置安全护栏、完整可观测性（追踪/日志）及多租户资源隔离。
- **成本监控**：内置 Token 用量追踪与计费分析。

**开发体验**
- **声明式配置**：通过 YAML 定义代理、任务及子代理，支持结构化输出 (JSON) 和变量扩展。
- **自动化引导**：根据系统提示自动生成完整的代理配置和任务定义。
- **任务框架**：支持规划、审批及执行复杂的多步操作。

**部署与使用**
- **Go 库集成**：作为库引入项目，支持多租户上下文及自定义内存后端（如 Redis）。
- **CLI 工具**：提供无头模式命令行接口，支持交互聊天、任务执行、配置管理及 MCP 服务器管理。