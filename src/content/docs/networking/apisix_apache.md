
---
title: apisix
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/apache/apisix?style=social) ](https://github.com/apache/apisix)
### [apache apisix](https://github.com/apache/apisix)

**核心内容总结：**  
Apache APISIX 是一个高性能、可扩展的开源 API 网关，支持动态路由、负载均衡、插件扩展等功能，适用于微服务架构和云原生场景。  

**主要功能与特性：**  
1. **高性能**：单核 QPS 达 18,000，延迟低于 0.2 毫秒，支持高并发场景。  
2. **插件系统**：提供丰富的内置插件（如限流、认证、日志记录等），支持自定义插件开发（Lua/Java/Go/Python/Proxy Wasm）。  
3. **多协议支持**：兼容 HTTP、HTTPS、gRPC 等协议，可作为反向代理或服务网格组件。  
4. **动态配置**：通过 REST Admin API 实现配置热更新，无需重启服务。  
5. **高可用与集群**：支持 etcd 集群配置，实现节点状态同步和故障转移。  
6. **日志与监控**：集成多种日志输出（HTTP、Kafka、Elasticsearch 等）和监控工具（Prometheus、Datadog）。  
7. **多语言支持**：插件开发支持 Java/Go/Python/Node.js，且可通过 WebAssembly 实现跨语言扩展。  
8. **Serverless 集成**：支持 AWS Lambda、Azure Functions、Apache OpenWhisk 等无服务器架构。  

**使用方法：**  
- 安装：通过官方文档提供的安装指南部署（支持多种操作系统和云环境）。  
- 配置：使用 YAML 文件定义路由规则，或通过 REST API 动态调整配置。  
- 扩展：开发自定义插件，或集成第三方服务（如 Vault 密钥管理）。  
- 监控：结合日志和监控工具分析流量、性能及安全事件。  

**适用场景：**  
企业级 API 管理、微服务网关、云原生服务编排、边缘计算及 Serverless 架构。