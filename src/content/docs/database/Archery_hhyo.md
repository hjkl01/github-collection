
---
title: Archery
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/hhyo/Archery?style=social) ](https://github.com/hhyo/Archery)
### [hhyo Archery](https://github.com/hhyo/Archery)

Archery 是一个支持多数据库的 SQL 审核与查询管理平台，主要功能包括 SQL 查询、审核、执行、备份、数据字典管理、慢日志分析、会话管理等。支持的数据库类型涵盖 MySQL、Oracle、MongoDB、ClickHouse 等，不同数据库功能支持程度存在差异（如 MySQL 支持最全面）。  

**核心特性**：  
- 提供可视化界面和代码级操作，集成 SQL 解析、索引优化、执行计划分析等功能；  
- 支持通过 Docker 快速部署或手动安装，提供在线演示环境（账号：archer/archer）；  
- 依赖 Django 框架，集成多种数据库连接器（MySQL、Redis、PostgreSQL 等）及第三方工具（如 goInception、SQLAdvisor、SOAR 等）；  
- 支持 LDAP 认证、数据加密、RDS 管理等企业级功能。  

**使用方法**：  
1. 在线体验：访问 [demo.archerydms.com](https://demo.archerydms.com)；  
2. 安装部署：通过 Docker 或手动安装（详见 GitHub 文档）。