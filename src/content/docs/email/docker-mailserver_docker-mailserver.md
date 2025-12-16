
---
title: docker-mailserver
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/docker-mailserver/docker-mailserver?style=social) ](https://github.com/docker-mailserver/docker-mailserver)
### [docker-mailserver docker-mailserver](https://github.com/docker-mailserver/docker-mailserver)

**项目核心内容总结：**

**功能**  
Docker Mailserver 是一个生产级全栈邮件服务器容器，集成 SMTP、IMAP、LDAP、反垃圾邮件（Rspamd/SpamAssassin）、反病毒（ClamAV）、域名验证（OpenDKIM/OpenDMARC）等功能，支持通过配置文件而非数据库进行管理。

**使用方法**  
通过 Docker 部署，需参考官方文档进行配置（提供基础安装教程、环境变量设置、更新指南等）。支持 LDAP、OAuth2 认证，包含自动化配置脚本（setup.sh）简化部署流程。

**主要特性**  
- 无数据库依赖，仅需配置文件，便于版本控制和升级  
- 集成 Postfix、Dovecot、Amavis、Fail2ban 等核心服务  
- 支持 Let's Encrypt 证书、邮件配额、别名扩展等高级功能  
- 提供中文文档（[FAQ/使用指南/示例](https://docker-mailserver.github.io/docker-mailserver/latest/)）及问题排查指引  

**注意事项**  
- 部署前需阅读对应版本的文档  
- 问题排查优先查阅文档，不直接在 GitHub 提交支持请求