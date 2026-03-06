
---
title: pgsync
---

### [ankane pgsync](https://github.com/ankane/pgsync)  ![GitHub Repo stars](https://img.shields.io/github/stars/ankane/pgsync?style=social)

pgsync 是一个用于在 PostgreSQL 数据库之间同步数据的命令行工具。主要功能如下：

1. **高效同步**：支持表格并行传输，可针对特定表、表组或行进行筛选（含条件过滤、保留或截断操作）。
2. **数据安全**：内置数据脱敏规则，防止敏感信息（如邮箱、电话）离开源服务器，支持匿名化和自定义语句。
3. **灵活处理**：自动处理表架构差异，支持同步模式、跳过序列与触发器，提供外键约束处理选项。
4. **多场景支持**：兼容 Gem、Homebrew 及 Docker 部署，内置针对 Rails、Django 等框架的配置，默认限制目标连接地址以确保安全。