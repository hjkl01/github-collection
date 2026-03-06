
---
title: VectorChord
---

### [tensorchord VectorChord](https://github.com/tensorchord/VectorChord)  ![GitHub Repo stars](https://img.shields.io/github/stars/tensorchord/VectorChord?style=social)

VectorChord 是一款基于 PostgreSQL 的高性能、低成本向量搜索扩展。它采用 RaBitQ 压缩与自主重排序技术，支持在单台服务器上高效托管 1 亿至 10 亿 + 向量，显著降低存储成本。项目具备极速索引构建能力（1 亿向量约 20 分钟）、支持海量数据平滑扩展，且完全兼容 pgvector 数据类型与语法，无需复杂调优。此外，它提供 4 位和 8 位原生量化向量类型以优化空间，并支持 Docker 快速部署。