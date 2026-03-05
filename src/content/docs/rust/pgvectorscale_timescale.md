
---
title: pgvectorscale
---

### [timescale pgvectorscale](https://github.com/timescale/pgvectorscale)  ![GitHub Repo stars](https://img.shields.io/github/stars/timescale/pgvectorscale?style=social)

pgvectorscale 是基于 pgvector 的 PostgreSQL 扩展，专为 AI 应用提供高性能嵌入搜索和高效存储。

核心功能：
1. 引入基于微软 DiskANN 算法的 StreamingDiskANN 索引。
2. 采用统计二元量化（SBQ）压缩方法降低成本。
3. 支持结合向量相似度与标签的过滤搜索。

项目特性：
- 采用 Rust 语言开发。
- 性能显著优于 Pinecone 等竞品（延迟降低 28 倍，吞吐量提高 16 倍，成本降低 75%）。
- 支持 Docker、源码或 Timescale Cloud 安装。
- 支持参数调优、任意 WHERE 过滤及严格排序处理。