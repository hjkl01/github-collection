
---
title: registry
---

### [modelcontextprotocol registry](https://github.com/modelcontextprotocol/registry)  ![GitHub Repo stars](https://img.shields.io/github/stars/modelcontextprotocol/registry?style=social)

MCP Registry 是一个面向 MCP 生态的服务器注册中心，功能类似于应用商店，旨在为 MCP 客户端提供 MCP 服务器的列表与发现服务。

核心功能如下：
1. **服务器发布**：提供 CLI 工具，支持通过 GitHub OAuth、OIDC 或 DNS/HTTP 验证等方式发布 MCP 服务器并校验命名空间所有权。
2. **API 服务**：提供查询 MCP 服务器的 API 接口，当前 v0.1 版本已冻结以确保集成稳定性。
3. **开发与部署**：基于 Go 语言和 PostgreSQL 构建，支持 Docker 本地环境搭建及容器化部署。