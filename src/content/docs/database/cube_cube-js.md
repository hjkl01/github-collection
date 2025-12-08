
---
title: cube
---

### [cube-js cube](https://github.com/cube-js/cube)

**核心内容总结：**  
Cube 是一个开源的语义层工具，用于统一管理数据源并提供多维分析能力，支持 REST、GraphQL 和 SQL 等 API 接口，可替代 LookML。其核心功能包括：  
1. **兼容性**：支持 Snowflake、BigQuery、PostgreSQL 等 SQL 数据源，内置缓存引擎优化查询性能。  
2. **特性**：提供多维分析、智能缓存、访问控制、多协议 API（含 MDX/DAX 兼容性）。  
3. **使用方法**：  
   - 通过 [Cube Cloud](https://cube.dev/cloud) 快速部署托管服务。  
   - 使用 Docker 命令本地运行：`docker run -p 4000:4000 -p 15432:15432 -v ${PWD}:/cube/conf -e CUBEJS_DEV_MODE=true cubejs/cube`。  
4. **适用场景**：数据建模、跨应用数据治理、高性能分析查询。  

**主要优势**：解决云数据平台缺乏 OLAP 能力的问题，通过预聚合、缓存策略提升性能，统一数据权限管理，并兼容传统与现代分析工具接口。