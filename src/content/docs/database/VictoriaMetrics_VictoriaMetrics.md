
---
title: VictoriaMetrics
---

### [VictoriaMetrics VictoriaMetrics](https://github.com/VictoriaMetrics/VictoriaMetrics)  ![GitHub Repo stars](https://img.shields.io/github/stars/VictoriaMetrics/VictoriaMetrics?style=social)

VictoriaMetrics 是一款快速、高效且可扩展的时间序列数据库，用于监控和管理时序数据。

- **存储与兼容**：支持 Prometheus 长期存储，可作为 Grafana 中 Prometheus 和 Graphite 的直接替代品。
- **查询能力**：支持 PromQL 及性能更优的 MetricsQL 查询语言。
- **数据摄入**：支持 Prometheus、InfluxDB、Graphite、OpenTSDB、OpenTelemetry 等多种协议及 JSON、CSV 等格式。
- **部署模式**：提供单节点和集群版本（均开源），单二进制文件无外部依赖，支持 NFS 存储及即时快照备份。
- **性能优势**：内存占用低，数据压缩率高，适合 APM、Kubernetes、IoT 等大规模数据场景。
- **企业版增强**：包含异常检测、自动备份、多保留策略、降采样及长期支持（LTS）等功能。