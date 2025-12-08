
---
title: usql
---

### [xo usql](https://github.com/xo/usql)

**usql 核心内容总结：**

**项目功能：**  
usql 是一个跨平台的命令行工具，支持 SQLite3、PostgreSQL、MySQL 等多种数据库，提供数据库连接、查询执行、数据迁移、图表展示等功能。

**使用方法：**  
- 通过 URL 格式连接数据库（如 `pg://user:pass@host:port/dbname`）。  
- 使用反斜杠命令（如 `\connect`、`\copy`、`\chart`）进行数据库操作和数据传输。  
- 支持 `.usqlpass` 文件存储密码，`.usqlrc` 配置文件自定义启动设置。

**主要特性：**  
1. **多数据库支持**：兼容 SQLite3、PostgreSQL、MySQL 等主流数据库。  
2. **语法高亮与终端图形**：支持代码语法高亮，可在终端内直接显示图表（需兼容终端如 WezTerm、iTerm2、kitty）。  
3. **密码与配置管理**：通过 `.usqlpass` 安全存储密码，`.usqlrc` 自定义提示信息、主题等。  
4. **数据操作**：提供 `\copy` 等命令实现数据库间数据复制，支持 SQL 脚本执行。  
5. **跨平台**：支持 macOS、Linux、Windows，可通过 Homebrew 或源码安装。