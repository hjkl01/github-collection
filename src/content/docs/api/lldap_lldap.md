
---
title: lldap
---

### [lldap lldap](https://github.com/lldap/lldap)  ![GitHub Repo stars](https://img.shields.io/github/stars/lldap/lldap?style=social)

lldap 是一个轻量级的 LDAP 认证服务器，提供简化的 LDAP 接口用于身份认证。它具备友好的 Web 管理界面，支持用户、群组创建、密码重置及自定义属性配置，数据默认存储于 SQLite，亦支持 MySQL/MariaDB 或 PostgreSQL 后端。该项目专为自托管服务（如 Nextcloud、Airsonic）提供 LDAP 认证源，支持 Docker、Kubernetes 等部署方式，并可与其他认证组件协同工作。虽非全功能 LDAP 服务器（如 OpenLDAP），不支持直接密码哈希验证等高级特性，但能满足多数 LDAP 客户端的认证需求。