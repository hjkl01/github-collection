
---
title: influxdb
---

### [influxdata influxdb](https://github.com/influxdata/influxdb)

**核心内容总结：**

**项目功能**  
InfluxDB Core 是专为收集、处理、转换和存储事件及时间序列数据设计的数据库，适用于需要实时数据摄入和快速查询的场景（如监控、仪表盘、自动化系统）。  

**使用方法**  
- 提供多种安装方式：Docker镜像、Debian/RPM包、tarball等。  
- 支持通过InfluxDB 1.x/2.x的写入API（如HTTP）和查询API（InfluxQL）。  
- 提供官方文档和社区资源（如教程、论坛）辅助使用。  

**主要特性**  
1. **无磁盘架构**：支持对象存储或本地磁盘，无需依赖其他组件。  
2. **高性能查询**：支持毫秒级响应（如last-value查询<10ms）。  
3. **扩展能力**：嵌入式Python虚拟机支持插件和触发器，Parquet文件持久化。  
4. **兼容性**：兼容InfluxDB 1.x/2.x的写入和查询API，支持SQL引擎（FlightSQL/HTTP）。  

**项目状态**  
InfluxDB 3 Core已于2025年4月15日发布GA版本，后续将按月发布点更新，6个月后转为季度更新。