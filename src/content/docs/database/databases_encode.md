
---
title: databases
---

### [encode databases](https://github.com/encode/databases)

**项目功能**  
Databases 是一个 Python 库，提供对 PostgreSQL、MySQL、SQLite 等数据库的异步支持，允许使用 SQLAlchemy Core 表达式语言进行查询，适用于 Starlette、Sanic、FastAPI 等异步 Web 框架。

**使用方法**  
1. 安装：通过 `pip install databases` 安装主库，再根据需求安装对应数据库驱动（如 `pip install databases[asyncpg]`）。  
2. 示例：连接数据库后，可执行建表、插入数据、查询等操作，支持异步执行（如 `await database.connect()`）。

**主要特性**  
- 支持异步数据库操作，兼容主流异步框架。  
- 使用 SQLAlchemy Core 进行灵活查询。  
- 同步操作（如 Alembic 迁移）需额外安装同步驱动（如 psycopg2、pymysql）。