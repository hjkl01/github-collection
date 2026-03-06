
---
title: cookiecutter-pypackage
---

### [audreyr cookiecutter-pypackage](https://github.com/audreyr/cookiecutter-pypackage)  ![GitHub Repo stars](https://img.shields.io/github/stars/audreyr/cookiecutter-pypackage?style=social)

这是一个用于生成 Python 包的 Cookiecutter 模板，提供生产级别的 CI/CD 流程和自动化的 PyPI 发布功能。项目集成了 uv 包管理器、just 任务 runner、ruff、ty、pytest、Typer 和 Zensical 等现代工具链，支持代码格式化、类型检查、多版本测试及文档自动生成。CI/CD 基于 GitHub Actions 实现，支持推送标签即发布（无需 Token）、CI 检查及文档部署，所有 Actions 经过安全加固，采用 SHA 锁定并遵循最小权限原则。