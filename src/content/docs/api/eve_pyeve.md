
---
title: eve
---

### [pyeve eve](https://github.com/pyeve/eve)

**项目核心内容总结：**

**项目功能**  
Eve 是一个基于 Python 的开源 REST API 框架，专注于简化 RESTful Web 服务的构建与部署。支持原生 MongoDB 数据库，可通过社区扩展实现 SQL 数据库兼容。  

**使用方法**  
通过简单代码即可启动 API：  
```python  
from eve import Eve  
app = Eve()  
app.run()  
```  
仅需数据库、配置文件（默认为 `settings.py`）和启动脚本即可部署服务。  

**主要特性**  
- **核心功能**：支持 RESTful 设计、CRUD 操作、自定义资源端点、数据过滤/排序/分页、HATEOAS 链接、JSON/XML 输出。  
- **数据管理**：数据验证、批量插入、并发控制、默认值设置、数据库预定义过滤、字段投影。  
- **扩展性**：支持 API 版本管理、文档版本控制、文件存储、GeoJSON、内部资源嵌套序列化。  
- **安全与控制**：认证机制、CORS 跨域支持、JSONP、读写权限控制、速率限制、自定义 ID 字段。  
- **开发辅助**：事件钩子、增强日志记录、操作日志、MongoDB 聚合框架集成、Flask 框架驱动。