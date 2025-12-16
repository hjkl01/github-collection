
---
title: rust-sdk
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/modelcontextprotocol/rust-sdk?style=social) ](https://github.com/modelcontextprotocol/rust-sdk)
### [modelcontextprotocol rust-sdk](https://github.com/modelcontextprotocol/rust-sdk)

**项目核心内容总结：**

**项目功能**  
RMCP 是 Model Context Protocol（MCP）的官方 Rust SDK 实现，基于 tokio 异步运行时，提供协议核心功能及代码生成工具，支持构建客户端/服务端应用。

**使用方法**  
1. **依赖导入**：通过 `Cargo.toml` 引入 `rmcp`（支持 `server` 功能）或开发分支。  
2. **依赖项**：需使用 `tokio`、`serde` 和 `schemars`（用于 JSON Schema 生成）。  
3. **客户端构建**：通过 `TokioChildProcess` 启动子进程连接服务端。  
4. **服务端构建**：定义服务逻辑（如 `Counter`），结合 `stdin/stdout` 传输层启动服务，支持请求/通知交互及服务关闭监听。

**主要特性**  
- 提供异步运行时支持，适配 tokio 生态；  
- 包含代码生成宏（`rmcp-macros`），简化工具实现；  
- 支持 OAuth 认证；  
- 提供多个扩展项目（如 `actix-web` 后端、OpenAPI 转换工具）及实际应用案例（如 S3 兼容存储、容器管理、Neovim 插件等）。