
---
title: databasus
---

### [databasus databasus](https://github.com/databasus/databasus)  ![GitHub Repo stars](https://img.shields.io/github/stars/databasus/databasus?style=social)

**项目核心内容总结：**

**项目功能**  
Databasus 是一款开源、自托管的数据库备份工具，支持 PostgreSQL、MySQL、MariaDB 和 MongoDB 的备份。提供定时备份、多存储目标（本地/云存储）、通知系统（Slack/Telegram 等）、企业级加密及团队协作功能（权限管理、审计日志）。支持云数据库（AWS RDS 等）和自托管数据库。

**主要特性**  
- 支持多种数据库版本（PostgreSQL 12-18、MySQL 5.7/8/9、MariaDB 10/11、MongoDB 4-8）  
- 灵活备份计划（小时/日/周/月/自定义 cron）  
- 多存储选项（本地、S3、Google Drive 等）  
- 通知系统（邮件、Telegram、Slack 等）  
- 企业级安全（数据加密、权限控制）  
- 支持团队协作（多用户、审计日志）  
- 界面友好，操作简单  

**使用方法**  
1. 安装方式：通过 Docker 命令、Docker Compose 或 Kubernetes Helm 部署。  
2. 配置步骤：访问 `http://localhost:4005`，添加数据库连接信息，设置备份计划和存储目标，可选配置通知方式。  
3. 管理功能：支持密码重置（通过 Docker 命令）、数据迁移（从旧版 Postgresus 迁移）。  

**其他信息**  
- 许可证：Apache 2.0  
- 项目由 Postgresus 更名而来（因商标问题及功能扩展需求），兼容旧版数据迁移。  
- 开发过程使用 AI 辅助代码优化，但所有代码需人工审核并通过测试验证。