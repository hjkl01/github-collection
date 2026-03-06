
---
title: gitleaks
---

### [gitleaks gitleaks](https://github.com/gitleaks/gitleaks)  ![GitHub Repo stars](https://img.shields.io/github/stars/gitleaks/gitleaks?style=social)

Gitleaks 是一个用于检测 Git 仓库、文件和标准输入中敏感信息（如密码、API 密钥、令牌）的静态安全扫描工具。它支持多种部署方式（Homebrew、Docker 等），具备 Git 历史扫描、目录文件扫描及流式输入扫描三种模式。工具支持自定义检测规则（正则、熵值、关键词）、基线忽略、自动解码及压缩包内文件扫描功能。同时提供 GitHub Action 和 Pre-commit 钩子集成，支持多种报告格式（JSON、CSV 等），用于防止敏感数据泄露。