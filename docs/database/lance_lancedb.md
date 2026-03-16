### [lancedb lance](https://github.com/lancedb/lance)  ![GitHub Repo stars](https://img.shields.io/github/stars/lancedb/lance?style=social)

Lance 是一个面向多模态 AI 的开源湖仓格式，提供高性能向量搜索、全文搜索、随机访问及特征工程能力。

主要特性：
1. **混合搜索**：融合向量相似度、全文检索（BM25）和 SQL 分析。
2. **极速随机访问**：比 Parquet 或 Iceberg 快 100 倍，保持扫描性能。
3. **多模态支持**：统一存储图像、视频、音频、文本及嵌入向量。
4. **数据演进**：无需全表重写即可高效添加列，适合特征工程。
5. **版本控制**：支持 ACID 事务、时间旅行、标签和分支。
6. **生态集成**：兼容 Pandas、DuckDB、Spark、PyArrow、Ray 等工具。

适用场景包括构建搜索引擎、特征存储及大规模 ML 训练工作流。