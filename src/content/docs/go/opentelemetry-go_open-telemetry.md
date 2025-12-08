
---
title: opentelemetry-go
---

### [open-telemetry opentelemetry-go](https://github.com/open-telemetry/opentelemetry-go)

**核心内容总结：**  
OpenTelemetry-Go 是 Go 语言实现的 OpenTelemetry 项目，提供 API 用于收集软件性能和行为数据，并发送至可观测性平台。主要功能包括：  
1. **功能**：支持分布式追踪（稳定）、指标（稳定）和日志（Beta）的采集与导出。  
2. **使用方法**：  
   - **仪器化**：通过官方支持的库或直接使用 `go.opentelemetry.io/otel` 包进行应用监控。  
   - **导出配置**：使用 OTLP、Prometheus、stdout、Zipkin 等导出器将数据发送至目标平台。  
3. **特性**：  
   - 兼容当前主流 Go 版本（如 1.24、1.25），支持多平台（Ubuntu、macOS、Windows）及多种架构（amd64、386、arm64）。  
   - 提供详细的 [版本稳定性说明](VERSIONING.md) 和 [贡献指南](CONTRIBUTING.md)。  
4. **支持导出器**：OTLP（全信号）、Prometheus（指标）、stdout（全信号）、Zipkin（追踪）。