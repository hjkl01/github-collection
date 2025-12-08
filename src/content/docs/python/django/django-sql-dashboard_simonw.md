
---
title: django-sql-dashboard
---

### [simonw django-sql-dashboard](https://github.com/simonw/django-sql-dashboard)

**项目核心内容总结：**  
django-sql-dashboard 是一个 Django 应用，提供基于浏览器的界面，用于安全执行只读 SQL 查询并查看 PostgreSQL 数据库结果。其主要功能包括：执行查询、保存书签、创建可共享的仪表板、通过参数生成交互式图表、导出查询结果为 CSV/TSV 文件，并集成 Django 认证系统。支持生成柱状图、进度条等可视化组件，以及通过 Markdown/HTML 渲染内容。用户可通过 Django 管理工具控制访问权限，适用于数据分析、调试及报告制作。  

**使用方法：**  
安装后配置 Django 项目，集成 PostgreSQL 数据库，通过界面输入 SQL 查询，使用内置功能生成仪表板并管理权限。  

**主要特性：**  
- 安全执行只读查询，支持参数化 SQL（如 `%(id)s`）生成交互表单  
- 保存查询、创建可共享仪表板，控制查看/编辑权限  
- 生成图表（柱状图、进度条）及自定义组件  
- 支持大型数据导出（CSV/TSV）及直接复制到 Excel/Google Sheets  
- 与 Django 认证系统集成，权限由 Django 管理