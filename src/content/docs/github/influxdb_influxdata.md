
---
title: influxdb
---

### [influxdata influxdb](https://github.com/influxdata/influxdb)  ![GitHub Repo stars](https://img.shields.io/github/stars/influxdata/influxdb?style=social)

InfluxDB Core 是一款专为收集、处理、转换和存储事件及时间序列数据设计的数据库，适用于需要实时数据摄入和快速查询响应的场景（如监控、自动化及交互式仪表盘）。其核心功能包括：
- 无盘架构，支持对象存储或本地磁盘；
- 快速查询响应（最后值查询低于 10 毫秒）；
- 内嵌 Python VM 支持插件和触发器；
- 支持 Parquet 文件持久化；
- 兼容 InfluxDB 1.x/2.x 写入 API、1.x 查询 API 及 SQL 查询引擎（支持 FlightSQL 和 HTTP）。