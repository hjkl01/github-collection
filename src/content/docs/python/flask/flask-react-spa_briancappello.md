
---
title: flask-react-spa
---

### [briancappello flask-react-spa](https://github.com/briancappello/flask-react-spa)

**项目核心内容总结：**  

**功能**：该项目是一个基于 Flask 和 React 的单页应用（SPA）框架，包含完整的前后端功能。前端使用 React、Redux 和 Webpack，支持热加载、代码分割；后端基于 Flask，集成 SQLAlchemy（ORM）、Flask-Security（认证授权）、Celery（异步任务）等，提供 RESTful API、用户权限管理、数据库迁移、邮件发送等功能。  

**使用方法**：  
- **Docker 部署**：通过 `docker-compose` 一键启动，需配置环境文件并运行命令 `docker-compose up --build`。  
- **本地开发**：需安装 Python 3.6+、PostgreSQL/Redis、Node.js 等，配置后运行数据库迁移、启动前端开发服务器和后端服务。  

**主要特性**：  
- 前端：React Router、Redux-Saga 状态管理、Webpack 优化（树摇、代码分割）。  
- 后端：Flask-Security 认证授权、Flask-Admin 数据管理、Celery 异步任务、数据库迁移支持。  
- 部署：支持 Ansible 自动化部署，包含 HTTPS、邮件测试（MailHog）等生产环境配置。