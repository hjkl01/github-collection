
---
title: sandman2
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/jeffknupp/sandman2?style=social) ](https://github.com/jeffknupp/sandman2)
### [jeffknupp sandman2](https://github.com/jeffknupp/sandman2)

**项目核心内容总结：**  
sandman2 是一个可自动生成 RESTful API 的工具，无需手动编写代码。它通过连接数据库（支持 MySQL、PostgreSQL、SQLite 等），自动解析数据库结构并生成对应的 API 接口，支持 HTTP 请求访问数据。  

**使用方法：**  
1. 通过 `pip install sandman2` 安装；  
2. 使用命令行工具 `sandman2ctl`，输入数据库连接字符串（如 `sqlite+pysqlite:///database_file_name` 或 `postgresql+psycopg2://用户名:密码@主机/数据库名`）启动服务。  

**主要特性：**  
- 无需编写代码，自动生成 RESTful API 和超媒体支持；  
- 支持多种数据库（包括 MySQL、PostgreSQL、SQLite 等）；  
- 提供现代化的管理界面（Admin Interface），可浏览和操作数据库；  
- 可集成到应用中自定义配置，或通过 Docker 部署（需设置数据库连接参数）。  

**其他说明：**  
sandman2 替代了原版 sandman，功能更完善，且原版已停更。