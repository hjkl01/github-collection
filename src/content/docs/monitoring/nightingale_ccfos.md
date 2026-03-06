
---
title: nightingale
---

### [ccfos nightingale](https://github.com/ccfos/nightingale)  ![GitHub Repo stars](https://img.shields.io/github/stars/ccfos/nightingale?style=social)

Nightingale（夜莺）是一款开源云原生监控项目，核心专注于告警引擎及告警流转分发。

**核心功能：**
1. **数据采集**：不自带采集能力，推荐配合 Categraf 使用，支持通过 Prometheus Remote Write 等协议接收数据，存储于时序数据库（如 Prometheus、VictoriaMetrics）。
2. **告警管理**：支持告警、静音、订阅及通知规则，内置 20 多种通知媒介，支持消息模板自定义及 Prometheus 规则导入。
3. **事件处理**：支持告警流水线处理、告警自愈合（触发脚本执行）及历史告警归档查询。
4. **组织集成**：基于业务组管理权限；支持多种数据源（ES、Loki 等）；可嵌入内部系统；支持分布式边缘部署；支持 MCP Server 与 AI 助手交互。
5. **可视化**：内置仪表盘，复杂场景推荐结合 Grafana 使用。

**适用边界：**
专注告警生成与分发，复杂的值班排班、升级及协同处理建议选用 PagerDuty 等专业产品。