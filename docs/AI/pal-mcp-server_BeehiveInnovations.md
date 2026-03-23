### [BeehiveInnovations pal-mcp-server](https://github.com/BeehiveInnovations/pal-mcp-server)  ![GitHub Repo stars](https://img.shields.io/github/stars/BeehiveInnovations/pal-mcp-server?style=social)

PAL MCP 是一个模型上下文协议（MCP）服务器，用于将 AI 命令行工具（如 Claude Code、Codex CLI、Cursor）与多个模型提供商（如 Gemini、OpenAI、Anthropic、Ollama 等）连接，实现多模型编排与协作。

核心功能：
1. **多模型协调**：支持在单一会话中调度多个模型进行对话、代码审查及决策，保持跨工具上下文连续性。
2. **CLI 桥接**：通过 `clink` 工具连接外部 AI CLI，支持隔离子代理和角色专业化工作流。
3. **智能工具集**：内置代码审查、调试、规划、重构、测试生成及 API 查找等工具，自动根据任务选择最优模型。
4. **上下文增强**：突破 MCP 令牌限制，支持对话上下文复活，防止大代码库场景下的上下文重置问题。
5. **灵活配置**：兼容云端及本地模型，支持自定义 API 密钥、工具启用状态及模型参数。

通过“一个 CLI + 多个模型”模式，该项目显著增强代码分析、问题解决及协作开发效率。