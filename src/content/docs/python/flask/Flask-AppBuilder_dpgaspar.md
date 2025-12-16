
---
title: Flask-AppBuilder
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/dpgaspar/Flask-AppBuilder?style=social) ](https://github.com/dpgaspar/Flask-AppBuilder)
### [dpgaspar Flask-AppBuilder](https://github.com/dpgaspar/Flask-AppBuilder)

**Flask App Builder 核心内容总结**  

**项目功能**  
Flask App Builder 是基于 Flask 的快速应用开发框架，提供自动化的 CRUD（增删改查）功能、数据库支持、安全权限管理、图表集成、REST API 生成等能力，适用于构建企业级 Web 应用。  

**使用方法**  
1. 通过 PyPI 安装（`pip install Flask-AppBuilder`）；  
2. 参考官方文档（[链接](http://flask-appbuilder.readthedocs.org/en/latest/)）配置数据库、安全权限及视图；  
3. 使用示例代码（[GitHub 示例](https://github.com/dpgaspar/Flask-AppBuilder/tree/master/examples)）快速搭建应用。  

**主要特性**  
- **数据库支持**：兼容 SQLite、MySQL、Oracle、MongoDB 等，支持多数据库连接及模型审计（记录操作者和时间）。  
- **安全权限**：基于角色的权限控制（RBAC），支持 OAuth、OpenID、LDAP 等认证方式，自动记录详细权限信息。  
- **自动化功能**：自动生成菜单、CRUD 界面、REST API，支持 Google 图表、筛选器、多语言（Babel）。  
- **灵活扩展**：提供自定义表单、视图组件、图表配置，支持与 Flask-JWT-Extended 集成保护 API 端点。  
- **前端集成**：内置 Bootstrap 3.1.1、Font-Awesome 图标、Select2 和日期选择器，支持文件上传和图片处理。  

**依赖库**  
Flask、Flask-SQLAlchemy、Flask-Login、Flask-Babel 等。