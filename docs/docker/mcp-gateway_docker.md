### [docker mcp-gateway](https://github.com/docker/mcp-gateway)  ![GitHub Repo stars](https://img.shields.io/github/stars/docker/mcp-gateway?style=social)

本项目是 Docker MCP 插件与网关（docker-mcp），用于安全地运行和管理 Model Context Protocol (MCP) 服务器，实现 AI 应用与外部工具的数据连接。

主要功能：
1. **MCP 网关**：作为统一接口，让 AI 客户端（如 VS Code、Cursor、Claude）连接并访问 MCP 服务。
2. **容器化运行**：MCP 服务器以 Docker 容器形式运行，提供隔离与安全。
3. **配置管理**：支持通过 Profile 分组管理服务器，支持目录、OCI 镜像及本地文件等多种来源，可导出/导入配置。
4. **安全管理**：利用 Docker Desktop 管理密钥，内置 OAuth 流，避免敏感凭据泄露。
5. **工具与动态发现**：自动发现工具、资源和提示，支持工具启用/禁用及调用，提供日志追踪。
6. **客户端管理**：管理 AI 客户端与网关的连接状态。

该插件既可在 Docker Desktop 中使用，也可作为独立 CLI 运行。