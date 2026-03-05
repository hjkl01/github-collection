
---
title: tarantool
---

### [tarantool tarantool](https://github.com/tarantool/tarantool)  ![GitHub Repo stars](https://img.shields.io/github/stars/tarantool/tarantool?style=social)

Tarantool 是一个基于内存的计算平台，集成了数据库和应用服务器。

应用服务器基于 LuaJIT 2.1 提供优化的 Lua 解释器和 JIT 编译器，支持协作式多任务、非阻塞 IO、持久队列、分片、集群管理及外部数据库（MySQL/PostgreSQL）访问。

数据库采用 MessagePack 格式，提供内存存储（含 WAL 持久化）及 LSM 树引擎，支持多种索引类型（HASH/TREE/RTREE/BITSET）、JSON 路径索引、异步/同步复制、RAFT 自动选举、认证访问控制及 ANSI SQL（含视图、关联和约束）。

支持 Linux、Mac OS X 和 FreeBSD 平台，适用于队列服务器、缓存和有状态 Web 应用等可扩展 Web 架构组件。