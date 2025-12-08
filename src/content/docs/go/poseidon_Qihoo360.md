
---
title: poseidon
---

### [Qihoo360 poseidon](https://github.com/Qihoo360/poseidon)

**核心内容总结：**  
Poseidon 是 360 公司开发的日志搜索平台，用于在 PB 级海量数据中快速检索特定信息（如 APT 事件相关日志），解决传统 Hadoop Map/Reduce 任务耗时长的问题。其核心功能包括：  
1. **高效检索**：通过倒排索引技术，实现秒级响应，从万亿至千万亿条数据中快速定位目标；  
2. **资源优化**：无需额外存储，数据直接基于 Hadoop 集群管理，节省存储与计算资源；  
3. **灵活支持**：兼容结构化与非结构化数据，适用于多种大规模数据查询场景。  

**使用方法**：通过 `docs/get_started.md` 文档中的 Quick Start 指南快速部署与使用。  

**主要技术**：基于 Hadoop 存储与索引构建、Java 与 Golang 开发、Redis/Memcached 存储元数据，并通过微服务架构（如 searcher、proxy 等）提供 HTTP 接口服务。