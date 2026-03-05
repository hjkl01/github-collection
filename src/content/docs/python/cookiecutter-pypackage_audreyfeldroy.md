
---
title: cookiecutter-pypackage
---

### [audreyfeldroy cookiecutter-pypackage](https://github.com/audreyfeldroy/cookiecutter-pypackage)  ![GitHub Repo stars](https://img.shields.io/github/stars/audreyfeldroy/cookiecutter-pypackage?style=social)

Cookiecutter PyPackage 是一个用于生成生产级 Python 包的 Cookiecutter 模板，提供自动化的 CI/CD 流程与 PyPI 发布功能。项目集成了 uv 包管理器、just 任务运行器、ruff 代码检查、ty 类型检查、pytest 测试、Typer CLI 框架及 Zensical 文档生成工具。CI 流程支持多 Python 版本测试与代码检查，通过 Git 标签即可自动构建并发布到 PyPI（基于可信发布者，无需管理 Token），同时自动部署文档至 GitHub Pages。所有 CI 动作均经过安全加固，采用 SHA 绑定与最小权限策略。