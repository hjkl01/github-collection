
---
title: cobra
---

### [spf13 cobra](https://github.com/spf13/cobra)  ![GitHub Repo stars](https://img.shields.io/github/stars/spf13/cobra?style=social)

Cobra 是一个用于构建强大现代命令行（CLI）应用的 Go 语言库，旨在提供类似 git 和 go 工具的高效界面。

核心功能包括：
- 支持基于子命令的 CLI 架构（如 `app server`）、嵌套子命令及命令别名。
- 提供完全符合 POSIX 标准的标志管理（支持短/长版本，含全局、本地、级联标志）。
- 自动生成帮助文档、Man 页面及 Shell 自动补全（支持 bash, zsh, fish, powershell）。
- 具备智能拼写建议功能。
- 允许自定义帮助、用法及错误处理。
- 可选无缝集成 Viper 配置库。
- 附带 cobra-cli 命令行工具用于快速生成项目脚手架。