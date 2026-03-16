### [golang-migrate migrate](https://github.com/golang-migrate/migrate)  ![GitHub Repo stars](https://img.shields.io/github/stars/golang-migrate/migrate?style=social)

migrate 是一个使用 Go 语言编写的数据库迁移工具，支持作为 CLI 命令行工具使用或作为 Go 库导入项目。它支持从本地文件系统、云存储、版本控制系统等多种来源读取迁移文件，并按正确顺序应用到 PostgreSQL、MySQL、SQLite 等多种数据库中。该工具核心逻辑负责保证迁移可靠性，驱动层保持轻量，支持优雅停止以防止数据损坏，具备线程安全、低内存开销特点，并提供稳定的 API 接口供开发集成。