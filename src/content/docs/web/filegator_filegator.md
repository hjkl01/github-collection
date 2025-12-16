
---
title: filegator
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/filegator/filegator?style=social) ](https://github.com/filegator/filegator)
### [filegator filegator](https://github.com/filegator/filegator)

**核心内容总结：**  
FileGator 是一款免费、开源、自托管的多用户文件管理工具，支持本地及多种云存储（如 FTP、S3、Dropbox 等），提供文件上传、下载、编辑、压缩、权限管理等功能。用户可通过拖拽上传、分块传输、多文件操作等提升效率。  

**使用方法：**  
- **Docker 快速部署**：运行 `docker run` 命令启动容器，访问默认地址登录（admin/admin123）。  
- **本地安装**：需 PHP、Node.js 等环境，执行 `composer install` 和 `npm install` 等步骤。  
- **演示环境**：提供在线演示（[demo.filegator.io](https://demo.filegator.io)），支持 guest 账户及权限测试。  

**主要特性：**  
- 支持多种存储适配器（本地、FTP、S3 等）和认证方式（JSON、数据库、WordPress）。  
- 前端基于 Vue.js 和 Bulma 框架，界面友好。  
- 分块上传、暂停/恢复、多文件下载。  
- 无需数据库，代码可扩展性强。  

**部署注意事项：**  
- 部署时需将 `dist` 目录设为网站根目录，避免暴露其他敏感文件。  
- 安全问题需通过邮件联系开发者，而非公开讨论。