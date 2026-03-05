
---
title: dbmate
---

### [amacneil dbmate](https://github.com/amacneil/dbmate)  ![GitHub Repo stars](https://img.shields.io/github/stars/amacneil/dbmate?style=social)

Dbmate 是一款独立的命令行数据库迁移工具，旨在跨不同开发者和生产服务器同步数据库架构。它支持多种数据库（如 MySQL、PostgreSQL、SQLite、ClickHouse、BigQuery 等），允许使用纯 SQL 编写迁移文件，并通过时间戳版本控制避免冲突。迁移操作在事务中原子执行，支持创建/删除数据库、导出 schema 文件、等待数据库就绪、回滚及状态检查等功能。工具支持通过环境变量或 `.env` 文件配置连接，也可作为 Go 库嵌入应用程序中使用，适用于多语言/多框架项目。