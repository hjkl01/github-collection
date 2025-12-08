
---
title: context7
---

### [upstash context7](https://github.com/upstash/context7)

**项目核心内容总结：**

**1. 项目功能**  
Context7 是一个基于 Model Context Protocol (MCP) 的服务器工具，旨在帮助大语言模型（LLM）快速访问和检索代码库的文档与信息。其核心功能包括：  
- 通过 `resolve-library-id` 工具将通用库名转换为 Context7 兼容的唯一库 ID。  
- 通过 `get-library-docs` 工具按库 ID 获取文档，并支持按主题（如“路由”“钩子”）和分页查询。  

**2. 使用方法**  
- **安装配置**：支持通过 `npx`、`bunx` 或 `deno` 安装，需配置 API 密钥（可通过环境变量或命令行参数设置）。  
- **集成开发环境**：提供针对 VS Code、LM Studio 等工具的安装指南，支持自定义规则（如自动触发 Context7 查询代码相关问题）。  
- **本地运行**：通过 `bun run` 启动服务，支持 `stdio`（本地集成）或 `http`（远程服务器）传输方式，可自定义端口。  

**3. 主要特性**  
- **灵活配置**：支持环境变量（如 `CONTEXT7_API_KEY`）和 `.env` 文件管理密钥，适配多种 MCP 客户端。  
- **错误处理**：提供常见问题解决方案，如使用 `bunx` 替代 `npx` 解决模块未找到问题，或通过 `--experimental-fetch` 绕过 TLS 证书限制。  
- **跨平台兼容**：适配 Node.js 18+，支持 Deno 等替代工具，确保在不同开发环境中的稳定性。  

**适用场景**：适用于需要快速查询库文档、提升代码辅助工具（如 Cursor、Codex）效率的开发者及团队。