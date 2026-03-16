### [datalens-tech datalens](https://github.com/datalens-tech/datalens)  ![GitHub Repo stars](https://img.shields.io/github/stars/datalens-tech/datalens?style=social)

DataLens 是一款现代化的开源商业智能（BI）和数据可视化系统。

1. **核心功能**：支持连接 ClickHouse、PostgreSQL 等数据源，提供数据查询、计算处理及可视化展示（兼容 Highcharts 或 D3.js，支持 Yandex Maps）。
2. **系统架构**：包含前端 UI、后端 Python 服务、统一存储（UnitedStorage）、认证授权（Auth）及元数据管理（MetaManager）。
3. **部署方式**：支持 Docker Compose 及 Kubernetes（Helm Chart）部署，支持配置外部数据库。
4. **权限管理**：内置基于角色的访问控制，包含 Viewer（只读）、Editor（编辑）、Admin（管理）角色。
5. **云服务**：除开源版本外，作为 Yandex Cloud 平台的一部分提供服务。