
---
title: chat-ui
---

### [huggingface chat-ui](https://github.com/huggingface/chat-ui)  ![GitHub Repo stars](https://img.shields.io/github/stars/huggingface/chat-ui?style=social)

Chat UI 是一个基于 SvelteKit 的 LLM 聊天界面项目，作为 HuggingChat 应用的前端核心。它仅支持 OpenAI 兼容 API，可灵活对接 Ollama、llama.cpp、Hugging Face 等多种大模型服务。项目使用 MongoDB 存储对话数据、用户设置及历史，支持本地开发、生产构建及 Docker 容器化部署。主要功能包括自定义主题、模型发现，并支持可选的 LLM 智能路由（Omni 虚拟模型）和 MCP 工具调用，以增强模型选择与外部工具交互能力。