
---
title: registry
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/modelcontextprotocol/registry?style=social) ](https://github.com/modelcontextprotocol/registry)
### [modelcontextprotocol registry](https://github.com/modelcontextprotocol/registry)

**MCP Registry 核心内容总结：**

**项目功能**  
MCP Registry 是一个为 MCP 客户端提供 MCP 服务器列表的目录服务，功能类似“应用商店”，帮助用户发现和管理 MCP 服务器。

**使用方法**  
1. **开发环境启动**：通过 `make dev-compose` 命令启动本地开发环境（含 PostgreSQL 数据库），默认从生产环境同步部分数据。  
2. **发布服务器**：使用内置 CLI 工具 `mcp-publisher` 发布服务器，需通过 GitHub OAuth、DNS 或 HTTP 验证所有权。  
3. **Docker 部署**：支持直接运行预构建的 Docker 镜像（如 `ghcr.io/modelcontextprotocol/registry:latest`）。  

**主要特性**  
- **API 稳定性**：当前 API 版本为 v0.1，已进入“冻结期”（未来一个月内无破坏性变更）。  
- **多认证方式**：支持 GitHub OAuth、GitHub OIDC、DNS 验证和 HTTP 验证，确保发布者身份合法性。  
- **模块化架构**：代码分层清晰，包含 API 处理、数据库、验证逻辑、认证模块等。  
- **社区驱动**：提供文档、讨论区和 Discord 渠道，鼓励社区参与开发与反馈。  

**其他**  
- 当前为预览版，可能有数据重置或功能变更。  
- 支持通过 GitHub Actions 自动化发布（需 OIDC 验证）。