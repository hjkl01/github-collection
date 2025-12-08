
---
title: loggie
---

### [loggie-io loggie](https://github.com/loggie-io/loggie)

**项目核心内容总结：**  
Loggie 是一个基于 Golang 的轻量级、高性能、云原生日志处理工具，支持多种数据源和输出目标（如 Kafka、Elasticsearch、Loki 等），具备多管道处理、可插拔组件（如转换器、过滤器）等能力。其核心特性包括：  
1. **Kubernetes 集成**：通过 CRD（自定义资源定义）实现日志配置的 Kubernetes 原生管理，支持 Agent 模式、Cluster 模式部署。  
2. **灵活处理能力**：支持日志采集（File、Kafka、Prometheus）、转换（Schema、Transformer）、告警（LogAlert）等功能，可扩展拦截器（如限速、字节限制）。  
3. **高可靠性**：具备自适应流量控制、异常恢复、监控指标（如吞吐量、延迟）等功能，适配生产环境。  
4. **多部署方式**：支持 Kubernetes 集群安装、单节点部署，提供快速入门指南和详细文档（含架构、使用、参考配置）。  
5. **对比优势**：相比 Filebeat 等工具，Loggie 在云原生集成、动态配置、多协议支持（如 gRPC）等方面表现更优。  

**使用方法**：  
- 通过 Kubernetes CRD 定义日志处理流程（如 LogConfig、Sink、Interceptor）。  
- 支持命令行参数配置或 YAML 文件定义管道。  
- 提供快速安装教程（Kubernetes/Node）、监控集成（Prometheus）及告警 Webhook 接口。  

**主要特性**：  
- 支持多种数据源（文件、Kafka、Elasticsearch、Kubernetes 事件）与输出目标（Elasticsearch、Loki、Zinc、Webhook）。  
- 提供日志转换、模式匹配、流量限速、字节限制等拦截器功能。  
- 文档完整，包含安装、使用、参考配置、路线图及 Apache 2.0 开源协议。