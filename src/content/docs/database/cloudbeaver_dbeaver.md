
---
title: cloudbeaver
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/dbeaver/cloudbeaver?style=social) ](https://github.com/dbeaver/cloudbeaver)
### [dbeaver cloudbeaver](https://github.com/dbeaver/cloudbeaver)

**核心内容总结**  
CloudBeaver 是一款开源的云数据库管理工具，提供基于 Web 的数据库操作界面，支持多种数据库类型（如 PostgreSQL、SQL Server、ClickHouse 等）。项目使用 Java 开发，前端基于 TypeScript 和 React，遵循 Apache 2.0 许可证。  

**使用方法**  
- 通过 Docker 部署，官方镜像地址为 [https://hub.docker.com/r/dbeaver/cloudbeaver](https://hub.docker.com/r/dbeaver/cloudbeaver)；  
- 可访问演示服务器 [https://demo.cloudbeaver.io](https://demo.cloudbeaver.io) 查看功能。  

**主要特性**  
1. **功能全面**：支持数据库连接管理、SQL 编辑、数据浏览与编辑、GIS 数据可视化、数据迁移等；  
2. **安全性增强**：修复关键漏洞（如 CVE-2025-61927），新增 SQL 执行确认提示；  
3. **交互优化**：SQL 编辑器支持临时表分析、自动补全排序；数据编辑器提供过滤/排序后查询回放、列宽自定义等功能；  
4. **兼容性扩展**：新增 ClickHouse 查询取消功能，改进 DuckDB、PostgreSQL 等数据库驱动支持；  
5. **易用性改进**：权限配置简化、LDAP 登录支持大小写不敏感、多语言键盘快捷键提示等。