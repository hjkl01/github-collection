
---
title: aisuite
---

### [andrewyng aisuite](https://github.com/andrewyng/aisuite)

**项目核心内容总结：**

`aisuite` 是一个轻量级的 Python 库，提供了一个**统一的 API 接口**，用于与多个生成式 AI 提供商（如 OpenAI、Anthropic、Google、Hugging Face、AWS、Cohere、Mistral、Ollama 等）进行交互。它抽象了 SDK 差异、认证细节和参数变化，设计风格模仿 OpenAI 的 API，使开发者可以快速上手。

**主要功能：**

- 提供统一的 API，支持多个模型提供商，代码可复用，只需更改参数即可切换模型。
- 支持创建轻量级的代理应用，通过 `max_turns` 参数控制多轮对话。
- 可直接传递 Python 函数进行工具调用，无需 JSON 格式描述。
- 支持 MCP 工具集成，无需手动编写连接代码。
- 模块化架构，易于扩展新提供商。

**使用方法：**

- 安装基础包：`pip install aisuite`
- 安装特定提供商包：`pip install 'aisuite[provider_name]'`
- 设置 API 密钥（如 `OPENAI_API_KEY`），通过 `Client` 对象调用模型。

**示例代码：**

```python
import aisuite as ai
client = ai.Client()

response = client.chat.completions.create(
    model="openai:gpt-4o",
    messages=[{"role": "user", "content": "Summarize this paragraph."}],
)
print(response.choices[0].message.content)
```

**其他特性：**

- 支持手动和自动工具调用两种方式。
- 提供 MCP 工具集成，用于连接外部数据源或工具。
- 允许用户通过实现适配器方式扩展新提供商。

**总结：** `aisuite` 旨在降低多模型提供商的使用复杂度，使开发者可以专注于构建 AI 应用，而无需处理 API 集成的细节。