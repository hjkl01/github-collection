
---
title: harlequin
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/tconbeer/harlequin?style=social) ](https://github.com/tconbeer/harlequin)
### [tconbeer harlequin](https://github.com/tconbeer/harlequin)

### 项目核心内容总结

**Harlequin** 是一款用于终端的 SQL IDE，支持连接多种数据库，并提供交互式查询、数据编辑和执行等功能。

**功能**：
- 支持多种数据库适配器（如 DuckDB、SQLite、PostgreSQL、MySQL 等）。
- 提供丰富的配置选项，如主题、快捷键、文件管理等。
- 可通过命令行运行，支持连接字符串和参数配置。
- 支持 Django 集成，使用 Django 的数据库配置启动 Harlequin。

**使用方法**：
- 安装方式：推荐使用 `uv` 工具安装，也可以通过 `pip`、`pipx`、`poetry` 或 Homebrew 安装。
- 安装数据库适配器：如需使用 Postgres、MySQL 等数据库，需额外安装对应的适配器。
- 启动方式：通过命令行运行 `harlequin`，可指定数据库连接字符串和适配器类型。
- 使用帮助：运行 `harlequin --help` 查看所有可用选项。

**主要特性**：
- 默认使用 DuckDB 适配器，支持内存数据库和文件数据库。
- 支持 SQLite 适配器，可连接内存数据库或文件数据库。
- 提供完整的配置文件功能，支持自定义主题、快捷键等。
- 提供详细的文档和社区支持，可通过 [harlequin.sh](https://harlequin.sh/docs) 获取更多使用信息。

**其他信息**：
- 可通过 `uv tool install` 安装 Harlequin 及其适配器。
- 支持跨平台运行（Linux、MacOS、Windows）。
- 可通过 GitHub 讨论、问题跟踪和赞助支持项目。