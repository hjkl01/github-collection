
---
title: stalwart
---

### [stalwartlabs stalwart](https://github.com/stalwartlabs/stalwart)  ![GitHub Repo stars](https://img.shields.io/github/stars/stalwartlabs/stalwart?style=social)

Stalwart 是一款基于 Rust 编写的开源邮件与协作服务器，设计目标是安全、快速、健壮且可扩展。核心功能如下：

- **邮件服务**：完整支持 JMAP、IMAP4、POP3、SMTP 协议，内置 DMARC、DKIM、SPF、ARC 认证机制及完善的反垃圾、反钓鱼过滤功能。
- **协作功能**：支持日历（CalDAV）、联系人（CardDAV）、文件存储（WebDAV）及共享管理，兼容 JMAP 标准扩展。
- **存储与搜索**：支持多种存储后端（RocksDB、SQL、S3 等）及全文搜索引擎，具备多租户隔离、自动配置和配额管理。
- **安全与认证**：提供 TLS 自动证书、数据加密（S/MIME、OpenPGP）、多种认证方式（OIDC、OAuth 2.0、LDAP）及双重验证。
- **运维与扩展**：支持 Kubernetes 部署、集群协调、高可用架构，提供 OpenTelemetry 可观测性及 Web 管理后台。