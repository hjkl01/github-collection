
---
title: spiceai
---

### [spiceai spiceai](https://github.com/spiceai/spiceai)  ![GitHub Repo stars](https://img.shields.io/github/stars/spiceai/spiceai?style=social)

Spice 是一个基于 Rust 开发的轻量级运行时引擎，专为数据应用和 AI 智能体提供 SQL 查询、搜索及 LLM 推理能力。其核心功能如下：

1. **统一 API 接口**：支持 SQL 查询与搜索（HTTP、Arrow Flight、JDBC/ODBC 等）、OpenAI 兼容接口、Iceberg Catalog REST API 及 MCP 集成。
2. **数据联邦与加速**：跨数据库、数据仓库和数据湖执行 SQL 查询；利用 Arrow、DuckDB、SQLite 或 Vortex 进行数据物化和缓存，支持单节点及分布式执行。
3. **AI 与搜索集成**：提供关键词、向量和全文搜索（支持 S3 Vectors/pgvector），支持检索增强生成（RAG）、智能体记忆及模型推理服务。
4. **灵活部署架构**：采用存算分离设计，支持侧边车、Kubernetes 等多种部署模式，覆盖边缘到云场景，兼容 OLAP 与 OLTP 负载。

项目基于 Apache DataFusion、Arrow 等技术构建，内置丰富的数据连接器、加速引擎及模型提供商支持。