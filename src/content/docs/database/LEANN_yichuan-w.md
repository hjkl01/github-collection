
---
title: LEANN
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/yichuan-w/LEANN?style=social) ](https://github.com/yichuan-w/LEANN)
### [yichuan-w LEANN](https://github.com/yichuan-w/LEANN)

**项目核心内容总结：**  
LEANN 是一个高效存储的向量索引系统，支持实时检索、多源数据处理及大规模数据的快速搜索。其核心特性包括：  
1. **低存储消耗**：通过图结构选择性重新计算和高阶节点保留修剪，存储节省达90%以上（如传统系统存储3.8GB的数据，LEANN仅需324MB）。  
2. **高效检索**：支持两种后端（HNSW/DiskANN），结合动态批处理和两阶段搜索技术，兼顾速度与精度。  
3. **灵活功能**：提供CLI命令（构建、搜索、询问）和Python API，支持元数据过滤（如按文件类型、代码行数筛选）及精确文本匹配（grep搜索）。  
4. **应用场景**：适用于文档检索、代码分析、知识库管理等需处理大规模数据的场景。  

**使用方法**：  
- **CLI命令**：通过 `leann build` 构建索引，`leann search` 进行语义搜索，`leann ask` 启动交互式问答。  
- **Python API**：支持添加文本时附加元数据，并通过 `search` 方法结合元数据过滤条件进行查询。