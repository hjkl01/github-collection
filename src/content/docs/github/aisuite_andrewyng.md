
---
title: aisuite
---

### [andrewyng aisuite](https://github.com/andrewyng/aisuite)  ![GitHub Repo stars](https://img.shields.io/github/stars/andrewyng/aisuite?style=social)

aisuite 是一个轻量级 Python 库，提供统一的 API 接口以对接多个生成式 AI 提供商（如 OpenAI、Anthropic、Google、Hugging Face 等）。它通过抽象 SDK 差异和认证细节，实现跨模型的一站式集成。

主要功能包括：
1. 统一 API：编写一次代码即可在多个提供商间切换，标准化聊天补全请求与响应。
2. 轻量级 Agent 构建：支持通过参数配置多轮对话和自动化工具执行流。
3. 灵活工具调用：支持直接传递 Python 函数或 MCP 工具，自动处理 Schema 生成与执行。
4. 扩展性强：采用插件式架构，便于快速添加新的模型提供商支持。

该库旨在降低学习成本，让开发者专注于 AI 系统构建而非 API 集成。