
---
title: pgvectorscale
---

### [timescale pgvectorscale](https://github.com/timescale/pgvectorscale)

**核心内容总结：**  
**项目功能**：pgvectorscale 是 PostgreSQL 的扩展，支持向量数据的高效索引与搜索，基于 StreamingDiskANN 算法，适用于 AI、分析等场景。  

**使用方法**：  
1. **安装**：需通过 Rust 编译安装，或使用 Timescale Cloud 服务。  
2. **创建索引**：通过 `CREATE INDEX` 命令定义向量字段索引，支持标签过滤（如 `labels` 字段）。  
3. **查询**：使用 `ORDER BY vector distance` 语法进行向量相似度搜索，支持参数调优（如 `query_rescore` 控制精度）。  

**主要特性**：  
- **高效索引**：StreamingDiskANN 算法支持内存优化存储（SBQ 压缩）、并行构建（自动适配大数据集）。  
- **灵活过滤**：支持标签字段过滤（如 `WHERE labels && array[...]`），可结合语义标签（如通过名称转换 ID）。  
- **参数调优**：提供索引构建参数（如 `num_neighbors`）和查询参数（如 `query_search_list_size`），平衡精度与性能。  
- **兼容性**：支持与 PostgreSQL 的 `WHERE` 子句结合使用，但不支持 `UNLOGGED` 表的索引。  

**注意事项**：  
- 空向量、空标签数组不参与索引；查询结果排序为宽松顺序（需通过 `MATERIALIZED CTE` 保证严格排序）。