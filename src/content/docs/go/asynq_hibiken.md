
---
title: asynq
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/hibiken/asynq?style=social) ](https://github.com/hibiken/asynq)
### [hibiken asynq](https://github.com/hibiken/asynq)

**Asynq 核心内容总结**  

**项目功能**  
Asynq 是一个基于 Redis 的 Go 语言分布式任务队列库，用于异步处理任务。支持任务调度、重试、优先级队列、去重、超时控制、任务聚合等功能，提供 Web UI 和 CLI 工具管理队列和任务。  

**主要特性**  
- 保证任务至少执行一次，支持失败重试和自动恢复；  
- 支持加权/严格优先级队列、任务去重、超时/截止时间控制；  
- 提供任务聚合功能，批量处理连续操作；  
- 支持 Redis Sentinel 高可用、Prometheus 监控集成；  
- 提供 Web UI 查看队列状态、任务详情及指标，CLI 工具远程控制队列；  
- 支持周期性任务、队列暂停等管理功能。  

**使用方法**  
1. **初始化项目**：使用 `go mod` 管理依赖，安装 Asynq 库；  
2. **定义任务**：编写任务处理函数，通过 `HandleFunc` 或 `Handle` 注册到 `ServeMux`；  
3. **生产任务**：使用 `Client` 的 `Enqueue` 方法提交任务，可配置重试次数、队列名称、延迟执行等参数；  
4. **启动 worker**：通过 `Server` 配置 Redis 连接、并发数及队列优先级，运行 worker 处理任务。  

**其他**  
- 需自行部署 Redis 作为后端存储；  
- Redis 集群兼容性需注意数据分片问题。