
---
title: pydantic-ai
---

### [pydantic pydantic-ai](https://github.com/pydantic/pydantic-ai)  ![GitHub Repo stars](https://img.shields.io/github/stars/pydantic/pydantic-ai?style=social)

Pydantic AI 是一个基于 Pydantic 的 Python 生成式 AI 代理框架，旨在帮助开发者快速、可靠地构建生产级 AI 应用和工作流。

核心特性包括：
1. **全类型安全**：利用 Python 类型提示和 Pydantic 验证，将大量错误从运行时转移至编写时。
2. **模型无关性**：支持主流大模型提供商（如 OpenAI、Anthropic、Gemini 等）及自定义模型实现。
3. **无缝可观测性**：深度集成 Pydantic Logfire 和 OpenTelemetry，支持实时调试、行为追踪和成本监控。
4. **强大工具集成**：支持工具调用、依赖注入、人机循环工具审批、外部工具交互及 Agent 间互通。
5. **高级功能**：提供结构化输出验证、流式输出、持久化执行、复杂工作流图定义及系统化评估（Evals）。

该框架致力于将 FastAPI 的优雅设计理念带入 GenAI 开发，提供简洁、高效且易于维护的体验。