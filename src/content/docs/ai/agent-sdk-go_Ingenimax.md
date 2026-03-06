
---
title: agent-sdk-go
---

### [Ingenimax agent-sdk-go](https://github.com/Ingenimax/agent-sdk-go)  ![GitHub Repo stars](https://img.shields.io/github/stars/Ingenimax/agent-sdk-go?style=social)

Agent Go SDK 是一个用于构建生产就绪 AI 智能体的 Go 框架，核心功能总结如下：

- **多模型支持**：无缝集成 OpenAI、Anthropic、Google Vertex AI、DeepSeek、Ollama 及 vLLM。
- **工具与集成**：提供模块化工具生态，支持 Web 搜索、自定义操作及 Model Context Protocol (MCP) 服务器。
- **记忆管理**：支持持久化对话跟踪，提供 Buffer、向量检索及 Redis 存储选项。
- **企业级特性**：内置安全护栏、完整的可观测性（追踪与日志）及多租户资源隔离。
- **配置与开发**：支持声明式 YAML 配置、系统提示自动配置生成、结构化任务框架及 Token 使用追踪。
- **使用方式**：既可作为 Go 库集成，也提供命令行工具（CLI）用于无头模式运行。