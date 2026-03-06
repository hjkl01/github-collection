
---
title: corrosion
---

### [superfly corrosion](https://github.com/superfly/corrosion)  ![GitHub Repo stars](https://img.shields.io/github/stars/superfly/corrosion?style=social)

Corrosion 是一款基于 Gossip 协议的大型分布式系统服务发现与状态管理工具。它通过在各节点维护本地 SQLite 数据库替代中央状态库，实现低延迟的读写与最终一致性。核心功能包括：使用 CRDTs 进行冲突解决、提供 SQL 读写 API 与 HTTP 流式订阅、基于 QUIC 协议的安全 P2P 通信、以及支持 SWIM 协议的集群成员管理。该工具支持动态 Schema 更新与配置同步，旨在解决跨地域网络延迟问题，提供灵活可靠的分布式状态同步方案。