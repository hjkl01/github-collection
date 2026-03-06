
---
title: Bifrost
---

### [brokercap Bifrost](https://github.com/brokercap/Bifrost)  ![GitHub Repo stars](https://img.shields.io/github/stars/brokercap/Bifrost?style=social)

Bifrost 是一款面向生产环境的异构数据同步中间件，支持将 MySQL、MariaDB、Kafka、Mongo 等源端数据，全量及实时同步到 Redis、ClickHouse、Elasticsearch、Kafka、MySQL 等多种目标端。核心功能包括：支持全量及增量数据同步及部分目标的 DDL 同步；提供 Web 界面动态配置数据表及目标库；采用 Binlog 解析多线程并行同步架构，支持宕机自动恢复及位点精确控制；具备监控报警（Email/微信）、HTTP API 接口，并支持第三方插件开发与 HTTPS 通信。