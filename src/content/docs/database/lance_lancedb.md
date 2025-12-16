
---
title: lance
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/lancedb/lance?style=social) ](https://github.com/lancedb/lance)
### [lancedb lance](https://github.com/lancedb/lance)

**Lance核心内容总结：**

**项目功能**  
Lance是专为多模态AI设计的开源湖仓格式，提供向量搜索、全文搜索（BM25）、随机访问和特征工程能力，支持在对象存储上构建完整的湖仓架构。兼容Pandas、DuckDB、Polars、Spark等工具，适用于构建搜索引擎、特征库、大规模机器学习训练及多模态数据管理。

**使用方法**  
1. 安装：`pip install pylance`（预览版需额外参数）  
2. 数据转换：通过PyArrow将Parquet数据转为Lance格式  
3. 读取数据：使用`lance.dataset()`加载数据并转换为Pandas或DuckDB可处理格式  
4. 向量搜索：支持构建IVF-PQ索引，通过`nearest`方法实现高效近似最近邻搜索  

**主要特性**  
- **混合搜索**：向量相似度、全文检索与SQL分析可联合操作  
- **高效随机访问**：比Parquet快100倍，不牺牲扫描性能  
- **多模态支持**：统一存储图像、视频、音频、文本及嵌入向量  
- **数据演化**：新增列无需全表重写，支持机器学习特征工程  
- **版本控制**：零拷贝ACID事务与时间旅行功能  
- **生态集成**：兼容Arrow、Spark、Ray、Flink等主流工具  

**性能优势**  
在SIFT数据集测试中，Lance向量搜索延迟低于1ms；相比Parquet，其分析查询性能提升50-100倍，随机访问速度提升100倍。