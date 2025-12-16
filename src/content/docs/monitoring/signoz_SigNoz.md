
---
title: signoz
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/SigNoz/signoz?style=social) ](https://github.com/SigNoz/signoz)
### [SigNoz signoz](https://github.com/SigNoz/signoz)

### 核心内容总结

**项目功能**  
SigNoz 是一个开源的可观测性平台，整合日志、指标和分布式追踪功能，支持应用性能监控（APM）、日志管理、异常监控、自定义仪表盘及告警。  
- **APM**：实时监控应用性能，提供延迟、错误率、Apdex 等关键指标图表。  
- **日志管理**：基于 ClickHouse 的高速日志存储，支持快速搜索、过滤及日志数据可视化。  
- **分布式追踪**：通过 OpenTelemetry 跟踪微服务请求，支持火焰图、甘特图分析性能瓶颈。  
- **指标与仪表盘**：自定义监控面板，支持多种图表类型及复杂查询。  
- **告警**：对日志、指标、追踪设置阈值告警，支持通知渠道及异常检测。  
- **异常监控**：自动捕获 Python/Java/Ruby/JavaScript 等语言的异常，支持自定义属性分析。  

**使用方法**  
- **云服务**：通过 [SigNoz Cloud](https://signoz.io/teams/) 快速部署，无需维护。  
- **自托管**：使用 Docker 或 Kubernetes Helm Chart 安装，文档提供详细步骤。  

**主要特性**  
- 集成日志、指标、追踪三大可观测性数据。  
- 基于 OpenTelemetry，避免厂商锁定。  
- 使用 ClickHouse 实现高效日志聚合分析。  
- 支持多语言（含 Rust/Swift/Python 等）。  
- 对比竞品（如 Prometheus、Jaeger、Elastic）具备更低资源消耗、更高效查询能力。  

**开源与社区**  
提供完整文档，支持贡献代码，维护团队涵盖前后端及 DevOps，社区活跃。