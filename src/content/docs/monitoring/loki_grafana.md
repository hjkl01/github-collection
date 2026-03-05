
---
title: loki
---

### [grafana loki](https://github.com/grafana/loki)  ![GitHub Repo stars](https://img.shields.io/github/stars/grafana/loki?style=social)

Loki 是一个水平可扩展、高可用、多租户的日志聚合系统，受 Prometheus 启发。它不对日志内容进行全文索引，仅基于标签元数据进行存储和查询，从而降低成本并简化运维。Loki 使用与 Prometheus 相同的标签机制，支持指标与日志的无缝关联查询，特别适用于 Kubernetes 环境。其日志栈由三个主要组件构成：Alloy（负责日志采集与发送）、Loki（负责日志存储与查询处理）以及 Grafana（负责日志查询与展示）。