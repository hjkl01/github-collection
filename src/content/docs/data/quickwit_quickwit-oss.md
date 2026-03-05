
---
title: quickwit
---

### [quickwit-oss quickwit](https://github.com/quickwit-oss/quickwit)  ![GitHub Repo stars](https://img.shields.io/github/stars/quickwit-oss/quickwit?style=social)

Quickwit 是一款专为可观测性（日志、链路追踪及即将支持的指标）设计的云原生开源搜索引擎，旨在作为 Datadog、Elasticsearch、Loki 和 Tempo 的替代方案。其核心功能包括基于云存储（如 S3、Azure Blob、GCS）的亚秒级全文搜索与聚合查询，兼容 Elasticsearch/OpenSearch API，原生支持 Jaeger 和 OpenTelemetry。项目采用计算与存储解耦的架构，支持 Kubernetes 部署，提供多数据源、多租户、保留策略、GDPR 合规删除等企业级特性，宣称成本比 Elastic 低 10 倍，遵循 Apache 2.0 开源协议。