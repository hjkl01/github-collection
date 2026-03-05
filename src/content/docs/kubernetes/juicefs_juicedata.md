
---
title: juicefs
---

### [juicedata juicefs](https://github.com/juicedata/juicefs)  ![GitHub Repo stars](https://img.shields.io/github/stars/juicedata/juicefs?style=social)

JuiceFS 是一款专为云原生环境设计的高性能 POSIX 文件系统，遵循 Apache License 2.0 开源协议。其架构采用数据与元数据分离设计，将数据持久化在对象存储（如 Amazon S3）中，将元数据持久化在兼容的数据库引擎（如 Redis、MySQL、TiKV）中。主要功能特性包括完全兼容 POSIX 和 Hadoop 标准，支持 Kubernetes CSI 驱动、Docker 及 Hadoop 生态无缝集成，支持数千客户端共享读写并具备强一致性。JuiceFS 提供低延迟、高吞吐的性能，支持数据加密、压缩及全局文件锁，兼容多种对象存储服务，允许应用无需修改代码即可将大规模云存储像本地存储一样高效用于大数据、机器学习及各类生产环境。