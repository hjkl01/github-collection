
---
title: any-llm
---

### [mozilla-ai any-llm](https://github.com/mozilla-ai/any-llm)

**项目核心内容总结：**

**功能**  
`any-llm` 是一个统一的接口库，支持通过简单代码切换 OpenAI、Anthropic、Mistral、Ollama 等多个大语言模型（LLM）提供商，无需修改代码逻辑。提供两种使用方式：直接调用 API 函数（适合开发测试）和通过 `AnyLLM` 类实例化对象（适合生产环境）。可选部署 `any-llm-gateway` 代理服务器，支持预算管理、密钥管理、使用分析等企业级功能。

**使用方法**  
1. 安装：通过 `pip install 'any-llm-sdk[提供商]'` 安装所需提供商支持。  
2. 配置：设置对应提供商的 API 密钥环境变量（如 `OPENAI_API_KEY`）。  
3. 调用：使用 `completion` 函数，指定 `model`（模型名）和 `provider`（提供商名）参数，或采用 `provider:model` 格式。  
4. 高级用法：通过 `AnyLLM` 类创建实例，复用客户端连接。

**主要特性**  
- **统一接口**：所有提供商使用一致的 API 调用方式，仅需修改模型名和提供商名。  
- **兼容性**：基于官方 SDK 实现，确保与各提供商 API 的兼容性。  
- **灵活部署**：支持直接连接（开发）或通过 `any-llm-gateway` 代理（生产），后者提供预算控制、密钥管理、多租户支持等功能。  
- **开发友好**：提供类型提示、清晰错误信息，支持流式响应、工具调用等高级功能。  
- **企业功能**：`any-llm-gateway` 支持用例追踪、成本分析、虚拟密钥管理等。