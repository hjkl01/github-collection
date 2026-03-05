
---
title: seaweedfs
---

### [seaweedfs seaweedfs](https://github.com/seaweedfs/seaweedfs)  ![GitHub Repo stars](https://img.shields.io/github/stars/seaweedfs/seaweedfs?style=social)

SeaweedFS 是一款简单、高可扩展的分布式文件系统，专为存储数十亿文件并提供高速服务设计。其架构将元数据分散至 Volume Server，支持 O(1) 磁盘读取，大幅降低小文件存储开销。核心功能涵盖对象存储、目录管理（Filer，支持多种元数据后端）、S3/WebDAV/Hadoop 兼容接口及 Kubernetes 集成。系统支持多副本、纠删码、冷热数据云分层、自动压缩、加密及 TTL 过期。相比其他系统，SeaweedFS 针对小文件性能优化显著，架构扁平，支持单二进制文件快速部署，易于弹性扩展。