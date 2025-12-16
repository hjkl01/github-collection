
---
title: graphql-engine
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/hasura/graphql-engine?style=social) ](https://github.com/hasura/graphql-engine)
### [hasura graphql-engine](https://github.com/hasura/graphql-engine)

**核心内容总结：**  
Hasura GraphQL Engine 是一个开源项目，通过提供统一、安全的 API 端点，简化现代应用的数据访问与构建。其核心功能包括：  
1. **多数据库支持**：兼容 PostgreSQL、MongoDB、ClickHouse、MS SQL Server 等，并支持自定义业务逻辑（通过 TypeScript、Python、Go 等语言的 Connector SDK）。  
2. **版本区分**：  
   - **V3**：最新版本，支持多种数据源和自定义逻辑，代码位于 `v3` 文件夹，文档链接为 [v3 文档](https://hasura.io/docs/3.0/)。  
   - **V2**：稳定版本，代码位于 `v2` 文件夹，文档链接为 [V2 文档](https://hasura.io/docs/)。  
3. **使用方法**：  
   - 克隆仓库时可采用浅层克隆（仅获取最新提交）或稀疏检出（仅获取 `v3` 文件夹代码），以减少资源消耗。  
4. **支持与资源**：提供文档、社区支持（Discord）、GitHub 问题跟踪及品牌资产（如 Logo 和“Powered by Hasura”徽章）。  
5. **许可证**：V3 和 V2 核心代码均采用 Apache License 2.0，部分 V2 内容使用 MIT License。  

**主要特性**：开源、多数据库兼容、支持自定义逻辑、分版本管理、提供丰富的社区资源与文档。