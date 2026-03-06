
---
title: seaweedfs
---

### [chrislusf seaweedfs](https://github.com/chrislusf/seaweedfs)  ![GitHub Repo stars](https://img.shields.io/github/stars/chrislusf/seaweedfs?style=social)

SeaweedFS 是一款开源的分布式文件系统，致力于高效存储数十亿文件并提供高速服务。

1. **架构设计**：Master 服务器管理卷映射，Volume 服务器存储数据与元数据（每文件仅需 16 字节元数据），实现 O(1) 磁盘读取，专为小文件和高并发读取优化。
2. **文件系统支持**：通过 Filer 组件提供目录结构和 POSIX 属性，支持 MySQL、Redis、Cassandra、HBase 等多种元数据存储引擎，支持 FUSE 本地挂载。
3. **接口兼容**：原生支持 Amazon S3 API、WebDAV、Hadoop 兼容接口，提供 Kubernetes CSI 驱动及 WebDAV 映射盘支持。
4. **数据可靠性与扩展**：支持机架/数据中心感知副本、纠删码（针对冷数据）、分层存储（本地热数据 + 云端冷数据）；添加节点无需触发数据重平衡，支持弹性扩容。
5. **部署便捷**：支持单二进制文件快速启动（weed mini）、Docker 运行及多平台部署，无单点故障设计。