
---
title: corrosion
---

### [superfly corrosion](https://github.com/superfly/corrosion)  ![GitHub Repo stars](https://img.shields.io/github/stars/superfly/corrosion?style=social)

Corrosion 是一款面向大型分布式系统的基于 gossip 的服务发现工具，旨在用最终一致的分布式状态替代 Consul 的中心化状态数据库。

核心功能：
- **节点架构**：各节点维护本地 SQLite 数据库，通过 gossip 传播变更，利用 CRDTs（CR-SQLite）解决冲突。
- **读写性能**：支持本地毫秒级读写，避免跨地域网络延迟。
- **数据交互**：提供 SQL API 读写、HTTP 流式订阅、动态配置生成及服务状态存储。
- **通信安全**：采用 QUIC 协议进行安全点对点通信，利用 SWIM 协议管理集群成员。
- **服务发现**：存储并传播本地注册的 Consul 服务状态，实现去中心化服务发现。