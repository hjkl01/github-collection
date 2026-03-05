
---
title: tikv
---

### [tikv tikv](https://github.com/tikv/tikv)  ![GitHub Repo stars](https://img.shields.io/github/stars/tikv/tikv?style=social)

TiKV 是一个开源的、分布式的、支持 ACID 事务的键值数据库。它使用 Rust 编写，基于 Raft 共识算法保证数据一致性，底层存储依赖 RocksDB。TiKV 支持水平扩展、自动分片、地理复制及外部一致的分布式事务，并提供 Coprocessor 框架支持分布式计算。作为 CNCF 毕业项目，它常与 TiDB 协同工作，并提供 Go、Java、Rust、C 等多种客户端驱动。