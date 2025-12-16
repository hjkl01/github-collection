
---
title: nightingale
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/ccfos/nightingale?style=social) ](https://github.com/ccfos/nightingale)
### [ccfos nightingale](https://github.com/ccfos/nightingale)

**Nightingale 核心内容总结**  

**项目功能**  
Nightingale 是一个开源的监控告警系统，专注于告警规则配置、告警生成与分发。不提供数据采集功能，需通过 [Categraf](https://github.com/flashcatcloud/categraf) 等工具采集数据并推送到 Nightingale。支持对接多种数据源（如 VictoriaMetrics、ElasticSearch、Prometheus 等），提供告警规则、静默规则、通知规则配置，支持 20 种通知渠道（如电话、邮件、Slack 等）。  

**使用方法**  
1. 通过 Categraf 等采集器收集监控数据，使用 Prometheus Remote Write 协议推送至 Nightingale。  
2. 在 Nightingale 中配置告警规则、通知规则，对接数据源（如 Prometheus、VictoriaMetrics）。  
3. 支持分布式部署，边缘数据中心可部署 `n9e-edge` 以实现断网环境下的告警处理。  

**主要特性**  
- **告警规则**：支持复杂告警逻辑、静默规则、订阅规则，可导入 Prometheus 原生规则。  
- **通知管理**：20 种通知渠道（电话、短信、邮件、DingTalk 等），支持自定义消息模板。  
- **事件处理**：支持事件流水线（Pipeline）处理，可自动执行脚本（如清理磁盘、采集系统状态）。  
- **权限与分类**：通过“业务组”划分权限，分类管理规则与数据。  
- **历史分析**：存储历史告警，支持多维查询与统计，可视化告警分布。  
- **集成能力**：兼容多种协议（Remote Write、OpenTSDB、Falcon 等），支持对接 Grafana、CMDB 等系统。  
- **自愈功能**：告警触发后自动执行预设修复逻辑。