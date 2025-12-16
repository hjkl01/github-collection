
---
title: qdrant
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/qdrant/qdrant?style=social) ](https://github.com/qdrant/qdrant)
### [qdrant qdrant](https://github.com/qdrant/qdrant)

**Qdrant 核心内容总结：**

**项目功能**  
Qdrant 是一个基于向量相似性搜索的数据库，支持存储、搜索和管理带元数据的向量数据。适用于神经网络、语义匹配、多条件过滤等场景，提供高性能的向量检索服务，并支持云托管版本（Qdrant Cloud）。

**使用方法**  
1. **Python 快速启动**：通过 `pip install qdrant-client` 安装客户端，使用内存或本地磁盘模式初始化实例。  
2. **本地运行**：通过 Docker 命令 `docker run -p 6333:6333 qdrant/qdrant` 启动服务，客户端连接 `http://localhost:6333`。  
3. **多语言支持**：提供 Go、Rust、JavaScript、Python、.NET、Java 等官方客户端，社区支持 Elixir、PHP、Ruby 等。

**主要特性**  
- **过滤与元数据**：支持 JSON 元数据存储，可基于关键字、全文、数值范围、地理信息等条件过滤。  
- **混合搜索**：结合密集向量（dense）与稀疏向量（sparse），提升关键词匹配能力。  
- **资源优化**：内置向量量化技术，减少内存占用（最高降低 97%），支持磁盘存储。  
- **分布式部署**：通过分片扩展规模，通过复制提升吞吐，支持无中断滚动更新。  
- **性能优化**：SIMD 硬件加速、异步 I/O（io_uring）、写前日志（WAL）保障数据持久化。  

**其他**  
- 提供 OpenAPI 3.0 文档和 gRPC 接口，支持多语言客户端生成。  
- 集成方案涵盖 Cohere、LangChain、Haystack 等主流 AI 框架。  
- 开源协议为 Apache 2.0，提供免费云服务试用。