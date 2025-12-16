
---
title: sqladmin
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/aminalaee/sqladmin?style=social) ](https://github.com/aminalaee/sqladmin)
### [aminalaee sqladmin](https://github.com/aminalaee/sqladmin)

SQLAdmin 是一个为 SQLAlchemy 模型提供管理界面的工具，支持 Starlette 和 FastAPI 框架。核心功能包括：  
- 支持 SQLAlchemy 同步/异步引擎  
- 集成 Starlette 和 FastAPI  
- 使用 WTForms 构建表单  
- 支持 SQLModel  
- 采用 Tabler 框架实现 UI  

**使用方法**：  
1. 安装：`pip install sqladmin` 或 `pip install "sqladmin[full]"`  
2. 定义 SQLAlchemy 模型并创建数据库引擎  
3. 在 FastAPI/Starlette 应用中初始化 `Admin`，通过继承 `ModelView` 定义模型视图类并注册  

**主要特性**：  
- 提供基于浏览器的数据库管理界面  
- 支持多种 ORM 和数据库引擎  
- 界面简洁，功能与 Flask-Admin 类似  
- 可通过 `/admin` 路径访问管理界面  

**示例**：  
定义模型后，通过继承 `ModelView` 并注册至 `Admin` 实例，即可在应用中访问管理界面。