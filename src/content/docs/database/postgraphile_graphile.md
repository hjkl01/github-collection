
---
title: postgraphile
---

### [graphile postgraphile](https://github.com/graphile/postgraphile)  ![GitHub Repo stars](https://img.shields.io/github/stars/graphile/postgraphile?style=social)

该项目是 Graphile 官方维护的 Monorepo，集成了多个与 GraphQL 及 PostgreSQL 相关的核心工具包，主要功能总结如下：

- **Grafast**：GraphQL.js 的高性能计划与执行引擎，可替代原生 execute 方法，利用声明式计划解析器优化业务逻辑执行，显著降低服务器负载。
- **PostGraphile**：基于 PostgreSQL 数据库快速构建高性能、结构化的 GraphQL API，支持自动生成类型与操作，并允许将 Schema 导出为独立管理的 JavaScript 源码。
- **核心辅助库**：提供 Schema 构建系统（graphile-build）、PostgreSQL 安全查询构建（pg-sql2）、类型化元数据检查（pg-introspection）、高性能 LRU 缓存（@graphile/lru）及统一配置管理（graphile-config）等工具。