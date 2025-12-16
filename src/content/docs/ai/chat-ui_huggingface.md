
---
title: chat-ui
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/huggingface/chat-ui?style=social) ](https://github.com/huggingface/chat-ui)
### [huggingface chat-ui](https://github.com/huggingface/chat-ui)

**项目核心内容总结：**

Chat UI 是一个基于 SvelteKit 构建的聊天界面，用于与大型语言模型（LLM）进行交互，主要支持 OpenAI 兼容的 API。该项目是 HuggingChat 应用（hf.co/chat）的底层技术支撑。

**功能与使用方法：**

- **快速启动**：支持通过 Hugging Face 推理服务、llama.cpp、Ollama、OpenRouter 等 OpenAI 兼容的 API 进行部署。只需设置 `.env.local` 文件，配置 `OPENAI_BASE_URL` 和 `OPENAI_API_KEY`，并选择 MongoDB 数据库即可启动。
- **数据库支持**：使用 MongoDB 存储聊天记录、用户信息、设置等数据，支持 MongoDB Atlas（托管服务）和本地 MongoDB 容器两种部署方式。
- **运行方式**：通过 `npm run dev` 启动开发服务器，默认监听 `http://localhost:5173`；也可使用 Docker 容器化部署。
- **自定义功能**：支持主题定制、模型路由（如使用 Arch-Router 进行模型选择）、MCP 工具调用（如 Web 搜索、Hugging Face 登录等），并提供用户级别的工具调用和多模态输入开关。

**主要特性：**

- 仅支持 OpenAI 兼容的 API，适用于 llama.cpp、Ollama、OpenRouter 等服务。
- 支持灵活的数据库部署方式（本地或托管）。
- 提供模型路由功能，可根据用户输入自动选择最佳模型。
- 支持 MCP 工具调用，允许用户与外部服务进行交互。
- 可通过环境变量自定义应用名称、主题、数据共享等设置。