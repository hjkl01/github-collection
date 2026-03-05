
---
title: sqlx
---

### [launchbadge sqlx](https://github.com/launchbadge/sqlx)  ![GitHub Repo stars](https://img.shields.io/github/stars/launchbadge/sqlx?style=social)

SQLx 是一个基于 Rust 的异步 SQL 工具包，支持 PostgreSQL、MySQL、MariaDB 和 SQLite 数据库，兼容 tokio、async-std 等运行时。其核心功能包括：完全异步操作、编译时查询检查（通过连接开发数据库验证标准 SQL 而非 DSL）、纯 Rust 实现（SQLite 除外）、内置连接池、行流式读取、自动语句缓存、TLS 支持及事务管理。项目提供 `query!` 和 `query_as!` 宏以验证 SQL 安全性，支持迁移管理、derive 宏及运行时数据库切换。SQLx 明确声明不是 ORM，不通过 Rust API 构建查询。