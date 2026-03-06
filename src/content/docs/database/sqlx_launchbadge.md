
---
title: sqlx
---

### [launchbadge sqlx](https://github.com/launchbadge/sqlx)  ![GitHub Repo stars](https://img.shields.io/github/stars/launchbadge/sqlx?style=social)

SQLx 是一个纯 Rust 编写的异步 SQL 工具包，支持 PostgreSQL、MySQL、MariaDB 和 SQLite。它提供编译时检查的查询功能，通过宏验证 SQL 有效性而无需 DSL。核心特性包括：完全异步（基于 async/await）、支持多种运行时（tokio、async-std 等）和 TLS 后端、内置连接池、行流式读取、自动语句缓存、异步通知及嵌套事务。SQLx 明确声明不是 ORM，而是允许直接使用原生 SQL 的库。此外，它还支持迁移管理、离线模式及除 SQLite 外保持 100% 安全 Rust 代码。