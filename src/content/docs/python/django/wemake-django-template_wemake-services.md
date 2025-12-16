
---
title: wemake-django-template
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/wemake-services/wemake-django-template?style=social) ](https://github.com/wemake-services/wemake-django-template)
### [wemake-services wemake-django-template](https://github.com/wemake-services/wemake-django-template)

**核心内容总结：**  
该项目是基于 Django 5.2 的高质量代码模板，用于快速生成结构规范、安全性强的 Django 项目。  

**主要功能：**  
- 通过 `cookiecutter` 工具生成项目结构，优于默认的 `django-admin.py startproject`。  
- 支持最新 Python 3.12 和 Django 5.2。  

**核心特性：**  
- 自动更新依赖项（通过 Dependabot）。  
- 使用 Poetry 2 管理依赖，Mypy + Django-stubs 实现静态类型检查。  
- Pytest + Hypothesis 进行单元测试，Ruff + Wemake-Python-Styleguide 进行代码规范检查。  
- 集成 Docker（开发/测试/生产环境）、Sphinx 文档生成、Gitlab CI 流水线（含构建/测试/部署）。  
- 默认配置 Caddy 服务器（支持 HTTPS 和 HTTP/2）。  

**使用方法：**  
1. 安装依赖（推荐使用 `uvx` 或 `pipx`）。  
2. 运行 `cookiecutter gh:wemake-services/wemake-django-template` 生成项目。