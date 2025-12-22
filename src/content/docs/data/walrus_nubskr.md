
---
title: walrus
---

### [nubskr walrus](https://github.com/nubskr/walrus)  ![GitHub Repo stars](https://img.shields.io/github/stars/nubskr/walrus?style=social)

**项目核心内容总结：**

**项目功能**  
Walrus 是一个基于高性能日志存储的分布式消息流处理引擎，支持容错、自动负载均衡和分段分区，采用 Raft 共识算法协调元数据，适用于需要高可用性和可扩展性的流数据处理场景。

**主要特性**  
1. **容错与高可用**：通过 Raft 共识算法（需 3+ 节点）保障数据一致性，支持自动领导轮换和故障恢复。  
2. **负载均衡**：分段分区机制结合自动领导轮换，实现集群负载均衡。  
3. **高性能存储**：基于 Linux 的 io_uring 技术优化 I/O 操作，显著提升吞吐量。  
4. **灵活读写**：支持密封分段历史数据读取，提供简单 TCP 客户端协议（文本命令）和交互式 CLI 工具。  
5. **多场景适配**：支持嵌入式使用（Rust 库形式）及独立部署，兼容多种存储后端（如 mmap、FD）。  

**使用方法**  
- **集群部署**：通过 `make cluster-bootstrap` 启动多节点集群，使用 CLI 命令（如 `REGISTER`、`PUT`、`GET`）进行交互。  
- **库集成**：以 Rust 库形式集成到项目，通过 `walrus-rust` API 实现数据写入与读取。  
- **测试验证**：提供完整测试套件，覆盖分布式场景、批量操作及性能基准测试。  

**性能表现**  
- **无 Fsync 情况下**：吞吐量达 11,389 writes/s（对比 Kafka 11,224 writes/s）。  
- **带 Fsync 情况下**：吞吐量保持 4,980 writes/s，优于 RocksDB（5,222 writes/s）。