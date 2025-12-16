
---
title: flask-vuejs-template
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/gtalarico/flask-vuejs-template?style=social) ](https://github.com/gtalarico/flask-vuejs-template)
### [gtalarico flask-vuejs-template](https://github.com/gtalarico/flask-vuejs-template)

**项目核心内容总结：**  
该模板结合 Flask（Python 后端框架）和 Vue.js（前端框架），提供一个全栈 Web 应用开发模板。  

**主要功能与特性：**  
1. **后端功能**：基于 Flask 1.0 和 Flask-RestPlus 构建 REST 风格 API，支持安全的类视图路由；提供 PyTest 测试套件。  
2. **前端功能**：使用 Vue CLI 3 + Vuex + Vue Router + Axios 实现前端框架，支持过滤器（Filters）等功能。  
3. **部署支持**：预配置 Heroku 一键部署，支持 Gunicorn + Python 虚拟环境。  
4. **结构优化**：采用扁平化文件结构，Yarn 管理依赖，分离 Flask API（`/api`）与 Vue 前端（`/`）入口。  

**使用方法：**  
1. **安装依赖**：需 Python 3、Yarn、Vue CLI，通过 `pipenv` 安装 Python 依赖，`yarn install` 安装前端依赖。  
2. **开发环境**：运行 `python run.py` 启动 Flask 服务，`yarn serve` 启动 Vue 开发服务器（前端 `localhost:8080`，后端 `localhost:5000`）。  
3. **生产环境**：通过 Heroku 部署，需配置 Node.js 和 Python 构建包，设置环境变量后推送代码即可部署。  

**适用场景**：适合需要快速搭建 Flask + Vue.js 全栈项目的开发者，支持 REST API 开发、前后端分离、自动化测试及云部署。