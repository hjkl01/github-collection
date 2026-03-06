
---
title: any-llm
---

### [mozilla-ai any-llm](https://github.com/mozilla-ai/any-llm)  ![GitHub Repo stars](https://img.shields.io/github/stars/mozilla-ai/any-llm?style=social)

any-llm 是一个 Python SDK，通过统一接口实现与各大语言模型提供商（如 OpenAI、Anthropic、Mistral、Ollama 等）的无缝通信，切换提供商无需修改代码。

**核心功能：**
1. **统一 API**：兼容官方 SDK，支持对话完成和 Responses API，框架无关。
2. **灵活模式**：提供直接函数调用（适合脚本/实验）和 AnyLLM 类（适合生产环境/连接复用）。
3. **企业级网关**：可选部署 any-llm-gateway，支持预算限制、密钥管理、使用分析及多租户控制。
4. **直连支持**：无需代理服务器，直接连接各模型提供商。