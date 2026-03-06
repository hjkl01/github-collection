
---
title: signoz
---

### [SigNoz signoz](https://github.com/SigNoz/signoz)  ![GitHub Repo stars](https://img.shields.io/github/stars/SigNoz/signoz?style=social)

SigNoz 是一款开源的、基于 OpenTelemetry 标准的可观测性平台，提供日志、指标和链路追踪的一站式解决方案，是 Datadog 和 New Relic 的替代产品。

核心功能包括：
*   **应用性能监控 (APM)**：监控应用及服务，提供 p99 延迟、错误率、Apdex 等关键指标。
*   **日志管理**：基于 ClickHouse 存储，支持快速搜索、查询构建及自定义日志仪表盘。
*   **分布式追踪**：追踪微服务请求，通过火焰图和甘特图帮助识别性能瓶颈。
*   **指标与仪表盘**：采集基础设施或应用指标，支持多种可视化面板及自定义查询（PromQL/ClickHouse）。
*   **LLM 可观测性**：监控大型语言模型应用的表现、Token 使用量、成本及行为。
*   **告警与异常监控**：支持对日志、指标、链路设置阈值告警及异常检测，自动捕获并展示异常堆栈。

支持多种编程语言及框架，提供云服务及自托管（Docker/Kubernetes）部署方式，旨在通过关联分析日志、指标和追踪数据来快速定位问题。