
---
title: rig
---

### [0xPlaygrounds rig](https://github.com/0xPlaygrounds/rig)  ![GitHub Repo stars](https://img.shields.io/github/stars/0xPlaygrounds/rig?style=social)

Rig 是一个基于 Rust 的库，用于构建可扩展、模块化且易用的大型语言模型（LLM）应用。其主要功能包括：

- 提供统一接口支持 20 多种模型提供商和 10 多种向量存储库。
- 支持代理工作流，处理多轮流式传输、提示及对话管理。
- 兼容 GenAI 语义规范。
- 支持 LLM 完成、文本嵌入、语音转录、音频生成及图像生成。
- 核心库支持全 WASM 兼容性，代码样板极少。

项目通过独立的配套 crate 扩展向量存储和模型提供商的集成能力，帮助开发者快速将 LLM 集成到应用程序中。