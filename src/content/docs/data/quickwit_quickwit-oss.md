
---
title: quickwit
---

### [quickwit-oss quickwit](https://github.com/quickwit-oss/quickwit)  ![GitHub Repo stars](https://img.shields.io/github/stars/quickwit-oss/quickwit?style=social)

Quickwit 是一个云原生的开源搜索引擎，专注于可观测性场景（日志、追踪，未来将支持指标），可作为 Datadog、Elasticsearch、Loki 和 Tempo 的替代方案。其核心功能包括：

### 项目功能
- **日志管理**：支持快速搜索与分析日志数据。
- **分布式追踪**：支持与 Jaeger 集成，进行分布式追踪分析。
- **兼容 Elasticsearch 接口**：支持 Elasticsearch 和 OpenSearch 的客户端，可直接替换使用。
- **支持 OTLP 协议**：可直接接收 OpenTelemetry 的日志和追踪数据。
- **多云存储支持**：可在 Amazon S3、Azure Blob Storage、Google Cloud Storage 等云存储上进行搜索。
- **无状态架构**：计算与存储分离，支持快速扩展。

### 使用方法
- 提供 RESTful API 和 Elasticsearch 兼容接口。
- 支持通过 Kafka、Kinesis、Pulsar 等消息队列进行数据摄入。
- 提供 Helm Chart 用于 Kubernetes 部署。
- 支持通过 Grafana 进行可视化。

### 主要特性
- 支持全文搜索与聚合查询。
- 支持无模式（schemaless）或严格模式的数据索引。
- 搜索响应时间极短，适合大规模数据场景。
- 支持多租户、索引分区、数据保留策略。
- 支持删除任务，满足 GDPR 等合规要求。
- 高可用性架构（搜索部分 HA，索引部分需 Kafka 支持）。

### 优势
- 相比 Elastic 可降低成本高达 10 倍。
- 基于云存储优化，性能更优。
- 开源，采用 Apache 2.0 协议。

Quickwit 的目标是成为新一代的可观测性数据处理引擎，提供高性能、低成本、易扩展的搜索解决方案。