
---
title: django-import-export
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/django-import-export/django-import-export?style=social) ](https://github.com/django-import-export/django-import-export)
### [django-import-export django-import-export](https://github.com/django-import-export/django-import-export)

**项目核心内容总结：**  

**功能**：  
django-import-export 是一个 Django 应用和库，支持通过 Admin 界面或编程方式实现数据的导入/导出，兼容 CSV、JSON、XLSX 等多种格式，并基于 tablib 库扩展其他格式支持。  

**主要特性**：  
- 支持 Admin 界面集成与编程操作，提供数据预览、批量导入、外键及多对多关系处理；  
- 可定义数据验证规则、自定义导出转换逻辑、使用自然键实现环境间数据迁移；  
- 支持权限控制、多语言、暗色模式，兼容 MySQL/PostgreSQL/SQLite；  
- 集成 Celery 实现异步导入，提供 Docker 测试环境和详尽文档；  
- 支持字段筛选、单条数据导出、导入编码处理等高级功能。  

**使用方法**：  
通过安装文档配置项目，定义数据资源类，利用 Admin 界面或调用 API 实现导入/导出操作，参考示例应用和教程快速上手。