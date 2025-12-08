
---
title: pingvin-share
---

### [stonith404 pingvin-share](https://github.com/stonith404/pingvin-share)

**项目核心内容总结：**

**功能**  
Pingvin Share 是一款自托管文件共享平台，提供链接分享、无限文件大小（受限于磁盘空间）、设置分享过期时间、密码保护、邮件发送、反向分享、OIDC/LDAP 认证、ClamAV 安全扫描、支持本地存储和 S3 文件存储等特性。

**使用方法**  
推荐通过 Docker 安装：下载 `docker-compose.yml` 文件后运行 `docker compose up -d`，通过 `http://localhost:3000` 访问。

**主要特性**  
- 支持大文件传输  
- 多种安全限制（密码、访问次数、过期时间）  
- 集成 OIDC/LDAP 认证  
- 支持多文件存储方案（本地/S3）  
- 提供演示站点和文档（[链接](https://stonith404.github.io/pingvin-share)）  

**项目状态**  
作者已将项目归档，专注于其他项目，但欢迎社区分叉维护。