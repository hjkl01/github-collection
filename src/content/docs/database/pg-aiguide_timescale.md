
---
title: pg-aiguide
---

### [timescale pg-aiguide](https://github.com/timescale/pg-aiguide)  ![GitHub Repo stars](https://img.shields.io/github/stars/timescale/pg-aiguide?style=social)

**pg-aiguide 核心内容总结**  
pg-aiguide 是一个优化 AI 生成 PostgreSQL 代码质量的工具，提供以下功能：  
1. **语义搜索**：支持按 PostgreSQL 版本检索官方文档（如 TimescaleDB 扩展）。  
2. **AI 优化技能库**：内置 PostgreSQL 最佳实践（如索引策略、约束设计、现代特性使用等），提升 AI 生成代码的规范性与性能。  
3. **生态文档支持**：涵盖 TimescaleDB 等扩展的文档，未来将支持 pgvector、PostGIS 等。  

**使用方法**：  
- 作为 **MCP 服务器**：通过 JSON 配置接入 AI 工具（如 VS Code、Cursor 等）。  
- 作为 **Claude Code 插件**：通过命令行安装插件。  

**核心特性**：  
- 修复 AI 生成代码的常见问题（如缺失约束、不熟悉新特性）。  
- 提供更健壮的数据库设计（如自动添加索引、使用 PG17 推荐模式）。  
- 支持多环境一键安装（Cursor、VS Code、Visual Studio 等）。  

**许可证**：Apache 2.0。