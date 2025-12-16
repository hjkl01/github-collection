
---
title: cockroach
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/cockroachdb/cockroach?style=social) ](https://github.com/cockroachdb/cockroach)
### [cockroachdb cockroach](https://github.com/cockroachdb/cockroach)

**CockroachDB核心内容总结**  

**项目功能**  
CockroachDB是一个云原生分布式SQL数据库，支持水平扩展、强一致性ACID事务及自动故障恢复（支持磁盘、机器、机架甚至数据中心级容灾），提供与PostgreSQL兼容的SQL接口，适用于构建高可用、数据密集型应用。  

**主要特性**  
- 分布式架构：支持跨节点水平扩展，自动数据复制与负载均衡。  
- 强一致性：保证ACID事务，支持跨节点事务处理。  
- 高可用性：自动故障转移与恢复，无需人工干预。  
- 兼容性：遵循PostgreSQL协议，支持主流编程语言的客户端驱动及ORM框架。  

**使用方法**  
1. **部署方式**  
   - 通过[CockroachCloud](https://www.cockroachlabs.com/docs/cockroachcloud/quickstart)快速创建托管集群。  
   - 本地部署：安装后启动本地集群，使用内置SQL客户端连接。  
   - 手动部署：支持多机器集群部署及云平台（如AWS、GCP）部署。  
2. **开发接入**  
   - 使用PostgreSQL兼容的客户端驱动（如Go、Python、Java等）连接数据库。  
   - 参考官方教程构建应用（如[Hello World示例](https://www.cockroachlabs.com/docs/stable/hello-world-example-apps.html)）。  
3. **学习资源**  
   - 官方文档提供安装、部署、SQL语法及故障排查指南。  
   - 通过[设计文档](https://www.cockroachlabs.com/docs/stable/architecture/overview.html)了解底层架构。  

**其他**  
- 社区支持：可通过Slack、论坛及GitHub提交问题或贡献代码。  
- 开源许可：2024年11月18日后版本采用CockroachDB Software License（CSL）。