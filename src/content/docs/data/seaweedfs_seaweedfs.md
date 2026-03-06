
---
title: seaweedfs
---

### [seaweedfs seaweedfs](https://github.com/seaweedfs/seaweedfs)  ![GitHub Repo stars](https://img.shields.io/github/stars/seaweedfs/seaweedfs?style=social)

SeaweedFS 是一款简单且高可扩展的开源分布式文件系统，专为存储数十亿文件并提供高速服务而设计。其核心架构采用卷服务器管理元数据，实现 O(1) 磁盘读取效率，单文件元数据开销仅 40 字节。项目支持 S3 兼容 API、WebDAV、Hadoop 集成及 Kubernetes CSI 驱动，并通过 Filer 模块提供目录与 POSIX 属性管理。功能涵盖多副本复制、自动压缩、纠删码（冷数据）、云本地混合存储及弹性扩展。支持单二进制、Docker 等多种部署方式，适用于开发、测试及生产环境，强调高性能、低开销与易用性。