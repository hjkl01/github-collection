
---
title: datalens
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/datalens-tech/datalens?style=social) ](https://github.com/datalens-tech/datalens)
### [datalens-tech datalens](https://github.com/datalens-tech/datalens)

DataLens 是一个开源的商业智能（BI）和数据可视化平台，支持连接 ClickHouse、PostgreSQL 等数据库，提供数据处理、用户界面、权限管理和元数据管理功能。核心特性包括：  
1. **功能**：支持数据可视化、多数据源连接（如 ClickHouse、PostgreSQL）、用户角色权限控制（查看者、编辑者、管理员）、工作簿导出、Temporal 工作流服务。  
2. **使用方法**：通过 Docker 部署，使用 `init.sh` 脚本生成配置文件，支持自定义域名/IP、外部 PostgreSQL 数据库、禁用认证或资源受限环境的简化部署。  
3. **部署方式**：提供 Docker Compose 模板和 Kubernetes Helm Chart，支持云平台（如 Yandex Cloud）集成，可扩展至高可用架构。  
4. **权限管理**：默认启用认证，支持角色分级（查看、编辑、管理），管理员可通过控制面板分配权限。  
5. **资源需求**：最低需 4GB 内存和 2 核 CPU，各组件内存需求从 512MB 至 1GB 不等。