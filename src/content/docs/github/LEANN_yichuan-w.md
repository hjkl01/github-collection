
---
title: LEANN
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/yichuan-w/LEANN?style=social) ](https://github.com/yichuan-w/LEANN)
### [yichuan-w LEANN](https://github.com/yichuan-w/LEANN)

**项目核心内容总结：**

**功能**  
LEANN 是一个低存储向量索引工具，通过图结构优化存储效率，支持高效搜索、元数据过滤、精确文本匹配（Grep）等功能，适用于大规模数据集的语义检索与分析。

**使用方法**  
1. **CLI 命令**：通过 `leann build` 构建索引，`leann search` 进行语义搜索，`leann ask` 启动交互式问答。  
2. **Python API**：支持添加文本与元数据、带条件的搜索（如按文件类型、代码行数过滤）。  

**主要特性**  
- **存储优化**：相比传统向量数据库（如 FAISS），存储节省达 90% 以上（如 DPR 数据集节省 91%）。  
- **高效搜索**：采用图结构选择性重新计算、动态批处理技术，支持 HNSW 和 DiskANN 两种后端，兼顾速度与精度。  
- **灵活过滤**：支持元数据条件筛选（如 `file_extension == ".py"`）、精确文本匹配（Grep）。  
- **跨平台兼容**：提供 CLI 工具与 Python 接口，适配不同使用场景。  

**适用场景**  
大规模文本/代码检索、语义相似度分析、需要高效存储与快速查询的 AI 应用。