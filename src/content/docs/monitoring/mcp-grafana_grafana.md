
---
title: mcp-grafana
---

### [grafana mcp-grafana](https://github.com/grafana/mcp-grafana)  ![GitHub Repo stars](https://img.shields.io/github/stars/grafana/mcp-grafana?style=social)

Grafana MCP Server 是为 Grafana 提供的 Model Context Protocol (MCP) 服务器，旨在让 AI 客户端（如 Claude、Cursor）能够访问和操作 Grafana 实例及其生态系统。

**核心功能**
1. **看板管理**：支持搜索、获取详情/摘要、创建、更新、补丁看板及提取面板查询。
2. **多数据源查询**：支持 Prometheus、Loki、ClickHouse、CloudWatch、Elasticsearch 等数据源的查询与元数据获取。
3. **告警与通知**：管理告警规则状态、通知策略及联系点。
4. **事件与 OnCall**：管理 Grafana Incident、Sift 调查分析及 OnCall 值班调度。
5. **系统管理**：管理用户、团队、角色权限及资源描述。
6. **辅助工具**：生成深度链接、渲染看板图片、管理注解及日志搜索。

**配置与安全**
*   支持按需启用/禁用工具类别，提供只读模式。
*   兼容 Grafana 9.0+，支持 RBAC 权限控制、多组织及 Service Account Token 认证。
*   支持 uvx、Docker、Helm 等多种部署方式。
*   支持 stdio、SSE、streamable-http 传输协议、TLS 配置及 Prometheus 指标监控。