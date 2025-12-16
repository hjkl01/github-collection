
---
title: gobang
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/TaKO8Ki/gobang?style=social) ](https://github.com/TaKO8Ki/gobang)
### [TaKO8Ki gobang](https://github.com/TaKO8Ki/gobang)

**项目核心内容总结：**

**功能**  
gobang 是一个基于文本的用户界面（TUI）数据库管理工具，支持通过键盘操作管理 MySQL、PostgreSQL 和 SQLite 数据库，提供跨平台支持（macOS/Windows/Linux）。

**主要特性**  
- 跨平台兼容性  
- 支持多种数据库类型  
- 仅需键盘操作的直观交互  

**使用方法**  
1. **安装**：支持通过 Homebrew、Scoop、Cargo 等方式安装，或直接下载二进制文件。  
2. **配置**：通过编辑配置文件（路径因系统而异）添加数据库连接信息，配置文件采用 TOML 格式，示例包含数据库类型、用户名、密码、主机地址等参数。  
3. **运行**：安装后直接执行 `gobang` 命令启动工具。  

**配置说明**  
配置文件需定义数据库连接信息，如类型（MySQL/PostgreSQL/SQLite）、用户、密码、主机、端口及数据库路径等。