
---
title: sqlx
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/launchbadge/sqlx?style=social) ](https://github.com/launchbadge/sqlx)
### [launchbadge sqlx](https://github.com/launchbadge/sqlx)

**项目核心内容总结：**  
sqlx 是一个用于 Rust 的异步数据库操作库，支持 PostgreSQL、MySQL、MariaDB、SQLite 等多种数据库，提供以下功能与特性：  

1. **核心功能**  
   - **连接池管理**：通过 `Pool` 对象管理数据库连接，支持自定义最大连接数。  
   - **查询执行**：支持参数化查询（防止 SQL 注入）与非参数化查询，提供 `execute`、`fetch` 等方法处理结果。  
   - **编译时验证**：通过 `sqlx::query!` 和 `sqlx::query_as!` 宏实现 SQL 语法与语义的编译时检查，自动映射查询结果到结构体或匿名记录。  

2. **使用方法**  
   - **连接数据库**：使用 `connect` 方法建立连接或连接池（如 `PgPoolOptions::new()`）。  
   - **执行查询**：通过 `sqlx::query` 或宏实现查询，支持绑定参数（如 `.bind(150_i64)`）。  
   - **结果处理**：使用 `fetch_one`、`fetch_all` 等方法获取结果，或通过 `map` 将行映射到自定义结构体（需实现 `FromRow` trait）。  

3. **主要特性**  
   - **异步支持**：基于 `futures` 库，适用于异步运行时（如 Tokio）。  
   - **安全代码**：默认使用 100% 安全 Rust 实现，仅 SQLite 模块允许部分 `unsafe` 代码。  
   - **编译优化**：支持离线模式缓存查询分析结果，提升构建速度。  
   - **跨数据库兼容**：统一 API 设计，适配多种数据库方言（如 PostgreSQL 的 `$1` 参数与 MySQL 的 `?` 参数）。  

**注意事项**：使用 `query!` 宏需配置 `DATABASE_URL` 环境变量，指向编译时验证的数据库实例。