
---
title: cookiecutter-pypackage
---

### [audreyr cookiecutter-pypackage](https://github.com/audreyr/cookiecutter-pypackage)  ![GitHub Repo stars](https://img.shields.io/github/stars/audreyr/cookiecutter-pypackage?style=social)

Cookiecutter PyPackage 是一个生产就绪的 Python 包 Cookiecutter 模板，旨在简化 Python 包的开发、测试与发布流程。

核心功能：
1. **自动化发布**：推送标签后自动构建并发布至 PyPI，基于 Trusted Publishers 机制无需配置 API 令牌。
2. **现代化工具链**：集成 uv 包管理、just 任务运行、ruff 代码检查、ty 类型检查、pytest 测试、Typer CLI 框架及自动文档生成。
3. **安全 CI/CD**：基于 GitHub Actions，支持多 Python 版本测试与代码审查，采用 SHA 固定操作与最小权限配置。
4. **快速启动**：支持通过 uvx 一键生成标准项目结构，包含完整的环境配置与工作流程。