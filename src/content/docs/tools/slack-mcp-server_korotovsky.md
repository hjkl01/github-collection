
---
title: slack-mcp-server
---

### [korotovsky slack-mcp-server](https://github.com/korotovsky/slack-mcp-server)  ![GitHub Repo stars](https://img.shields.io/github/stars/korotovsky/slack-mcp-server?style=social)

本项目是一个 Slack 工作区的 Model Context Protocol (MCP) 服务器，支持 Stdio、SSE 和 HTTP 传输。核心功能包括：

1. **认证与模式**：支持 OAuth 或静默模式（浏览器 Token），无需额外权限即可使用，兼容企业级设置。
2. **消息操作**：获取频道及私聊的历史消息与线程回复（支持分页）；搜索消息（支持多条件过滤）；支持安全配置下的消息发送、表情反应增删及标记已读。
3. **信息与管理**：获取未读消息（支持优先级排序）；列出频道、用户；管理用户组（增删改查成员及成员组）。
4. **优化与安全**：支持用户和频道缓存；敏感操作默认禁用，需环境变量启用；支持代理及 GovSlack 模式。