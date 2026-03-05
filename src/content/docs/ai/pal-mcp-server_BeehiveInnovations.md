
---
title: pal-mcp-server
---

### [BeehiveInnovations pal-mcp-server](https://github.com/BeehiveInnovations/pal-mcp-server)  ![GitHub Repo stars](https://img.shields.io/github/stars/BeehiveInnovations/pal-mcp-server?style=social)

PAL MCP 是一个 MCP 服务器，作为 Provider 抽象层，将 CLI AI 工具（如 Claude Code、Codex、Cursor）与多个 AI 模型（如 Gemini、OpenAI、Anthropic、Grok、本地模型等）连接。

核心功能：
1. **多模型编排**：在单次对话中协调多个模型，实现协作辩论、获取第二意见及构建共识。
2. **上下文延续**：跨工具和模型保持会话线程，确保上下文无缝流转，解决主模型上下文重置问题。
3. **CLI 桥接 (clink)**：连接外部 AI CLI 进入工作流，支持创建隔离子代理、角色专业化及任务卸载。
4. **开发工具集**：提供代码审查、调试、规划、预提交验证、测试生成、安全审计等工具，支持按需配置。
5. **广泛支持**：兼容主流云厂商及本地模型，具备视觉分析及突破 MCP 令牌限制的能力。

旨在通过组合不同模型优势，增强代码分析、问题解决和协作开发体验。