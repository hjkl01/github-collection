
---
title: sqlalchemy
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/sqlalchemy/sqlalchemy?style=social) ](https://github.com/sqlalchemy/sqlalchemy)
### [sqlalchemy sqlalchemy](https://github.com/sqlalchemy/sqlalchemy)

**项目功能**  
SQLAlchemy 是 Python 的 SQL 工具包和对象关系映射器（ORM），提供企业级数据库访问模式，支持高效、灵活的数据库操作，通过 Pythonic 的方式实现对象与数据库的映射。

**主要特性**  
1. **工业级 ORM**：基于身份映射、工作单元和数据映射器模式，支持对象的透明持久化，使用声明式配置系统。  
2. **关系查询系统**：支持 SQL 的全部功能（如连接、子查询），通过对象模型进行查询，无需直接使用 SQL。  
3. **灵活加载系统**：支持缓存、按需加载、批量加载等策略，优化查询效率。  
4. **核心 SQL 构建系统**：独立于 ORM，提供 SQL 表达式语言、连接池、类型系统等，适配多种数据库。  
5. **数据库自省与生成**：可反射数据库结构为 Python 对象，并生成建表语句。  
6. **哲学原则**：强调开发者对查询结构、数据库设计的完全控制，避免 ORM 自动生成低效查询，支持事务管理和参数绑定以防止 SQL 注入。

**使用方法**  
- 安装：通过 PyPI 安装（`pip install sqlalchemy`）。  
- 文档：参考 [https://www.sqlalchemy.org/docs/](https://www.sqlalchemy.org/docs/)。  
- 适用场景：适合需要 ORM 的复杂数据库操作，也可单独使用 Core 进行 SQL 构建。  

**许可证**  
采用 MIT 开源协议。