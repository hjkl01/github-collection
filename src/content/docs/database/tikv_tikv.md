
---
title: tikv
---

### [tikv tikv](https://github.com/tikv/tikv)  ![GitHub Repo stars](https://img.shields.io/github/stars/tikv/tikv?style=social)

TiKV 是一个开源的、分布式的、支持事务的键值数据库，使用 Rust 编写并基于 Raft 共识算法。它以 RocksDB 为存储引擎，提供符合 ACID 规范的事务支持，具有地理复制、高横向扩展性（支持百 TB 级数据）及一致的分布式事务能力。TiKV 作为 CNCF 毕业项目，常与 TiDB 配合使用，通过放置驱动（PD）、存储（Store）、区域（Region）和节点（Node）组件实现自动分片、数据复制和负载均衡。