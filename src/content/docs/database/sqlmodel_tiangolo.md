
---
title: sqlmodel
---

### [tiangolo sqlmodel](https://github.com/tiangolo/sqlmodel)

**核心内容总结：**

**项目功能：**  
SQLModel 是一个基于 Python 类型注解的库，用于简化 Python 与 SQL 数据库的交互。它结合了 Pydantic 和 SQLAlchemy，提供直观的模型定义和数据库操作，兼容 FastAPI、Pydantic 和 SQLAlchemy。

**主要特性：**  
1. **直观易用**：支持代码自动补全，减少调试时间；  
2. **代码简洁**：通过类型注解定义模型，避免 SQLAlchemy 和 Pydantic 的重复代码；  
3. **高度兼容**：与 FastAPI、Pydantic 和 SQLAlchemy 无缝集成；  
4. **功能强大**：底层依赖 SQLAlchemy 和 Pydantic，支持复杂数据库操作；  
5. **开发体验优化**：提供编辑器智能提示和错误检查，提升开发效率。

**使用方法：**  
1. **安装**：通过 `pip install sqlmodel` 安装；  
2. **定义模型**：继承 `SQLModel` 并设置字段，例如：  
   ```python  
   class Hero(SQLModel, table=True):  
       id: int | None = Field(default=None, primary_key=True)  
       name: str  
       secret_name: str  
       age: int | None = None  
   ```  
3. **数据库操作**：  
   - 创建数据库连接（如 SQLite）；  
   - 使用 `Session` 添加数据并提交；  
   - 通过 SQLAlchemy 的 `select` 语句查询数据。  

**适用场景：**  
适用于需要在 FastAPI 或其他 Python 项目中高效管理 SQL 数据库的场景，尤其适合希望减少模型定义重复、提升开发效率的开发者。