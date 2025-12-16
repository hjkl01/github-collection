
---
title: tarantool
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/tarantool/tarantool?style=social) ](https://github.com/tarantool/tarantool)
### [tarantool tarantool](https://github.com/tarantool/tarantool)

**项目功能**  
Tarantool 是一个内存计算平台，集成了数据库和应用服务器。应用服务器提供高性能 LuaJIT 解释器、协作多任务、非阻塞 IO、持久队列、分片、集群管理框架等功能，支持连接 MySQL 和 PostgreSQL 等外部数据库。数据库支持 MessagePack 数据格式、多种索引类型（HASH、TREE 等）、异步/同步复制、RAFT 自动选举、ANSI SQL 等特性，并兼容多种编程语言的连接器。

**使用方法**  
可通过下载二进制包或 Docker 安装，也可从源码构建。模块、工具和连接器可通过官方资源获取。

**主要特性**  
1. 高性能：基于 LuaJIT 的 JIT 编译器，支持内存计算与持久化。  
2. 灵活架构：支持单主集群、分片、队列、多语言连接器。  
3. 数据库特性：MessagePack 协议、LSM 树引擎、JSON 索引、同步/异步复制。  
4. 跨平台：支持 Linux、Mac OS X（含 M1）、FreeBSD。  
5. 开发友好：提供 ANSI SQL、集群管理框架 Cartridge、丰富的模块生态。