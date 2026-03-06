
---
title: quickwit
---

### [quickwit-oss quickwit](https://github.com/quickwit-oss/quickwit)  ![GitHub Repo stars](https://img.shields.io/github/stars/quickwit-oss/quickwit?style=social)

Quickwit 是一款面向可观测性（日志、追踪及未来指标）的云原生开源搜索引擎，作为 Datadog、Elasticsearch 和 Loki 的替代品。

核心功能总结：
1. **云存储优化搜索**：针对云存储（S3、Azure Blob 等）优化 IO，采用存算分离架构，实现亚秒级搜索且成本显著低于传统方案。
2. **高兼容性**：提供 Elasticsearch/OpenSearch 兼容 API，原生支持 Jaeger 和 OpenTelemetry，便于迁移和集成现有客户端。
3. **灵活索引与分析**：支持全文搜索、聚合查询及无模式/严格模式索引，兼容 Kafka/Kinesis 等多种数据源。
4. **企业级特性**：支持 Kubernetes 部署、多租户管理、生命周期策略、GDPR 数据删除任务及高可用架构。