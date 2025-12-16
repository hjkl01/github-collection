
---
title: rainfrog
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/achristmascarl/rainfrog?style=social) ](https://github.com/achristmascarl/rainfrog)
### [achristmascarl rainfrog](https://github.com/achristmascarl/rainfrog)

**项目核心内容总结：**  
rainfrog 是一个基于终端的数据库管理工具，支持 PostgreSQL、MySQL 等数据库的连接与操作。其主要功能包括：  
1. **数据库操作**：执行 SQL 查询、查看表结构、导出查询结果为 CSV 文件。  
2. **交互特性**：提供 Vim 风格的键盘快捷键、可滚动表格、语法高亮、异步查询（支持取消操作）。  
3. **便捷功能**：保存常用查询为收藏夹，支持从收藏夹快速调用或编辑；导出结果至系统下载目录。  
4. **使用方法**：通过命令行启动，配置数据库连接参数（如 `DATABASE_URL`），支持环境变量自定义导出路径或收藏夹存储位置。  

**主要特性**：  
- 支持多数据库连接，兼容常见 SQL 语法。  
- 终端界面友好，支持鼠标操作（如滚动、切换焦点）。  
- 查询结果可导出为 CSV，适用于数据分析。  
- 收藏夹功能便于管理高频查询，提升工作效率。  
- 当前为 Beta 版本，部分功能（如几何类型支持）尚在完善中。