### [open-telemetry opentelemetry-collector](https://github.com/open-telemetry/opentelemetry-collector)  ![GitHub Repo stars](https://img.shields.io/github/stars/open-telemetry/opentelemetry-collector?style=social)

OpenTelemetry Collector 是一个厂商中立的工具，用于接收、处理和导出遥测数据。它能够统一管理多种遥测格式（如 Jaeger、Prometheus）及传输至多个后端，无需运行多个独立的代理或收集器。

核心特性包括：
- **统一性**：单一代码库，支持跟踪、指标和日志，可部署为代理或收集器。
- **易用性**：提供合理默认配置，支持流行协议，开箱即用。
- **高性能**：在多变负载下保持稳定和高效。
- **可扩展性**：支持定制而不需修改核心代码。
- **可观测性**：作为可观测服务项目的典范。

此外，项目基于稳定的 OTLP 协议 v1.5.0 构建，支持 Go 版本动态更新，并提供镜像签名验证功能。