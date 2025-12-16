
---
title: pgx
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/jackc/pgx?style=social) ](https://github.com/jackc/pgx)
### [jackc pgx](https://github.com/jackc/pgx)

**项目核心内容总结：**

pgx 是一个用于 PostgreSQL 的高性能 Go 语言驱动和工具包，提供直接访问 PostgreSQL 特有功能（如 `LISTEN`/`NOTIFY`、`COPY` 协议）的低级别接口，同时兼容标准 `database/sql` 接口。

**使用方法**：通过 `Connect` 建立数据库连接，使用 `QueryRow` 执行 SQL 查询并用 `Scan` 获取结果，支持通过环境变量配置连接参数。

**主要特性**：
- 支持 70+ PostgreSQL 数据类型，包括 `json`、`hstore`、`inet` 等；
- 提供自动语句缓存、批量查询、单次往返模式等性能优化；
- 支持 TLS、二进制格式传输、`COPY` 协议实现高速数据导入；
- 包含连接池、通知响应处理、模拟嵌套事务等高级功能；
- 支持自定义类型与 `database/sql` 接口适配。

**适用场景**：推荐在仅使用 PostgreSQL 的场景下优先使用 pgx 接口，以获得更优性能和功能；若需兼容其他数据库，可通过 `database/sql` 接口实现。

**支持版本**：Go 1.24+、PostgreSQL 13+，并兼容 CockroachDB。

**相关库**：包含逻辑复制、模拟服务器、SQL 迁移等工具，以及第三方适配器（如 UUID、PostGIS）和第三方库（如 mock 框架、ORM 工具）。