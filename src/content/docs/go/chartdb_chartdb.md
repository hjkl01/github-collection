
---
title: chartdb
---

### [chartdb chartdb](https://github.com/chartdb/chartdb)

**ChartDB核心内容总结：**

**项目功能**  
ChartDB是一款开源的在线数据库结构图编辑工具，支持通过“智能查询”快速导入数据库模式，生成可视化图表。支持AI生成目标数据库的DDL脚本（如MySQL转PostgreSQL），并提供交互式编辑和SQL脚本导出功能，无需安装或数据库密码。

**使用方法**  
1. **在线使用**：访问[ChartDB.io](https://chartdb.io)运行预置查询，导入JSON数据生成图表。  
2. **本地部署**：通过`npm install && npm run dev`启动，或使用Docker命令部署（需配置OpenAI API密钥或自定义推理服务）。  
3. **AI功能**：部署时需配置OpenAI API密钥或自定义模型端点。

**主要特性**  
- 支持PostgreSQL、MySQL、SQL Server、SQLite等10+数据库（含Supabase、Cloudflare D1等扩展支持）。  
- 无安装、无数据库密码要求，AGPL 3.0开源协议。  
- AI驱动的DDL脚本生成与跨数据库迁移支持。  
- 提供隐私保护的Fathom Analytics分析功能（可禁用）。  

**许可证**  
采用[GNU Affero General Public License v3.0](LICENSE)开源协议。