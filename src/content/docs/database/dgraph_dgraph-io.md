
---
title: dgraph
---

### [dgraph-io dgraph](https://github.com/dgraph-io/dgraph)

**核心内容总结：**

Dgraph 是一个支持 ACID 事务的分布式 GraphQL 数据库，采用图存储结构，具备水平扩展能力，适用于处理大规模结构化数据。其核心特性包括：  
- **高性能**：通过优化数据存储结构，减少磁盘寻址和网络调用，支持高吞吐量和低延迟查询。  
- **多协议支持**：支持 GraphQL 查询，响应格式包括 JSON 和 Protocol Buffers，通信协议为 gRPC 和 HTTP。  
- **跨平台部署**：官方支持 Linux/amd64 和 Linux/arm64，推荐通过 Docker 部署。  

**使用方法：**  
1. **Docker 安装**：  
   ```bash  
   docker pull dgraph/dgraph:latest  
   ```  
   快速启动单机集群：  
   ```bash  
   docker run -it -p 8080:8080 -p 9080:9080 -v ~/dgraph:/dgraph dgraph/standalone:latest  
   ```  
2. **源码安装**：需 Go 1.24+ 环境，执行以下命令：  
   ```bash  
   git clone https://github.com/dgraph-io/dgraph.git  
   cd dgraph  
   make install  
   ```  

**主要特性对比：**  
- 支持分布式 ACID 事务，优于 Neo4j 和 Janus Graph 的单节点或非 ACID 实现。  
- 提供原生的全文搜索、正则表达式、地理搜索功能，而 Neo4j 部分功能依赖外部系统。  
- 采用分片架构，支持自动数据迁移和负载均衡，Neo4j 企业版仅支持副本，Janus Graph 依赖底层数据库。  

**适用场景：**  
适合需要处理多表关联、稀疏数据、复杂图遍历且要求高并发性能的场景，尤其适合需要 SQL 级事务保障和 NoSQL 扩展性的应用。