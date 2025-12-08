
---
title: django-react-boilerplate
---

### [vintasoftware django-react-boilerplate](https://github.com/vintasoftware/django-react-boilerplate)

**项目核心内容总结：**

该项目是一个基于 Django 和 React 的全栈 Web 应用程序模板，适用于开发现代 Web 应用。其主要功能包括：

- **项目结构**：整合了 Django 后端与 React 前端，支持前后端分离开发。
- **部署支持**：提供 Render.com 的部署配置文件 `render.yaml`，便于将项目部署到生产环境。
- **功能特性**：
  - 集成 Sentry 用于错误监控。
  - 支持 SendGrid 发送邮件。
  - 配置了 Celery 用于异步任务处理。
  - 使用 Django-CSP 来增强安全性，防止 XSS 攻击。
  - 包含代码规范工具（如 Ruff 和 ESLint）和 Git 预提交钩子，确保代码质量。
- **开发与部署流程**：
  - 支持本地开发（包括 Docker 和非 Docker 环境）。
  - 提供部署脚本 `render_build.sh`，用于构建前端、后端、运行迁移、收集静态文件等。
- **生产环境配置**：支持通过 Render.com 部署，并提供了环境变量配置说明，如 `SECRET_KEY`、`SENTRY_DSN` 等。
- **其他**：支持通过 GitHub Actions 实现自动化测试，提供详细的开发和贡献指南。

**使用方法**：
- 克隆项目，配置环境变量。
- 使用 `poetry` 安装 Python 依赖，使用 `npm` 或 `yarn` 安装前端依赖。
- 启动开发服务器，进行本地调试。
- 通过 `render.yaml` 配置文件部署到 Render.com，设置相关环境变量。

**主要特性**：
- 完整的前后端开发框架。
- 支持异步任务和邮件发送。
- 集成错误监控和代码质量工具。
- 提供生产部署方案和环境配置指导。