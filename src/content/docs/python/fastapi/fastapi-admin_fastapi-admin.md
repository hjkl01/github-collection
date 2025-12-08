
---
title: fastapi-admin
---

### [fastapi-admin fastapi-admin](https://github.com/fastapi-admin/fastapi-admin)

**项目核心内容总结：**

`fastapi-admin` 是一个基于 FastAPI 和 TortoiseORM 的快速管理后台系统，采用 Tabler UI 界面设计，灵感来源于 Django Admin。  

**功能与特性**  
- 提供可视化管理界面，支持数据库模型管理、数据操作等功能。  
- 默认集成 Redis 作为缓存。  
- 提供在线演示环境（含管理员账号），可访问 [演示链接](https://fastapi-admin.long2ice.io/admin/login)。  
- 支持通过 Docker 快速部署，提供本地运行示例的完整步骤。  
- 官方文档完整，支持中文、韩文、日文多语言。  

**使用方法**  
1. 安装：`pip install fastapi-admin`  
2. 配置环境变量（如数据库连接、Redis 地址）。  
3. 使用 Docker 启动服务，访问 `http://localhost:8000/admin/init` 初始化管理员账号。  
4. 通过浏览器访问管理后台进行操作。  

**依赖要求**  
- 需安装 Redis 服务。  
- 示例中使用 MySQL 数据库（需提前安装）。