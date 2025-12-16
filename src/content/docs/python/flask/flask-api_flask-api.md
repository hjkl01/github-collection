
---
title: flask-api
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/flask-api/flask-api?style=social) ](https://github.com/flask-api/flask-api)
### [flask-api flask-api](https://github.com/flask-api/flask-api)

**核心内容总结：**  
Flask API 是 Flask 的扩展，提供类似 Django REST framework 的可浏览 API 功能，支持自动内容协商（根据客户端请求头选择 JSON 或 HTML 响应）和智能请求解析（自动处理 JSON 或表单数据）。  

**使用方法：**  
1. 安装：`pip install Flask-API`，并导入 `FlaskAPI` 初始化应用。  
2. 定义路由时返回字典或列表，系统会自动选择渲染器生成响应。  
3. 通过 `request.data` 获取解析后的请求数据（支持 JSON 或表单格式）。  

**主要特性：**  
- 自动根据客户端请求内容（如 Accept 头）返回 JSON 或可浏览的 HTML 界面。  
- 支持 RESTful 操作（GET/POST/PUT/DELETE），示例包含增删改查功能。  
- 项目处于维护模式，原作者已转向其他项目，但维护者仍接受合理 PR。