
---
title: pgsync
---

### [ankane pgsync](https://github.com/ankane/pgsync)  ![GitHub Repo stars](https://img.shields.io/github/stars/ankane/pgsync?style=social)

pgsync 是一个用于在两个 PostgreSQL 数据库之间同步数据的命令行工具。

核心功能：
- **高性能**：支持表数据并行传输。
- **高安全**：内置数据脱敏规则，防止敏感数据离开源服务器。
- **高灵活**：处理架构差异，支持同步架构或仅同步数据。
- **精控制**：支持同步特定表、行、表组及相关记录，可保留或清空目标数据。
- **易配置**：通过 `.pgsync.yml` 管理排除项、分组、数据规则及连接安全。
- **广兼容**：支持外键约束处理、触发器禁用、序列跳过及追加表批量同步。
- **多场景**：默认限制本地目标以防误操作，支持 Gem、Homebrew 和 Docker 安装，适配常见框架。