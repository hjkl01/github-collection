### [korotovsky slack-mcp-server](https://github.com/korotovsky/slack-mcp-server)  ![GitHub Repo stars](https://img.shields.io/github/stars/korotovsky/slack-mcp-server?style=social)

本项目是一个专为 Slack 工作区设计的 Model Context Protocol (MCP) 服务器，支持 Stdio、SSE 和 HTTP 传输及代理配置。

核心功能：
1. **认证与接入**：支持隐身模式（无需额外权限）和 OAuth 模式，兼容企业工作区。
2. **消息处理**：获取频道、线程、DM 及群 DM 的消息历史（支持按日期/数量分页），提供多维度搜索、未读消息获取（含优先级排序）及标记已读功能。
3. **交互操作**：支持安全发布消息（默认禁用）及添加/移除表情反应。
4. **资源管理**：检索用户与频道列表，管理用户分组（创建、更新、成员变更），并提供目录资源。
5. **性能与安全**：内置用户和频道缓存，通过环境变量精细控制工具权限。