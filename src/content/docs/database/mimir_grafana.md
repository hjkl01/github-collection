
---
title: mimir
---

### [grafana mimir](https://github.com/grafana/mimir)  ![GitHub Repo stars](https://img.shields.io/github/stars/grafana/mimir?style=social)

Grafana Mimir 是一个开源项目，为 Prometheus 提供可扩展的长期存储解决方案。核心功能包括：

- **易部署维护**：支持单体模式，单二进制文件即可运行，配套完善文档。
- **大规模扩展**：水平架构可处理数十亿活跃时间序列。
- **全局指标视图**：聚合多个 Prometheus 实例数据，查询引擎并行度高。
- **低成本存储**：兼容多种对象存储（如 AWS S3、Azure 等）实现长期存储。
- **高可用性**：数据复制防止丢失，支持零停机升级与维护。
- **原生多租户**：支持数据隔离及服务质量控制，便于多团队共享集群。