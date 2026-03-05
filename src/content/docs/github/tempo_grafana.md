
---
title: tempo
---

### [grafana tempo](https://github.com/grafana/tempo)  ![GitHub Repo stars](https://img.shields.io/github/stars/grafana/tempo?style=social)

Grafana Tempo 是一个开源、易用且支持高扩展的分布式追踪后端。该项目仅需对象存储即可低成本运行，并与 Grafana、Prometheus 及 Loki 深度集成。

主要功能包括：
1. 多协议兼容：支持接收 Jaeger、Zipkin、Kafka 和 OpenTelemetry 格式的数据。
2. 灵活存储：支持将数据缓冲后写入 Azure、GCS、S3 或本地磁盘。
3. TraceQL 查询：提供专用的追踪查询语言，支持基于追踪数据创建指标。
4. 直观分析：集成 Traces Drilldown UI，提供无需编写复杂查询即可分析追踪、定位性能瓶颈和错误的界面。
5. 辅助工具：包含 tempo-vulture（一致性检查）和 tempo-cli 等实用工具。