
---
title: dockerized
---

### [iredmail dockerized](https://github.com/iredmail/dockerized)  ![GitHub Repo stars](https://img.shields.io/github/stars/iredmail/dockerized?style=social)

本项目是基于 Docker 的 iRedMail 全功能邮件服务器部署方案（Beta 版，暂不推荐用于生产环境）。基于 Ubuntu 22.04 镜像，通过环境变量文件配置，快速提供 SMTP、IMAP、POP3 等邮件收发服务。内置集成 Postfix、Dovecot、Roundcube（Web 邮件）、iRedAdmin（管理面板）、Amavisd-new、ClamAV、SpamAssassin（反垃圾/反病毒）、Fail2ban 安全防护及 mlmmj 邮件列表管理功能。支持通过 Docker 卷或主机目录进行数据持久化存储，建议硬件至少配备 4GB 内存。