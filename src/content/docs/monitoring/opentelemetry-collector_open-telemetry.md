
---
title: opentelemetry-collector
---

### [open-telemetry opentelemetry-collector](https://github.com/open-telemetry/opentelemetry-collector)  ![GitHub Repo stars](https://img.shields.io/github/stars/open-telemetry/opentelemetry-collector?style=social)

OpenTelemetry Collector 是一个供应商中立的工具，用于接收、处理和导出追踪、指标和日志等遥测数据。它消除了运行多个代理以支持多种遥测格式到不同后端的需求，实现单一代码库的统一部署（作为代理或收集器）。

核心特性包括：
1. **统一性**：同时支持追踪、指标和日志，可部署为代理或收集器。
2. **可扩展性**：支持自定义组件，无需修改核心代码即可定制。
3. **易用与性能**：提供合理默认配置，支持流行协议，在各种负载下稳定高效。
4. **安全与兼容**：基于 OTLP v1.5.0 协议（稳定版），支持容器镜像签名验证及 Go 版本兼容性管理。