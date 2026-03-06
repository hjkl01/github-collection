
---
title: influxdb
---

### [influxdata influxdb](https://github.com/influxdata/influxdb)  ![GitHub Repo stars](https://img.shields.io/github/stars/influxdata/influxdb?style=social)

InfluxDB Core 是一款用于收集、处理、转换和存储事件及时序数据的数据库，针对实时数据摄入和快速查询响应进行了优化，适用于监控、自动化及各类分析场景。

核心功能特性包括：
- **存储架构**：支持无盘模式（对象存储）或本地磁盘，采用 Parquet 文件持久化。
- **查询性能**：查询响应极快，最后值查询通常低于 10 毫秒。
- **扩展能力**：内嵌 Python VM，支持插件和触发器。
- **API 兼容**：兼容 InfluxDB 1.x/2.x 写入 API 及 1.x 查询 API（InfluxQL）。
- **SQL 引擎**：支持 SQL 查询，包含 FlightSQL 和 HTTP 查询 API。