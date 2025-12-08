
---
title: VictoriaMetrics
---

### [VictoriaMetrics VictoriaMetrics](https://github.com/VictoriaMetrics/VictoriaMetrics)

VictoriaMetrics 是一个高性能的时间序列数据库，用于监控和管理时间序列数据，支持作为 Prometheus 的替代方案。其核心功能包括：  
1. **数据摄入**：兼容多种协议（如 Prometheus remote write、InfluxDB line protocol、Graphite 等），支持从监控工具采集数据。  
2. **部署方式**：提供单节点部署、集群模式及企业版（需付费），企业版包含异常检测、备份自动化、多数据保留策略、数据降采样等功能。  
3. **性能优势**：内存占用低（比 InfluxDB、Prometheus 等少 10 倍以上），数据压缩率高（存储效率比 Prometheus 提升 7 倍），支持高吞吐和大规模数据查询。  
4. **使用方式**：可通过二进制文件、Docker 镜像部署，支持与现有监控系统集成。  
5. **社区与支持**：提供 Slack、Reddit、Telegram 等社区交流渠道，企业用户可获取官方技术支持和长期稳定版本（LTS）。