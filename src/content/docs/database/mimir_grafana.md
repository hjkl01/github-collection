
---
title: mimir
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/grafana/mimir?style=social) ](https://github.com/grafana/mimir)
### [grafana mimir](https://github.com/grafana/mimir)

### 核心内容总结：

**项目功能**  
Grafana Mimir 是一个开源的长期存储解决方案，专为 Prometheus 设计，支持水平扩展、多租户、高可用性，适用于大规模监控场景。

**使用方法**  
- 提供部署指南、迁移文档（从 Thanos/Cortex/Prometheus 迁移）、入门教程。  
- 包含架构概述、配置说明及生产环境部署指导。  
- 支持多种对象存储（如 AWS S3、Google Cloud Storage 等）作为长期数据存储。  

**主要特性**  
- **易用性**：单二进制文件即可快速部署，附带最佳实践仪表板和警报。  
- **高扩展性**：支持跨多节点水平扩展，处理高达 10 亿级时间序列。  
- **全局视图**：聚合多 Prometheus 实例数据，支持高效并行查询。  
- **低成本存储**：利用对象存储技术，兼容多种云平台。  
- **高可用性**：数据自动复制，支持零停机升级/降级。  
- **多租户**：隔离数据与查询，支持租户间资源公平分配。