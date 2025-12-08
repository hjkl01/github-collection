
---
title: aichat
---

### [sigoden aichat](https://github.com/sigoden/aichat)

**AIChat 项目核心内容总结：**

**项目功能**  
AIChat 是一款集成多种功能的大型语言模型（LLM）命令行工具，支持以下核心能力：  
- **多模型提供商支持**：兼容 20+ 主流 LLM 服务（如 OpenAI、Claude、Gemini、Ollama 等）。  
- **多模式交互**：提供 CMD 模式（命令行工具）、REPL 模式（交互式命令行）、Shell 助手（将自然语言转换为 Shell 命令）。  
- **灵活输入处理**：支持本地文件、目录、远程 URL、标准输入（stdin）及外部命令输出作为输入。  
- **会话与角色管理**：通过会话保持上下文连贯性，自定义角色提示词和模型配置以调整 LLM 行为。  
- **扩展功能**：集成 RAG（基于检索的生成）、函数调用（连接外部工具）、AI 工具/代理（自动化任务）、宏（组合命令）。  
- **本地服务器**：内置 HTTP 服务器，提供 Chat Completions、Embeddings、Rerank 接口及 Web 界面（Playground、Arena 对比不同模型）。  

**使用方法**  
- **安装**：通过 `cargo install aichat`（Rust 开发者）、Homebrew、Pacman、Scoop 等包管理器安装，或从 GitHub 发布页下载预编译二进制文件。  
- **运行**：直接命令行调用（如 `aichat hello`），或通过 `--serve` 启动本地服务器。  

**主要特性**  
- 支持自定义主题（暗色/亮色模式）。  
- 提供详细的中文文档（含配置、主题、宏等指南）。  
- 开源协议：MIT 或 Apache 2.0 双许可。