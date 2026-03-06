
---
title: sea-orm
---

### [SeaQL sea-orm](https://github.com/SeaQL/sea-orm)  ![GitHub Repo stars](https://img.shields.io/github/stars/SeaQL/sea-orm?style=social)

SeaORM 是一个用于 Rust 语言的功能强大且生产级别的 ORM 框架，专为构建 Web 服务设计。其核心功能包括：

1.  **复杂关系处理**：支持 1-1、1-N、M-N 及自引用关系的高级建模与高效查询。
2.  **智能加载**：通过智能实体加载器自动优化连接与数据加载策略，消除 N+1 查询问题。
3.  **灵活开发模式**：支持 Schema First 和 Entity First 工作流，可自动检测架构变更并生成迁移；提供 ActiveModel 以简化嵌套对象的持久化操作。
4.  **查询能力**：支持链式查询、过滤器、分页、嵌套查询及原生 SQL 宏，同时提供同步 API 以支持轻量级 CLI 应用。
5.  **生态集成**：兼容主流 Web 框架（如 Actix、Axum 等），内置 GraphQL 框架（Seaography）及管理面板解决方案（SeaORM Pro），并提供 SQL Server 支持。