
---
title: slack-mcp-server
---

### [korotovsky slack-mcp-server](https://github.com/korotovsky/slack-mcp-server)  ![GitHub Repo stars](https://img.shields.io/github/stars/korotovsky/slack-mcp-server?style=social)

**项目核心内容总结：**

该项目是一个用于Slack的Model Context Protocol（MCP）服务器，提供对Slack工作区的深度访问功能。  

**功能：**  
- **认证支持**：支持多种Slack令牌类型（如用户令牌`xoxp`、机器人令牌`xoxb`、浏览器令牌`xoxc/xoxd`），适用于不同使用场景。  
- **消息操作**：提供消息获取、搜索（支持通过用户名`@userHandle`或频道名`#channel-name`）、发送（需启用`SLACK_MCP_ADD_MESSAGE_TOOL`）等功能。  
- **目录资源**：通过`slack://<workspace>/channels`和`slack://<workspace>/users`获取工作区频道和用户信息的CSV格式数据。  
- **缓存机制**：支持用户和频道信息的本地缓存，提升性能并减少API调用。  

**使用方法：**  
1. **配置环境变量**：设置认证令牌（如`SLACK_MCP_XOXC_TOKEN`）、端口（默认`13080`）、代理等参数。  
2. **安装与运行**：通过文档指引完成安装，启动MCP服务器。  
3. **调试与日志**：使用`npx @modelcontextprotocol/inspector`工具调试，通过日志文件（如`~/Library/Logs/Claude/mcp*.log`）查看运行状态。  

**主要特性：**  
- 支持多认证方式（用户、机器人、浏览器令牌）。  
- 提供消息搜索、发送、频道/用户目录查询等工具。  
- 可配置代理、自定义TLS、缓存路径及日志级别。  
- 通过缓存提升性能，无缓存时部分功能受限。  

**注意事项：**  
- 安全性：严禁泄露API令牌，确保`.env`文件安全。  
- 限制：未启用缓存时，部分功能（如消息搜索、频道列表）受限。