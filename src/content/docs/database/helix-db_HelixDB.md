
---
title: helix-db
---

### [HelixDB helix-db](https://github.com/HelixDB/helix-db)  ![GitHub Repo stars](https://img.shields.io/github/stars/HelixDB/helix-db?style=social)

HelixDB 是一个基于 Rust 从头构建的开源图向量数据库，旨在为 AI 应用提供统一的数据存储平台，无需组合多种独立数据库。它采用图 + 向量核心数据模型，同时支持 KV、文档及关系型数据。项目内置文本向量化功能与 MCP 工具以支持 Agent 访问，提供向量搜索、关键词搜索及图遍历能力以构建 RAG 应用。基于 Rust 和 LMDB 引擎实现超低延迟，默认私有化安全，仅允许通过编译后的 HelixQL 类型安全查询访问数据，并提供 CLI 工具及 TypeScript/Python SDK 便于部署与调用。