
---
title: cookiecutter-flask
---

### [cookiecutter-flask cookiecutter-flask](https://github.com/cookiecutter-flask/cookiecutter-flask)

**核心内容总结：**  
`cookiecutter-flask` 是一个基于 Flask 的项目模板，支持 Python 3.8 及以上版本，提供完整的 Web 开发基础结构。  

**功能与特性：**  
- 集成 Bootstrap 5、Font Awesome 6、Flask-SQLAlchemy、Flask-Migrate 等工具，支持数据库迁移和用户认证（含 Flask-Login、Flask-Bcrypt）。  
- 配置通过环境变量实现（符合 Twelve-Factor App 规范），支持测试（pytest + Factory-Boy）、前端资源管理（Webpack + npm）、缓存（Flask-Cache）及调试工具栏。  
- 采用蓝图（Blueprints）和应用工厂（Application Factory）模式，代码结构清晰。  

**使用方法：**  
1. **Docker 方式（推荐）：**  
   克隆模板仓库后，运行 `./cookiecutter-docker.sh`，按提示生成项目。  
2. **标准方式：**  
   安装 `cookiecutter`，执行命令 `cookiecutter https://github.com/cookiecutter-flask/cookiecutter-flask.git`，填写项目信息生成代码。  

**其他：**  
生成的项目需根据其 README 进行后续配置与运行，支持 GitHub Actions 进行 CI 流水线构建。