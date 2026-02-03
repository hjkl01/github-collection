
---
title: slack-mcp-server
---

### [korotovsky slack-mcp-server](https://github.com/korotovsky/slack-mcp-server)  ![GitHub Repo stars](https://img.shields.io/github/stars/korotovsky/slack-mcp-server?style=social)

**项目核心内容总结：**  
Slack MCP Server 是一个用于与 Slack 平台交互的工具，支持通过多种身份验证方式（如 `xoxc`、`xoxd`、`xoxp`、`xoxb` 令牌）连接，并提供多种传输协议（如 stdio、SSE、HTTP）。主要功能包括：  
1. **频道与用户管理**：获取频道列表（支持公共、私有、DM 等类型）、用户目录（含用户 ID、姓名等信息）。  
2. **消息操作**：支持发送消息、搜索消息（按用户、频道、关键词等）、标记消息为已读等。  
3. **缓存机制**：通过用户和频道缓存减少重复 API 请求，提升性能。  
4. **灵活配置**：支持代理设置、自定义 User-Agent、TLS 握手、日志级别（info/debug 等）等。  

**使用方法**：  
- 安装并配置环境变量（如 `SLACK_MCP_XOXC_TOKEN`、`SLACK_MCP_PORT` 等）。  
- 运行服务器，通过指定传输方式（如 `stdio`）启动。  
- 使用工具（如 `inspector`）调试或查看日志。  

**主要特性**：  
- 支持多种 Slack 令牌认证方式。  
- 提供频道和用户信息的 CSV 格式导出。  
- 可自定义代理、缓存路径、日志输出等。  
- 安全措施：强调保护 API 令牌和配置文件。  

**注意事项**：  
- 不得共享 API 令牌，确保 `.env` 文件安全。  
- 默认禁用消息发送功能，需通过 `SLACK_MCP_ADD_MESSAGE_TOOL` 开启。  
- 许可证为 MIT，非官方 Slack 产品。