
---
title: airweave
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/airweave-ai/airweave?style=social) ](https://github.com/airweave-ai/airweave)
### [airweave-ai airweave](https://github.com/airweave-ai/airweave)

Airweave 是一个开源的 AI 代理用语义搜索平台，支持从 30+ 应用（如 Stripe、Slack、PostgreSQL 等）同步数据并建立知识库。其核心功能包括：  
1. **数据同步**：通过配置连接器自动从外部系统拉取数据，支持增量更新和版本控制。  
2. **语义搜索**：提供纯语义、混合（语义+关键词）、带权重的搜索模式，支持查询扩展、结果重排序、近期数据优先等高级功能。  
3. **开发支持**：提供 Python 和 TypeScript SDK，可创建数据集合、管理连接、执行搜索并获取 AI 生成的答案。  

**使用方式**：  
- 托管服务直接使用，自托管需通过 Docker 启动（`docker-compose up`），访问 `http://localhost:8080` 配置数据源，通过 `http://localhost:8001/docs` 调用 API。  
- SDK 安装后可初始化客户端，创建数据集、添加连接、执行多类型搜索。  

**技术特性**：基于 FastAPI（Python）+ React 构建，使用 PostgreSQL 存储元数据、Qdrant 管理向量数据，支持多租户架构和 OAuth2 认证。