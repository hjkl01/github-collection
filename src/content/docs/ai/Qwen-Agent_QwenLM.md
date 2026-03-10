
---
title: Qwen-Agent
---

### [QwenLM Qwen-Agent](https://github.com/QwenLM/Qwen-Agent)  ![GitHub Repo stars](https://img.shields.io/github/stars/QwenLM/Qwen-Agent?style=social)

Qwen-Agent 是一个基于 Qwen 的大语言模型（LLM）应用开发框架，支持指令遵循、工具调用、规划与记忆等功能。该框架提供了一系列示例应用，如浏览器助手、代码解释器和自定义助手，并作为 [Qwen Chat](https://chat.qwen.ai/) 的后端运行。

主要功能包括：
- 支持多种工具调用，如图像生成、代码执行、文件操作、数据库访问等；
- 提供代码解释器工具，可在隔离的 Docker 容器中安全执行代码；
- 支持 MCP（Model Context Protocol）协议，便于集成多种开源工具；
- 提供 GUI 界面，便于快速部署和调试；
- 支持多种模型服务，包括阿里云 DashScope 和本地部署的 OpenAI 兼容服务（如 vLLM 和 Ollama）；
- 支持超长文档（百万级 token）的问答处理，提供高效的 RAG 解决方案；
- 提供内置代理类（如 Assistant、FnCallAgent、ReActChat），也可自定义代理逻辑；
- 支持并行工具调用，提升处理效率；
- 提供完整的文档和示例，便于快速上手和扩展开发。