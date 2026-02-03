
---
title: sqlit
---

### [Maxteabag sqlit](https://github.com/Maxteabag/sqlit)  ![GitHub Repo stars](https://img.shields.io/github/stars/Maxteabag/sqlit?style=social)

**项目核心内容总结：**

**功能**  
sqlit 是一个基于终端的 SQL 数据库管理工具，支持连接和查询多种数据库（如 PostgreSQL、MySQL、SQL Server、SQLite 等），提供类似 lazygit 的简洁界面，无需复杂配置即可快速操作。

**使用方法**  
- **安装**：通过 `pipx install sqlit-tui`、`pip` 或系统包管理器（如 Arch Linux、Nix）安装。  
- **连接数据库**：运行 `sqlit`，通过 UI 选择或新建连接（支持 Docker 自动发现、SSH 隧道）。  
- **查询操作**：支持 CLI 模式执行查询、导入导出数据、取消运行中的查询。  
- **测试**：使用 `sqlit --mock` 模拟数据库环境测试功能。

**主要特性**  
1. **多数据库支持**：兼容主流数据库及云服务（如 Snowflake、Athena、Cloudflare D1）。  
2. **无配置连接**：首次运行时自动提示安装缺失的 Python 驱动。  
3. **安全存储**：密码通过操作系统密钥链（如 macOS Keychain、Windows Credential Locker）加密存储。  
4. **高效交互**：Vim 风格快捷键、查询历史记录、结果过滤、主题切换（暗色/亮色）。  
5. **云与容器集成**：支持 Docker 容器自动发现、SSH 隧道连接远程数据库。  
6. **轻量化设计**：专注于快速查询操作，避免冗余功能，适合日常数据库管理需求。