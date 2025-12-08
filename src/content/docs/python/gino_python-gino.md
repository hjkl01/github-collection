
---
title: gino
---

### [python-gino gino](https://github.com/python-gino/gino)

GINO 是一个基于 SQLAlchemy 核心的轻量级异步 ORM，专为 Python 的 asyncio 设计。它支持 PostgreSQL（通过 asyncpg）和 MySQL（通过 aiomysql），提供异步数据库操作能力。  

**使用方法**：通过 `pip install gino` 安装，支持与 SQLAlchemy 生态（如 Alembic 迁移工具）集成。  

**主要特性**：  
- 异步 SQLAlchemy-like 引擎与连接管理；  
- 支持异步数据库方言 API；  
- 提供面向异步操作的 CRUD 模型；  
- 兼容 SQLAlchemy 核心查询语法；  
- 社区支持主流异步框架（如 FastAPI、Starlette、aiohttp 等）；  
- 优化 PostgreSQL JSONB 字段操作。