
---
title: mail-server
---

### [stalwartlabs mail-server](https://github.com/stalwartlabs/mail-server)  ![GitHub Repo stars](https://img.shields.io/github/stars/stalwartlabs/mail-server?style=social)

Stalwart 是一款基于 Rust 编写的开源邮件与协作服务器，具备安全、快速、鲁棒及可扩展的特性。它完整支持 IMAP、JMAP、SMTP、POP3、CalDAV、CardDAV 和 WebDAV 等通信协议。核心功能包括：邮件收发与管理（内置反垃圾邮件、钓鱼防护及 DMARC/DKIM/SPF 验证）、协作服务（日历排程、联系人管理、文件存储）、灵活的存储后端支持（如 PostgreSQL、RocksDB、S3 等）及多语言全文搜索。此外，项目提供完善的认证授权体系（支持 OIDC、LDAP、2FA 等）、Web 管理后台、可观测性监控（Prometheus、OpenTelemetry）以及高可用集群部署能力，适用于从个人使用到企业级大规模部署的邮件通信场景。