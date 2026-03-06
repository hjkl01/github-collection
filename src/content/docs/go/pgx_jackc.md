
---
title: pgx
---

### [jackc pgx](https://github.com/jackc/pgx)  ![GitHub Repo stars](https://img.shields.io/github/stars/jackc/pgx?style=social)

pgx 是一个纯 Go 编写的高性能 PostgreSQL 驱动程序及工具集。

1. **核心功能**：提供低层高性能接口，支持 PostgreSQL 特有功能（如 LISTEN/NOTIFY、COPY），并兼容标准 `database/sql` 接口。
2. **特性支持**：支持 70+ 种 PostgreSQL 类型、自动语句缓存、批量/单轮询查询、二进制格式、连接池、TLS 控制、日志追踪及嵌套事务模拟。
3. **工具包**：包含 Wire 协议解析和类型映射包，可用于构建代理、负载均衡器或逻辑复制客户端。
4. **生态扩展**：提供逻辑复制客户端、协议 Mock、SQL 迁移工具，以及针对 UUID、Decimal、Geo 等类型的适配器和日志/追踪库集成。