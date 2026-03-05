
---
title: nightingale
---

### [ccfos nightingale](https://github.com/ccfos/nightingale)  ![GitHub Repo stars](https://img.shields.io/github/stars/ccfos/nightingale?style=social)

Nightingale（N9E）是一款专注于告警能力的开源监控系统，核心职责为告警生成、处理与分发，而非数据可视化或采集。

1. **告警管理**：支持告警、静默、订阅及通知规则，内置 20 种通知渠道（如钉钉、短信、电话），支持事件流水线处理与告警自愈脚本。
2. **数据集成**：不直接采集监控数据，兼容 Prometheus、VictoriaMetrics、ElasticSearch 等多种数据源，推荐配合 Categraf 采集器使用。
3. **部署架构**：支持分布式边缘部署模式，适应弱网环境下的本地告警处理，保障告警服务可用性。
4. **业务与可视化**：提供内置仪表盘、预置监控模板及历史告警查询，基于业务组进行权限管理与规则分类。
5. **系统扩展**：支持嵌入企业内部系统（如 CMDB、Grafana），兼容多种数据采集协议，并提供 MCP Server 支持 AI 助手交互。