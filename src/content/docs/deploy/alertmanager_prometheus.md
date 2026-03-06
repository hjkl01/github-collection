
---
title: alertmanager
---

### [prometheus alertmanager](https://github.com/prometheus/alertmanager)  ![GitHub Repo stars](https://img.shields.io/github/stars/prometheus/alertmanager?style=social)

Alertmanager 是 Prometheus 的告警管理组件，负责处理来自客户端应用（如 Prometheus 服务器）的告警。核心功能包括告警去重、分组、路由至多种接收器（如邮件、PagerDuty、OpsGenie 及 Webhook）、告警静默与抑制。它支持 YAML 配置路由规则，提供 v2 API 接口，并附带 CLI 工具 amtool 用于告警查询和管理。项目支持高可用集群部署，Prometheus 向所有实例发送告警以确保系统可靠性。