
---
title: atlas
---

### [ariga atlas](https://github.com/ariga/atlas)  ![GitHub Repo stars](https://img.shields.io/github/stars/ariga/atlas?style=social)

**项目功能：**  
Atlas 是一个语言无关的数据库架构管理工具，支持通过现代 DevOps 原理进行数据库迁移。它提供两种工作流：

- **声明式迁移**：通过比较当前数据库状态与目标状态（用 HCL、SQL 或 ORM 描述），生成并执行迁移计划。
- **版本化迁移**：用户描述目标数据库结构，Atlas 负责自动规划、校验和应用迁移。

**使用方法：**  
- 安装方式包括 macOS/Linux 下的脚本安装、Homebrew、Docker、NPM。
- 使用命令如 `schema inspect`、`schema diff`、`schema apply`、`migrate diff` 和 `migrate apply` 来管理数据库结构和迁移。
- 支持多种数据库类型，包括 MySQL、PostgreSQL、SQLite、SQL Server 等。

**主要特性：**  
- 支持多种数据库格式（HCL、SQL、ORM）。
- 提供数据库架构的可视化（ERD、Mermaid 语法）。
- 支持版本控制、迁移校验、多租户架构。
- 与云服务集成，可从 AWS/GCP 密钥管理服务读取数据库凭证。
- 与 Terraform 集成，支持数据库变更作为部署工作流的一部分。