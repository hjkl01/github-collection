
---
title: github-mcp-server
---

### [github github-mcp-server](https://github.com/github/github-mcp-server)

### 核心内容总结

**项目功能**  
GitHub MCP Server 是一个提供多种 GitHub 交互工具的服务器，支持仓库管理（如分支创建、拉取请求、问题处理）、用户搜索、Copilot 代码助手集成、安全建议管理、星标仓库操作等功能。包含 200+ 工具，覆盖仓库操作、用户管理、安全分析、文档搜索等场景。

**使用方法**  
1. **命令行启动**：通过 `--dynamic-toolsets` 启用动态工具发现，或 `--read-only` 启用只读模式，或 `--lockdown-mode` 启用锁定模式。  
2. **Docker 部署**：通过环境变量（如 `GITHUB_DYNAMIC_TOOLSETS=1`）配置功能模式，需设置 GitHub 个人访问令牌。  
3. **多语言支持**：可通过配置文件或环境变量覆盖工具描述（如 `GITHUB_MCP_TOOL_CREATE_BRANCH_DESCRIPTION`）。

**主要特性**  
- **动态工具发现**：按需加载工具集，避免工具冗余。  
- **安全模式**：  
  - **只读模式**：禁止所有写操作。  
  - **锁定模式**：过滤无推送权限用户的公开仓库内容。  
- **Copilot 集成**：支持通过 Copilot 自动创建拉取请求。  
- **文档搜索**：提供 GitHub 官方文档检索功能（如 Actions、Packages 等）。  
- **多语言配置**：支持工具描述的本地化覆盖。