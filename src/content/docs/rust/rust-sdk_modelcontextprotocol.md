
---
title: rust-sdk
---

### [modelcontextprotocol rust-sdk](https://github.com/modelcontextprotocol/rust-sdk)  ![GitHub Repo stars](https://img.shields.io/github/stars/modelcontextprotocol/rust-sdk?style=social)

RMCP 是 Model Context Protocol (MCP) 的官方 Rust 实现 SDK，基于 tokio 异步运行时。核心包含协议实现 crate (rmcp) 与工具生成宏 (rmcp-macros)，支持构建 MCP 客户端与服务器。功能涵盖资源管理（数据暴露、URI 模板）、提示词模板、采样（服务器请求客户端调用 LLM）、根目录（工作区范围）、日志记录、参数补全、通知机制（进度、取消、状态变更）及资源订阅。支持 OAuth 认证，并提供示例代码与第三方扩展生态。