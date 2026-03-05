
---
title: aisuite
---

### [andrewyng aisuite](https://github.com/andrewyng/aisuite)  ![GitHub Repo stars](https://img.shields.io/github/stars/andrewyng/aisuite?style=social)

aisuite 是一个轻量级 Python 库，旨在为多种生成式 AI 提供商提供统一的 API 接口。它屏蔽了 OpenAI、Anthropic、Google、AWS 等不同平台的 SDK 差异、认证细节及参数变化，使开发者能够以极简方式构建 LLM 或智能体应用。主要功能包括：

1. **统一 API 接口**：支持代码一次编写跨平台运行，可无缝切换不同的模型提供商。
2. **智能体应用构建**：提供简单抽象，通过 `max_turns` 参数即可自动管理多轮对话与工具执行循环。
3. **工具调用支持**：支持直接传递 Python 函数作为工具，自动处理 Schema 生成与执行；同时原生集成 Model Context Protocol (MCP)。
4. **模块化扩展**：采用插件式架构，允许通过编写轻量级适配器轻松添加新的模型提供商支持。