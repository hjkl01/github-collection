
---
title: wemake-django-template
---

### [wemake-services wemake-django-template](https://github.com/wemake-services/wemake-django-template)  ![GitHub Repo stars](https://img.shields.io/github/stars/wemake-services/wemake-django-template?style=social)

wemake-django-template 是一个专注于代码质量和安全性的 Django 5.2 项目脚手架模板，旨在提供比标准 django-admin 更完善的初始化方案。

主要功能包括：
- 依赖管理：支持 Python 3.13，使用 Poetry 管理依赖，并通过 Dependabot 保持依赖更新。
- 代码规范：集成 MyPy 和 django-stubs 进行静态类型检查，使用 Ruff 和 wemake-python-styleguide 进行代码风格审查。
- 测试与文档：内置 pytest 和 hypothesis 单元测试框架，以及 Sphinx 文档生成工具。
- 部署运维：包含 Docker 环境配置、Gitlab CI 流水线及默认开启 HTTPS 的 Caddy 服务器。
- 快速生成：通过 Cookiecutter 工具一键创建项目结构。