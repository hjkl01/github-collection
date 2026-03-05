
---
title: mox
---

### [mjl- mox](https://github.com/mjl-/mox)  ![GitHub Repo stars](https://img.shields.io/github/stars/mjl-/mox?style=social)

Mox 是一款现代、全功能的开源安全邮件服务器，旨在提供低维护成本的自托管电子邮件服务。

核心功能包括：
- 邮件协议：支持 SMTP（接收、提交、投递）、IMAP4 及 Webmail。
- 安全验证：支持自动 TLS（ACME/Let's Encrypt）、SPF/DKIM/DMARC、DANE 及 MTA-STS。
- 反垃圾机制：用户级贝叶斯过滤、信誉追踪、可疑发件人限速及拒绝邮件暂存。
- 管理集成：Web 管理后台、账号自动发现、内置 Web 服务器、HTTP/JSON API 及 Webhooks。
- 运维监控：Prometheus 指标、结构化日志、配置生成与验证工具。
- 基础架构：Go 语言编写，支持 Unix 系统与 Docker，严格遵循 RFC 标准，MIT 开源协议。