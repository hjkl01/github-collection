
---
title: signoz
---

### [SigNoz signoz](https://github.com/SigNoz/signoz)  ![GitHub Repo stars](https://img.shields.io/github/stars/SigNoz/signoz?style=social)

SigNoz 是一个基于 OpenTelemetry 的开源可观测性平台，集成了日志、指标和分布式追踪，可作为 Datadog 和 New Relic 的替代方案。

**核心功能：**
*   **APM**：监控应用及服务的延迟、错误率、Apdex 及数据库/外部调用。
*   **日志管理**：基于 ClickHouse 的集中式日志存储、快速搜索与可视化。
*   **分布式追踪**：追踪微服务请求链路，利用火焰图和甘特图定位瓶颈。
*   **指标与仪表盘**：自定义仪表盘，支持 PromQL 和 ClickHouse 查询。
*   **LLM 可观测性**：监控大模型调用、Token 使用及成本。
*   **告警与异常**：基于多信号阈值告警，支持代码异常堆栈追踪。

平台支持云、Docker 及 Kubernetes 部署，兼容多种编程语言，通过关联日志、指标和追踪数据提供丰富调试上下文。