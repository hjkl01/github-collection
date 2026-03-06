
---
title: mox
---

### [mjl- mox](https://github.com/mjl-/mox)  ![GitHub Repo stars](https://img.shields.io/github/stars/mjl-/mox?style=social)

Mox 是一个由 Go 语言编写的现代全功能开源安全邮件服务器，专为低维护成本的自托管邮件服务设计。

- **协议支持**：支持 SMTP（接收、提交、投递）、IMAP4（含扩展）、Webmail 及内置 Web 服务器（反向代理）。
- **安全机制**：支持自动 TLS（ACME/Let's Encrypt）、SPF/DKIM/DMARC 验证、DANE 和 MTA-STS。
- **反垃圾功能**：具备基于用户/域名的信誉跟踪、贝叶斯过滤及类 Greylisting 的智能限流机制。
- **管理运维**：提供 Web 管理界面、账号自动发现、HTTP/JSON API（WebAPI/Webhooks）、Prometheus 指标和结构化日志。
- **部署便捷**：支持源码编译与 Docker 运行，提供快速启动脚本，支持国际化邮箱地址及邮件端口复用。