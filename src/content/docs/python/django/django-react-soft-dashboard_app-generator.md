
---
title: django-react-soft-dashboard
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/app-generator/django-react-soft-dashboard?style=social) ](https://github.com/app-generator/django-react-soft-dashboard)
### [app-generator django-react-soft-dashboard](https://github.com/app-generator/django-react-soft-dashboard)

**项目核心内容总结：**

**项目功能**  
- 提供一个基于 **Material-UI** 的 React 前端与 **Django API** 后端的全栈仪表盘模板，支持用户注册、登录、注销的 JWT 认证流程。  
- 前端包含 70+ 可复用组件（如按钮、卡片、导航栏等），后端基于 Django/DRF，提供 SQLite3 数据库支持、单元测试和 Docker 部署方案。  

**使用方法**  
1. **启动 Django API**  
   - 使用 Docker：进入 `django-api` 目录，执行 `docker-compose up --build`，后端服务运行于 `http://localhost:5000`。  
   - 手动启动：创建虚拟环境、安装依赖、配置 `.env` 文件，运行 `python manage.py runserver 5000`。  

2. **启动 React 前端**  
   - 进入 `react-ui` 目录，执行 `yarn` 安装依赖，再运行 `yarn start`，前端服务运行于 `http://localhost:3000`。  

**主要特性**  
- **Material-UI 设计**：由 Creative-Tim 提供，支持灵活的组件组合。  
- **全栈集成**：前后端分离，支持自定义 API 端口配置。  
- **开发便捷性**：提供 Docker 快速部署、JWT 认证接口（含 Postman 示例）、多版本 NodeJS 兼容性测试。  
- **扩展性强**：后端支持单元测试，前端使用 Redux 管理状态，适配多种开发场景。