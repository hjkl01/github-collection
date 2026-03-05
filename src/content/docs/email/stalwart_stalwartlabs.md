
---
title: stalwart
---

### [stalwartlabs stalwart](https://github.com/stalwartlabs/stalwart)  ![GitHub Repo stars](https://img.shields.io/github/stars/stalwartlabs/stalwart?style=social)

Stalwart 是一款基于 Rust 开发的开源邮件与协作服务器，主打安全、高性能、高可扩展性。

核心功能包括：
1. **邮件服务**：支持 JMAP、IMAP、POP3、SMTP 全协议，内置反垃圾邮件与反钓鱼机制，支持 DMARC、DKIM、SPF 等认证及传输加密。
2. **协作服务**：提供 CalDAV、CardDAV、WebDAV 支持，涵盖日历、联系人及文件存储，具备细粒度共享与权限控制。
3. **灵活性与存储**：支持 RocksDB、S3、SQL 等多种存储后端及全文搜索，支持多租户、自动配置、Sieve 脚本及配额管理。
4. **安全与运维**：内存安全设计，支持 ACME 自动 TLS 证书，具备集群协调、Kubernetes 支持、高可用及故障恢复能力。
5. **认证与监控**：支持 OIDC、OAuth 2.0、LDAP 认证，提供 Web 管理控制台、OpenTelemetry 日志追踪及 Prometheus 指标监控。

采用 AGPL v3.0 与 Stalwart 企业版双许可。