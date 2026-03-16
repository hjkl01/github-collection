### [iredmail dockerized](https://github.com/iredmail/dockerized)  ![GitHub Repo stars](https://img.shields.io/github/stars/iredmail/dockerized?style=social)

本项目是基于 Docker 的 iRedMail 全功能邮件服务器容器化部署方案。
- **镜像基础**：基于 Ubuntu 22.04，提供 `stable` 稳定版和 `nightly` 每日构建版。
- **核心服务**：集成 Postfix (SMTP)、Dovecot (IMAP/POP3)、mlmmj (邮件列表)、Roundcube (Webmail)、iRedAdmin (管理后台)，以及 ClamAV、SpamAssassin、Fail2ban 等安全组件。
- **配置与持久化**：通过配置文件 `iredmail-docker.conf` 设定域名、密码等参数，支持使用主机目录或 Docker 卷持久化存储邮件箱、数据库、日志及 SSL 证书。
- **网络端口**：开放 HTTP/HTTPS、SMTP、IMAP、POP3 及 Managesieve 等标准邮件协议端口（80/443/25/587/143/993/110/995 等）。
- **注意事项**：当前为 Beta 版本，生产环境稳定性未完全保障，建议服务器内存不低于 4GB，部署前需配置相关 DNS 记录。