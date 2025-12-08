
---
title: corrosion
---

### [superfly corrosion](https://github.com/superfly/corrosion)

**项目核心内容总结：**

Corrosion 是一个基于 gossip 协议的分布式服务发现工具，适用于大规模分布式系统。其核心功能包括：通过 SQLite 数据库实现节点本地状态存储，利用 CRDTs（冲突可解的无向数据类型）和 CR-SQLite 解决数据冲突，通过 SWIM 协议（由 Foca 实现）管理集群成员，结合 QUIC 协议实现安全的节点间通信。

**主要特性：**
1. 支持 SQL 语句灵活读写数据；
2. 文件化 schema 设计，支持运行时更新；
3. 基于 SQL 查询的 HTTP 流式订阅；
4. 通过 Rhai 模板引擎动态生成配置文件；
5. 可替代 Consul 的服务状态存储方案；
6. 使用 QUIC 协议实现低延迟通信。

**使用方法：**
在集群所有节点运行 Corrosion 代理程序，通过 HTTP API 实现数据查询、更新及订阅。管理工具提供 CLI 操作界面。部署需配置文件、定义数据库 schema 并启动代理服务。