
---
title: spiceai
---

### [spiceai spiceai](https://github.com/spiceai/spiceai)  ![GitHub Repo stars](https://img.shields.io/github/stars/spiceai/spiceai?style=social)

Spice 是一款基于 Rust 开发的轻量级运行时引擎，旨在为数据应用和 AI 智能体提供统一的 SQL 查询、搜索及大语言模型（LLM）推理服务。

核心功能包括：
1. **数据联邦**：支持跨数据库、数据仓库及数据湖的 SQL 查询，可水平扩展至分布式多节点执行。
2. **数据加速与物化**：利用 Arrow、DuckDB、SQLite 或 Cayenne 等技术加速查询、缓存和物化数据，支持从 S3 快照实现快速冷启动。
3. **企业级搜索**：集成 Tantivy 实现关键词与全文搜索，支持 Amazon S3 Vectors 进行 PB 级向量相似性搜索。
4. **AI 智能体支持**：提供 OpenAI 兼容 API 和本地模型服务，支持检索增强生成（RAG）、MCP 集成及模型评估。
5. **多标准接口**：提供 SQL、OpenAI、Iceberg Catalog 及 MCP HTTP+SSE 四种行业标准 API。

支持从边缘到云原生的多种部署模式（如 Kubernetes 侧车、微服务、集群），将计算与存储解耦，帮助开发者将数据与 AI 推理整合在同一引擎中。