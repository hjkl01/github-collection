
---
title: loggie
---

### [loggie-io loggie](https://github.com/loggie-io/loggie)  ![GitHub Repo stars](https://img.shields.io/github/stars/loggie-io/loggie?style=social)

Loggie 是一款基于 Golang 的轻量级、高性能云原生日志代理与聚合器。
- **配置与管理**：支持通过 Kubernetes CRD 定义多管道，实现日志的采集、传输、过滤、解析及告警组件配置。
- **部署架构**：提供 Agent（DaemonSet）、Sidecar（自动注入）及 Aggregator（独立中间节点）三种部署模式。
- **高性能传输**：具备自适应 Sink 并发调节能力，相比竞品资源占用更低，传输效率更高。
- **流式处理**：支持实时日志解析（JSON/Grok 等）、字段转换、条件逻辑处理及基于日志的指标聚合（如 QPS、错误率统计）。
- **可观测性**：内置 Prometheus 指标，支持自定义告警规则（Webhook）及 Grafana 监控大盘。
适用于构建云原生环境下的可扩展日志数据平台。