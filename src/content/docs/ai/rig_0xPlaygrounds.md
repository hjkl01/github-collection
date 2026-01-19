
---
title: rig
---

### [0xPlaygrounds rig](https://github.com/0xPlaygrounds/rig)  ![GitHub Repo stars](https://img.shields.io/github/stars/0xPlaygrounds/rig?style=social)

**项目核心内容总结：**  
Rig 是一个用于构建可扩展、模块化且符合人体工程学的 **LLM（大语言模型）应用** 的 Rust 库，支持多模型提供商和向量存储集成。  

**主要功能与特性：**  
- 支持多轮对话、流式处理和复杂代理工作流；  
- 兼容 GenAI 语义规范（OpenTelemetry）；  
- 集成 20+ 模型提供商（如 OpenAI、AWS Bedrock 等）和 10+ 向量存储（如 MongoDB、Qdrant 等）；  
- 支持 LLM 完成、嵌入、语音/图像生成等能力；  
- 提供极简代码集成 LLM，兼容 WASM（仅核心库）；  
- 提供配套 crate 用于扩展功能（如数据库、区块链交互等）。  

**使用方法：**  
通过 `cargo add rig-core` 安装，示例代码展示如何使用 OpenAI 客户端调用模型，需设置环境变量并启用 Tokio 异步功能。  

**典型用户：**  
St Jude、Coral Protocol、Nethermind 等公司及项目已采用 Rig 构建 AI 应用。