### [pydantic pydantic-ai](https://github.com/pydantic/pydantic-ai)  ![GitHub Repo stars](https://img.shields.io/github/stars/pydantic/pydantic-ai?style=social)

Pydantic AI 是一个基于 Pydantic 验证的 Python 生成式 AI 智能体框架，旨在以类 FastAPI 的体验构建生产级 AI 应用与工作流。

核心功能：
1. **模型中立**：支持 OpenAI、Anthropic 等主流模型及众多云服务商，支持自定义模型。
2. **类型安全**：利用 Python 类型提示进行静态检查，将错误从运行时移至编写时，增强 IDE 智能提示。
3. **无缝可观测性**：深度集成 Pydantic Logfire 或 OpenTelemetry，支持实时调试、追踪与成本监控。
4. **工具与依赖注入**：支持注册 LLM 工具函数，通过类型安全的上下文注入业务逻辑与数据。
5. **高级流程控制**：支持流式结构化输出验证、图定义（Graph）、持久执行及人类介入审批。
6. **评估与标准**：提供性能评估工具，并支持 MCP、A2A 及 UI 事件流标准。

该项目致力于将 Pydantic 的验证优势延伸至 GenAI 开发，提供高效、可靠且易于类型检查的 AI 代理构建体验。