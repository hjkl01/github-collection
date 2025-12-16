
---
title: django-sql-explorer
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/groveco/django-sql-explorer?style=social) ](https://github.com/groveco/django-sql-explorer)
### [groveco django-sql-explorer](https://github.com/groveco/django-sql-explorer)

**核心内容总结：**

SQL Explorer 是一个基于 Django 的数据查询与分析工具，支持连接任意 Django 支持的 SQL 数据库，以及用户上传的 CSV、JSON、SQLite 文件。主要功能包括：  
- **快速查询**：提供 SQL 编辑器，支持实时查看结果、数据统计、数据透视表和散点图。  
- **AI 助手**：集成 OpenAI 等 API，提供智能 SQL 生成与调试帮助。  
- **灵活管理**：支持多数据库连接、用户上传文件、定时数据快照、查询历史记录与日志。  
- **交互功能**：参数化查询生成可视化表单、邮件发送结果、通过 API 暴露保存的查询。  

**使用方法**：  
通过 Docker Compose 启动测试项目（`docker compose up`），访问 `127.0.0.1:8000/explorer/`，使用 `admin/admin` 登录即可体验。前端修改支持热重载。  

**主要特性**：  
多数据源支持、AI 辅助查询、数据可视化、参数化查询、定时快照、查询日志、邮件发送结果、API 接口等。