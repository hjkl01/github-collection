### [Suor django-cacheops](https://github.com/Suor/django-cacheops)  ![GitHub Repo stars](https://img.shields.io/github/stars/Suor/django-cacheops?style=social)

django-cacheops 是一款专为 Django ORM 设计的高性能缓存应用。

核心功能：
1. **查询集缓存**：支持自动或手动缓存数据库查询，后端基于 Redis 或文件系统。
2. **事件驱动失效**：监听模型变更信号（保存、删除等），自动且精准地使相关缓存失效，无需手动清理。
3. **全场景缓存**：提供装饰器用于缓存函数、视图及模板片段（支持 Django 和 Jinja2）。
4. **事务与性能**：透明支持事务处理，具备防狗堆机制，提供数据库查询优化技巧。
5. **灵活配置**：可针对不同模型和查询操作定制缓存策略、超时时间及失效规则。
6. **辅助工具**：内置管理命令用于缓存手动失效、清理及统计监控。