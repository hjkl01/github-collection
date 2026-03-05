
---
title: opentelemetry-go
---

### [open-telemetry opentelemetry-go](https://github.com/open-telemetry/opentelemetry-go)  ![GitHub Repo stars](https://img.shields.io/github/stars/open-telemetry/opentelemetry-go?style=social)

OpenTelemetry-Go 是 OpenTelemetry 的 Go 语言实现，提供 API 直接测量软件性能与行为并将数据发送至可观测性平台。它支持捕获分布式追踪（Traces）、指标（Metrics）和日志（Logs）遥测数据，其中 Traces 和 Metrics 已稳定，Logs 为 Beta 版。项目允许通过插桩应用收集遥测信息，并配置 OTLP、Prometheus、stdout、Zipkin 等导出器将数据发送至目标平台。