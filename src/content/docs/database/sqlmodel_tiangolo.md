
---
title: sqlmodel
---

### [tiangolo sqlmodel](https://github.com/tiangolo/sqlmodel)  ![GitHub Repo stars](https://img.shields.io/github/stars/tiangolo/sqlmodel?style=social)

SQLModel 是一个基于 Python 类型注解的库，用于通过 Python 对象与 SQL 数据库交互。它整合了 Pydantic 和 SQLAlchemy，旨在简化 FastAPI 应用中的数据库操作。

主要功能：
1. **模型统一**：数据库模型同时是 SQLAlchemy 和 Pydantic 模型，避免代码重复。
2. **体验优化**：提供优秀的编辑器自动补全和类型提示支持。
3. **生态兼容**：完全兼容 FastAPI、Pydantic 和 SQLAlchemy。
4. **简化操作**：支持通过 Python 类定义数据库表，通过实例轻松完成数据库的增删改查。