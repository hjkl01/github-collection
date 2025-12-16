
---
title: airweave
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/airweave-ai/airweave?style=social) ](https://github.com/airweave-ai/airweave)
### [airweave-ai airweave](https://github.com/airweave-ai/airweave)

Airweave 是一个开源项目，提供 AI 代理的上下文检索功能，可连接 30 多种应用和数据库（如 Stripe、Slack、PostgreSQL 等），将数据转化为可搜索的知识库。用户可通过 REST API 或 MCP 接口进行语义搜索、混合搜索（语义+关键词）及 AI 生成答案。  

**使用方法**：  
- **托管服务**：直接使用云端服务；  
- **自托管**：通过 Docker Compose 部署，运行 `http://localhost:8080` 访问 UI，`http://localhost:8001/docs` 查看 API 文档；  
- **SDK**：支持 Python 和 TypeScript/JavaScript，提供创建数据集、连接数据源、执行搜索等操作。  

**核心特性**：  
- 支持 30+ 数据源的自动化同步；  
- 语义搜索、关键词混合搜索、查询扩展、结果重排序；  
- 增量更新、数据版本控制、多租户架构；  
- 技术栈包含 FastAPI（后端）、React/TypeScript（前端）、PostgreSQL 和 Qdrant（向量数据库）。