
---
title: crush
---

### [charmbracelet crush](https://github.com/charmbracelet/crush)  ![GitHub Repo stars](https://img.shields.io/github/stars/charmbracelet/crush?style=social)

**项目核心内容总结：**  
Crush 是一个支持多种 AI 模型的命令行工具，可集成 Anthropic、Vertex AI、Amazon Bedrock 等云服务模型，以及本地运行的 Ollama、LM Studio 等模型。用户通过配置 API 密钥和模型参数，可直接调用模型进行交互。主要特性包括：  
1. **多模型支持**：兼容主流云服务模型及本地模型，支持自定义模型配置（如成本、上下文窗口等）。  
2. **自动更新**：默认从开源数据库 Catwalk 自动同步最新模型和提供商信息，支持禁用该功能。  
3. **灵活配置**：通过环境变量或 `crush.json` 文件设置密钥、模型参数及日志调试选项。  
4. **日志与调试**：提供日志记录功能，支持查看历史日志、实时追踪及调试模式。  
5. **隐私控制**：默认收集匿名使用数据，用户可选择禁用指标收集。  
使用方法包括安装后配置密钥、调用模型、管理日志及更新提供商信息。