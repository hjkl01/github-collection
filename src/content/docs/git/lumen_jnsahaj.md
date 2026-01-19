
---
title: lumen
---

### [jnsahaj lumen](https://github.com/jnsahaj/lumen)  ![GitHub Repo stars](https://img.shields.io/github/stars/jnsahaj/lumen?style=social)

**项目核心内容总结：**

Lumen 是一个基于 AI 的命令行工具，旨在优化 Git 工作流程，提供以下核心功能：  
1. **智能提交信息生成**：根据代码更改自动生成符合规范的提交信息（如 feat、fix、docs 等类型）。  
2. **差异分析与解释**：通过 AI 解析代码差异，帮助理解修改内容。  
3. **多 AI 提供商支持**：兼容 OpenAI、Claude、Gemini、Ollama 等主流模型，支持本地或云端模型调用。  

**使用方法：**  
- **命令行调用**：通过 CLI 参数指定 AI 提供商、模型、API 密钥等（如 `lumen -p openai -k "key" draft`）。  
- **配置文件**：支持项目级或全局配置文件（JSON 格式），可自定义提交类型、主题（如暗色/亮色主题）、默认模型等。  
- **环境变量**：通过环境变量设置全局参数（如 `LUMEN_AI_PROVIDER="openai"`）。  

**主要特性：**  
- **多模型适配**：支持主流 AI 提供商的多种模型（如 GPT-5、Claude-3、Gemini-2.5 等），可自由切换。  
- **主题定制**：支持代码差异查看器的视觉主题（如 Catppuccin Mocha 风格）。  
- **灵活配置**：配置优先级明确（CLI 参数 > 配置文件 > 环境变量 > 默认值），支持项目级和全局配置。  
- **集成便捷**：可与 Lazygit 等工具联动，提升开发效率。  

**适用场景**：适用于需要频繁提交代码、优化 Git 日志规范、利用 AI 分析代码差异的开发者。