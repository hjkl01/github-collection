
---
title: seaweedfs
---

### [chrislusf seaweedfs](https://github.com/chrislusf/seaweedfs)  ![GitHub Repo stars](https://img.shields.io/github/stars/chrislusf/seaweedfs?style=social)

SeaweedFS 是一个开源的轻量级、高度可扩展的分布式文件系统和对象存储，旨在存储数十亿文件并提供高速服务。

主要功能：
1. **高效对象存储**：Master 管理卷元数据，Volume Server 管理文件内容，实现 O(1) 磁盘读取，特别优化海量小文件存储。
2. **高可用架构**：支持机架和数据中心感知的自动复制，主节点故障自动转移，无单点故障。
3. **混合存储**：支持本地热数据与云端冷数据（如 S3、GCS）透明集成，结合纠删码降低存储成本。
4. **文件系统支持**：可选 Filer 组件提供目录、POSIX 属性，支持 S3 兼容 API、WebDAV、Hadoop 兼容及 FUSE 挂载。
5. **弹性扩展**：无需数据重平衡即可动态扩容，支持 Kubernetes CSI 驱动。
6. **丰富特性**：支持自动压缩、TTL 过期、图片缩放、数据加密及超大文件分块处理。