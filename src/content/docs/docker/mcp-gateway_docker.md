
---
title: mcp-gateway
---

### [docker mcp-gateway](https://github.com/docker/mcp-gateway)  ![GitHub Repo stars](https://img.shields.io/github/stars/docker/mcp-gateway?style=social)

该项目是 Docker MCP CLI 插件（docker-mcp），提供 Docker MCP 网关功能，旨在帮助开发者安全便捷地运行和部署 MCP（Model Context Protocol）服务器。核心功能如下：

- **容器化部署**：将 MCP 服务器封装为 Docker 容器，实现隔离运行与生命周期管理。
- **统一网关访问**：为 AI 客户端（如 Cursor、Claude Desktop）提供单一接口，连接并调用多个 MCP 服务器的工具、资源及提示。
- **安全管理**：利用 Docker 机制管理密钥凭证，内置 OAuth 认证流，避免敏感信息通过环境变量泄露。
- **配置与目录管理**：支持通过 Profile 分组服务器并导出共享，可管理 OCI 目录，支持动态工具发现及工具权限控制。
- **跨环境兼容**：既可在 Docker Desktop 中作为特性使用，也可作为独立 CLI 插件在 WSL2 或容器化环境中运行。