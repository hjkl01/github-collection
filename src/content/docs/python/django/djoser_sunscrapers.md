
---
title: djoser
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/sunscrapers/djoser?style=social) ](https://github.com/sunscrapers/djoser)
### [sunscrapers djoser](https://github.com/sunscrapers/djoser)

**djoser** 是一个基于 Django 和 Django REST Framework 的认证系统实现，提供用户注册、登录、注销、密码重置、账户激活等基础功能。其核心特性包括：支持令牌（Token）和 JWT 认证、社交认证、WebAuthn 技术，并兼容 Django 自定义用户模型。  

**使用方法**：通过 `pip install djoser` 安装，需确保 Python 版本 ≥3.9、Django ≥3.2 及 DRF ≥3.14。安装后根据文档配置即可使用。项目文档可通过 [Read the Docs](https://djoser.readthedocs.io) 查阅。  

**开发相关**：使用 Poetry 管理依赖，运行 `pytest` 进行测试，开发前需安装 `pre-commit` 以确保代码格式和质量。