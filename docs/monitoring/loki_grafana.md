### [grafana loki](https://github.com/grafana/loki)  ![GitHub Repo stars](https://img.shields.io/github/stars/grafana/loki?style=social)

Loki 是一个水平可扩展、高可用、多租户的日志聚合系统，灵感源自 Prometheus。它不索引日志内容，仅对日志流进行标签元数据索引，具有成本低、易运维的特点。系统支持与 Prometheus 相同的标签体系，便于指标与日志的无缝关联，特别适用于 Kubernetes Pod 日志。Loki 日志栈由三个核心组件构成：Alloy（负责日志采集，替代 Promtail）、Loki（负责日志存储与查询）、Grafana（负责日志展示）。该项目设计为无依赖、易操作，支持单二进制运行，并原生集成于 Grafana。