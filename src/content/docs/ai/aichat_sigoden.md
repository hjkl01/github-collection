
---
title: aichat
---

### [sigoden aichat](https://github.com/sigoden/aichat)

**项目核心内容总结：**

**AIChat** 是一个集成多种功能的 LLM 命令行工具，支持多模型提供商、交互式模式、会话管理、文档检索及本地服务器部署。  

**主要功能与特性：**  
1. **多模型支持**：兼容 20+ 提供商（如 OpenAI、Claude、Gemini、Ollama 等），统一接口调用。  
2. **交互模式**：  
   - **CMD 模式**：通过自然语言生成 Shell 命令，提升终端操作效率。  
   - **REPL 模式**：支持代码补全、多行输入、历史搜索及自定义提示符的交互式环境。  
3. **会话管理**：维护上下文对话，确保交互连续性。  
4. **RAG 集成**：结合外部文档提升回答准确性。  
5. **工具与代理**：通过函数调用扩展能力，支持自动化任务及 AI 代理（类似 GPTs）。  
6. **本地服务器**：内置 HTTP 服务，提供 Chat、Embedding、Rerank 接口及 LLM 对比平台（Arena）。  
7. **自定义配置**：支持角色设定、宏命令、主题（暗/亮模式）及 REPL 提示符定制。  

**使用方法：**  
- **安装**：通过 `cargo install aichat`、Homebrew、Pacman 等包管理器，或下载预编译二进制文件。  
- **运行**：直接命令行调用（如 `aichat hello`），或通过 `-f` 参数加载文件、目录、URL 等多类型输入。  
- **本地服务**：执行 `aichat --serve` 启动内置服务器，访问 API 或 Web 界面（Playground/Arena）。