
---
title: mcp-grafana
---

### [grafana mcp-grafana](https://github.com/grafana/mcp-grafana)  ![GitHub Repo stars](https://img.shields.io/github/stars/grafana/mcp-grafana?style=social)

这是一个为 Grafana 设计的 Model Context Protocol (MCP) 服务器，旨在让 AI 客户端（如 Claude Desktop、Cursor）安全访问和操作 Grafana 实例及其生态系统。

**核心功能：**
*   **仪表板管理**：支持搜索、获取详情/摘要/特定属性、创建/更新/补丁、提取面板查询信息。
*   **数据查询**：支持对 Prometheus (PromQL)、Loki (LogQL)、ClickHouse (SQL)、CloudWatch、Elasticsearch、Pyroscope 执行查询和元数据获取。
*   **告警与通知**：管理 Grafana 告警规则（增删改查）及通知策略（联系人、路由）。
*   **事件与调查**：管理 Grafana Incidents（创建、更新、搜索）及 Sift Investigations（分析日志错误、检测慢请求）。
*   **OnCall 管理**：管理 OnCall 排班、轮值人员、团队、用户及告警组。
*   **系统工具**：管理用户、团队、角色及权限；生成资源深度链接；管理注解；渲染仪表板/面板为 PNG 图片。
*   **部署与安全**：支持 uvx、Docker、二进制及 Helm 部署；提供 stdio、SSE、streamable-http 传输模式；支持 RBAC 权限控制、TLS 加密及只读模式配置。