
---
title: apisix
---

### [apache apisix](https://github.com/apache/apisix)

**Apache APISIX 核心内容总结**

**项目功能**  
Apache APISIX 是一个高性能的 API 网关，支持反向代理、负载均衡、动态路由、插件扩展等功能，适用于微服务架构和云原生场景。

**使用方法**  
1. 安装：通过官方文档提供的安装指南部署（支持多种环境）。  
2. 快速入门：按照文档步骤配置基础路由和插件。  
3. 管理：通过 REST Admin API 动态调整配置，或使用 Dashboard 界面操作。  
4. 插件开发：支持 Lua、Java、Go、Python 等语言编写自定义插件，或使用 Wasm SDK 实现扩展。

**主要特性**  
- **高性能**：单核 QPS 达 18,000，延迟低于 0.2 毫秒，支持高并发场景。  
- **多语言支持**：插件开发兼容 Lua、Java、Go、Python 等语言，支持 Wasm 扩展。  
- **插件生态**：内置 100+ 插件（如限流、认证、日志记录），支持自定义负载均衡算法和路由规则。  
- **集群与高可用**：通过 etcd 实现配置中心集群，支持多节点高可用部署。  
- **日志与监控**：支持将日志输出到 Kafka、Elasticsearch、ClickHouse 等系统，集成 Prometheus、Datadog 等监控工具。  
- **Serverless 集成**：支持 AWS Lambda、Azure Functions、Apache OpenWhisk 等云函数作为动态上游。  
- **安全与权限**：集成 HashiCorp Vault 管理密钥，支持 JWT 认证、IP 过滤等安全策略。