
---
title: fastmcp
---

### [jlowin fastmcp](https://github.com/jlowin/fastmcp)  ![GitHub Repo stars](https://img.shields.io/github/stars/jlowin/fastmcp?style=social)

FastMCP 是由 Prefect 开发的 Model Context Protocol (MCP) 标准框架，旨在连接大语言模型（LLM）与工具和数据，实现从原型到生产的高效构建。其核心功能包括：

1. **Servers（服务器）**：将 Python 函数封装为 MCP 兼容的工具、资源和提示词，自动处理 schema、验证与文档。
2. **Clients（客户端）**：支持通过完整协议连接任意本地或远程 MCP 服务器。
3. **Apps（应用）**：为工具提供直接在对话中渲染的交互 UI。

FastMCP 自动管理传输协商、认证及协议生命周期，内置最佳实践，是目前构建 MCP 服务器的标准方案。