
---
title: mcp-gateway
---

### [docker mcp-gateway](https://github.com/docker/mcp-gateway)  ![GitHub Repo stars](https://img.shields.io/github/stars/docker/mcp-gateway?style=social)

**项目核心内容总结：**

**项目功能**  
该项目提供 Docker MCP CLI 插件和 MCP 网关工具，用于管理运行在 Docker 容器中的 [Model Context Protocol (MCP)](https://spec.modelcontextprotocol.io/) 服务器。支持通过统一网关调用 MCP 工具、资源和提示，集成 Docker Desktop 的秘密管理、OAuth 认证等功能，实现安全、便捷的 MCP 服务部署与使用。

**主要特性**  
- 容器化 MCP 服务器：以 Docker 容器运行 MCP 服务，确保隔离性。  
- 服务器管理：支持启用/禁用服务器、查看服务器信息、重置配置。  
- 秘密管理：通过 Docker Desktop 安全存储 API 密钥等敏感信息。  
- OAuth 集成：支持 OAuth 认证流程。  
- 动态发现：自动发现运行中的工具、提示和资源。  
- 日志与监控：内置日志记录和调用追踪功能。  

**使用方法**  
1. **安装**  
   - 需 Docker Desktop（启用 MCP 工具包）和 Go 1.24+。  
   - 克隆仓库并构建插件：`make docker-mcp`，安装后通过 `docker mcp --help` 使用。  

2. **操作命令**  
   - **目录管理**：初始化默认目录、列出目录、展示服务器信息（如 `docker mcp catalog init`）。  
   - **网关启动**：通过 `docker mcp gateway run` 启动网关，支持 `stdio` 或 `streaming` 传输模式。  
   - **服务器管理**：启用/禁用服务器（如 `docker mcp server enable <name>`）。  
   - **配置管理**：读取/写入配置文件（如 `docker mcp config read`）。  
   - **工具调用**：列出工具、调用工具（如 `docker mcp tools call <tool-name>`）。  

**核心价值**  
通过标准化协议（MCP）和 Docker 工具链，简化 AI 应用与外部数据源的集成，提供统一接口、安全认证和动态配置能力。