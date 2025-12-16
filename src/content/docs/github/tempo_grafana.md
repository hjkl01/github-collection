
---
title: tempo
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/grafana/tempo?style=social) ](https://github.com/grafana/tempo)
### [grafana tempo](https://github.com/grafana/tempo)

**核心内容总结：**

**项目功能**  
Grafana Tempo 是一个开源的分布式追踪后端，支持与 Grafana、Prometheus 和 Loki 深度集成，仅需对象存储即可运行，具备高扩展性和低成本特性。兼容 Jaeger、Zipkin、OpenTelemetry 等多种数据格式，支持将追踪数据写入 Azure、GCS、S3 或本地磁盘。

**主要特性**  
1. **Traces Drilldown UI**：提供无需查询的交互式分析界面，支持快速定位性能问题、错误和延迟瓶颈，集成 RED 指标（速率、错误率、持续时间）和自动对比功能。  
2. **TraceQL**：基于 LogQL 和 PromQL 的查询语言，支持复杂查询和指标生成（实验性功能）。  
3. **低成本存储**：依赖对象存储，无需额外数据库，简化运维。  
4. **工具链**：包含 `tempo-vulture`（一致性校验工具）和 `tempo-cli`（命令行工具）。  

**使用方法**  
- 通过官方文档 [Getting Started](https://grafana.com/docs/tempo/latest/getting-started/) 部署。  
- 支持多种部署方式：[Docker Compose](./example/docker-compose)、[Helm](./example/helm)、[Jsonnet](./example/tk)。  
- 参考 [OpenTelemetry 集成指南](https://grafana.com/docs/tempo/latest/guides/instrumentation/) 进行应用埋点。  

**许可证**  
采用 AGPL-3.0-only 许可，部分组件支持 Apache-2.0 异常许可。