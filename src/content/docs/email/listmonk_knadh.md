
---
title: listmonk
---

### [knadh listmonk](https://github.com/knadh/listmonk)  ![GitHub Repo stars](https://img.shields.io/github/stars/knadh/listmonk?style=social)

ListMonk 是一个独立、自托管的邮件列表和新闻通讯管理工具，采用 PostgreSQL 作为数据库，具备快速、功能丰富等特点，集成于单一二进制文件中。  

**使用方法**：  
- **Docker**：通过 DockerHub 镜像 `listmonk/listmonk:latest`，下载 `docker-compose.yml` 文件后运行 `docker compose up -d`，访问 `http://localhost:9000`。  
- **二进制**：下载最新版本二进制文件，执行 `./listmonk --new-config` 生成配置文件并编辑，再通过 `./listmonk --install` 初始化 PostgreSQL 数据库，最后运行 `./listmonk` 启动服务。  

**主要特性**：  
- 完全自托管，无需依赖第三方服务；  
- 单一二进制文件部署，简化安装流程；  
- 支持 PostgreSQL 数据库；  
- 提供图形化管理界面（可通过 `http://localhost:9000` 访问）；  
- 开源，采用 AGPLv3 协议授权。