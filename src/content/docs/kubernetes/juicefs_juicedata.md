
---
title: juicefs
---

### [juicedata juicefs](https://github.com/juicedata/juicefs)  ![GitHub Repo stars](https://img.shields.io/github/stars/juicedata/juicefs?style=social)

JuiceFS 是一款专为云原生环境设计的高性能开源 POSIX 文件系统。它通过将数据持久化在对象存储（如 Amazon S3），并将元数据存储于多种数据库引擎（如 Redis、MySQL、TiKV），实现了海量云存储无需修改代码即可像本地存储一样高效使用。

主要特性：
1. 接口兼容：完全兼容 POSIX、Hadoop 及 S3 协议，支持 Kubernetes CSI Driver。
2. 并发与一致：支持数千客户端共享读写，具备强一致性。
3. 性能与安全：具备低延迟高吞吐性能，支持数据加密、压缩及多种存储后端。