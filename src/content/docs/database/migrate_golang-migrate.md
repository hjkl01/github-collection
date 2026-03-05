
---
title: migrate
---

### [golang-migrate migrate](https://github.com/golang-migrate/migrate)  ![GitHub Repo stars](https://img.shields.io/github/stars/golang-migrate/migrate?style=social)

一个用 Go 编写的数据库迁移工具，支持 CLI 和库两种使用方式。核心逻辑负责流程管理并确保健壮性，驱动保持轻量。它从本地或远程来源读取迁移脚本，按顺序应用到支持的多种数据库（如 PostgreSQL、MySQL、SQLite 等）。工具支持优雅中断、线程安全及低内存开销，迁移脚本采用 up 和 down 分离的文件格式。