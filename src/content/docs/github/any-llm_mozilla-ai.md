
---
title: any-llm
---

### [mozilla-ai any-llm](https://github.com/mozilla-ai/any-llm)  ![GitHub Repo stars](https://img.shields.io/github/stars/mozilla-ai/any-llm?style=social)

any-llm 是一个 Python SDK，提供统一接口连接任何大语言模型（LLM）提供商，支持在 OpenAI、Anthropic、Ollama 等服务商间切换而无需修改代码。它支持按需安装提供商依赖，提供直接 API 函数（适合脚本）和 AnyLLM 类（适合生产）两种调用方式。此外，可选的 any-llm-gateway 组件提供企业级功能，包括预算限制、虚拟 API 密钥管理、使用量分析及多租户支持。该库基于官方 SDK 构建，旨在解决接口碎片化并保持框架无关性。