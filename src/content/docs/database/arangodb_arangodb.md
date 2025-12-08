
---
title: arangodb
---

### [arangodb arangodb](https://github.com/arangodb/arangodb)

ArangoDB 是一个支持图数据库、文档存储和全文搜索的多模型数据库系统，提供统一的查询语言（AQL）。其核心功能包括：  
1. **原生图数据库**：高效处理复杂关系数据，支持多层级连接查询；  
2. **灵活数据模型**：兼容 JSON 文档存储，支持无模式或模式验证；  
3. **ArangoSearch**：集成全文检索与索引功能，优化搜索性能。  

**使用方式**：  
- 通过 [ArangoDB Cloud](https://cloud.arangodb.com/home) 快速部署；  
- 本地安装或使用 Docker 启动（命令：`docker run -e ARANGO_ROOT_PASSWORD=test123 -p 8529:8529 -d arangodb`）；  
- 提供学习资源（文档、培训课程等）。  

**核心特性**：  
- 支持水平扩展、高可用集群、自动故障转移；  
- 支持事务、数据加密、跨数据中心复制等企业级功能；  
- 提供 Web 界面和命令行工具，兼容多平台部署。  

提供免费社区版和商业企业版，适用于大规模数据场景。