
---
title: mailpit
---

### [axllent mailpit](https://github.com/axllent/mailpit)  ![GitHub Repo stars](https://img.shields.io/github/stars/axllent/mailpit?style=social)

Mailpit 是一款面向开发者的轻量级、零依赖的多平台电子邮件测试工具及 API。它作为 SMTP 服务器运行，提供 Web 界面查看捕获邮件，并支持 REST API 进行自动化集成测试。

主要功能包括：
- **邮件服务**：支持 SMTP（含 STARTTLS/SSL/TLS、认证）及可选 POP3 服务器。
- **界面展示**：提供 Web UI 支持邮件搜索、HTML/源码查看、附件预览（含缩略图）、HTTPS 及认证。
- **通知集成**：支持 REST API、WebSocket 实时推送、浏览器通知及 Webhook。
- **质量检测**：内置 HTML 兼容性检查、链接检查、垃圾邮件检测（SpamAssassin）及 HTML 截图。
- **高级管理**：支持邮件标签、SMTP 中继与转发、高吞吐存储自动清理、混沌工程（模拟 SMTP 错误）。
- **部署方式**：支持单二进制文件或 Docker 部署。