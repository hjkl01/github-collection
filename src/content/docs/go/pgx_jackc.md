
---
title: pgx
---

### [jackc pgx](https://github.com/jackc/pgx)  ![GitHub Repo stars](https://img.shields.io/github/stars/jackc/pgx?style=social)

pgx 是一个用于 PostgreSQL 的纯 Go 驱动和工具包，主要功能总结如下：

1. **核心驱动**：提供高性能低层接口，暴露 PostgreSQL 特有功能（如 LISTEN/NOTIFY、COPY），并包含标准 `database/sql` 接口适配器。
2. **工具组件**：提供 Wire 协议解析和类型映射等底层包，可用于实现替代驱动、代理、负载均衡器或逻辑复制客户端。
3. **主要特性**：支持约 70 种 PostgreSQL 类型，具备自动语句准备与缓存、批处理查询、单轮次传输、二进制格式支持、COPY 批量加载、连接池管理及 TLS 控制等功能。
4. **生态扩展**：提供逻辑复制（pglogrepl）、协议模拟（pgmock）、SQL 迁移（tern）等配套库，并支持广泛的第三方 UUID、Decimal、日志追踪及数据扫描库适配器。