
---
title: cookiecutter-flask-restful
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/karec/cookiecutter-flask-restful?style=social) ](https://github.com/karec/cookiecutter-flask-restful)
### [karec cookiecutter-flask-restful](https://github.com/karec/cookiecutter-flask-restful)

**项目核心内容总结：**  
该项目是一个基于Flask的Web应用模板，集成API文档生成（Swagger/ReDoc）、Celery异步任务、Docker部署及自动化测试功能。  

**主要功能与特性：**  
1. **快速开发**：提供Flask应用框架，支持数据库迁移（Flask-Migrate）、API接口自动生成（OpenAPI规范）。  
2. **异步任务支持**：集成Celery，可配置RabbitMQ/Redis作为消息代理，支持任务执行与测试。  
3. **开发与测试工具**：内置Makefile管理初始化、构建、测试、数据库操作；支持pytest、tox进行单元测试与代码检查（flake8）。  
4. **容器化部署**：提供Dockerfile与docker-compose.yml，支持开发环境快速启动，包含Web服务、Celery worker及消息队列。  
5. **API文档**：自动生成Swagger UI与ReDoc界面，支持JSON/YAML格式的OpenAPI文档。  

**使用方法：**  
- 初始化项目：通过`make init`配置环境变量。  
- 启动服务：使用`gunicorn`或`uwsgi`部署，或通过`docker-compose up`启动容器。  
- 数据库操作：执行`make db-init`、`make db-migrate`等命令管理迁移。  
- 测试：运行`make test`执行单元测试与代码检查。  
- Celery任务：通过`celery -A myapi.celery_app:app worker`启动worker，或使用`docker-compose`管理。