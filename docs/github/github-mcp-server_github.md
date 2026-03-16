### [github github-mcp-server](https://github.com/github/github-mcp-server)  ![GitHub Repo stars](https://img.shields.io/github/stars/github/github-mcp-server?style=social)

GitHub MCP Server 旨在连接 AI 工具与 GitHub 平台，使 AI 代理能通过自然语言交互直接操作 GitHub 资源。

**核心功能：**
*   **仓库管理**：浏览代码、搜索文件、分析提交记录及项目结构。
*   **Issue 与 PR 自动化**：创建、更新及管理问题与拉取请求，辅助代码审查与任务分类。
*   **CI/CD 与流程智能**：监控 GitHub Actions 运行、分析构建失败及管理发布。
*   **代码安全分析**：检查安全警报、Dependabot 通知及代码漏洞洞察。
*   **团队协作**：管理讨论、通知及团队活动。

**部署与配置：**
*   支持**远程服务器**（GitHub 托管）和**本地服务器**（Docker/Go 构建），兼容 GitHub Enterprise 环境。
*   适配 VS Code、Claude Desktop、Cursor 等多种 MCP 主机。
*   支持通过**工具集**（如 repos, issues, actions 等）灵活控制可用功能。
*   提供**只读模式**、**锁定模式**及动态工具发现功能。