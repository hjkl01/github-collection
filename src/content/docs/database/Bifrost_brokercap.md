
---
title: Bifrost
---

### [brokercap Bifrost](https://github.com/brokercap/Bifrost)

**Bifrost** 是一款用于将 MySQL/MariaDB 数据实时同步到 Redis、ClickHouse、Elasticsearch、Kafka 等异构系统的中间件，支持全量与增量同步。  

**核心功能**：  
- **源端支持**：MySQL、MariaDB、Percona、Kafka、Mongo 等，支持 Binlog、Kafka 消息、JSON 自定义格式等。  
- **目标端支持**：Redis、MySQL、ClickHouse、Kafka、RabbitMQ、StarRocks、Doris 等，部分支持 DDL 同步。  
- **特性**：  
  - 界面化动态配置数据表与目标库；  
  - 多源多目标并行同步，支持故障恢复与位点控制；  
  - 提供 HTTP API、Email/微信报警、插件开发接口；  
  - 支持 HTTPS、TLS 加密及自定义证书。  

**使用方法**：  
1. **安装**：通过源码编译、二进制包或 Docker 部署。  
2. **配置**：修改 `Bifrost.ini` 设置用户名、监听端口、日志路径、TLS 证书等参数。  
3. **启动**：执行 `./Bifrost-server start`，通过 Web 界面（默认地址：`https://127.0.0.1:21036`）管理同步任务。  

**适用场景**：数据实时同步、跨数据库迁移、消息队列集成等生产环境需求。