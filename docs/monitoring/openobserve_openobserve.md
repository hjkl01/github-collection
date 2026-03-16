### [openobserve openobserve](https://github.com/openobserve/openobserve)  ![GitHub Repo stars](https://img.shields.io/github/stars/openobserve/openobserve?style=social)

OpenObserve 是一个基于 Rust 开发的开源可观测性平台，提供日志、指标、链路追踪和前端监控（RUM）的统一解决方案，旨在替代 Datadog、Splunk 和 Elasticsearch。

核心功能与优势：
1.  **架构优势**：采用 Parquet 列式存储和 S3 原生架构，存储成本比 Elasticsearch 低 140 倍，支持 TB 级至 PB 级数据规模，查询性能更高。
2.  **全功能监控**：集成日志管理、分布式追踪、指标采集、仪表盘、告警及数据处理流水线。
3.  **易用部署**：单二进制部署，内置 OpenTelemetry 支持，5 分钟内即可运行，支持高可用和多区域集群。
4.  **查询能力**：日志与追踪使用 SQL 查询，指标支持 SQL 或 PromQL，无专有查询语言。
5.  **企业特性**：支持多租户、SSO 认证、敏感数据脱敏、审计日志及容量规划工具。
6.  **安全合规**：符合 SOC 2、ISO 27001 及 GDPR 标准，提供端到端数据加密。

项目核心采用 AGPL-3.0 开源协议，同时提供商用企业版支持与服务。