
---
title: flask-restless
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/jfinkels/flask-restless?style=social) ](https://github.com/jfinkels/flask-restless)
### [jfinkels flask-restless](https://github.com/jfinkels/flask-restless)

**项目核心内容总结：**

1. **项目功能**  
   Flask-Restless 是 Flask 的一个扩展，用于自动生成符合 [JSON API](https://jsonapi.org) 规范的 RESTful API 端点，支持基于 [SQLAlchemy](https://sqlalchemy.org) 或 [Flask-SQLAlchemy](https://packages.python.org/Flask-SQLAlchemy) 的数据库模型。

2. **主要特性**  
   - 自动为数据库模型生成标准的 CRUD（创建、读取、更新、删除）接口  
   - 支持数据库搜索和过滤功能  
   - 提供数据序列化与反序列化能力  
   - 兼容 Python 2.6-3.4（不支持 Python 3.2）  
   - 提供示例代码和单元测试  

3. **使用方法**  
   - 安装依赖：通过 `pip install -r requirements/install.txt` 安装 Flask、SQLAlchemy 等库  
   - 配置 API：通过 `manager.py` 中的类为模型创建接口  
   - 运行测试：安装测试依赖后执行 `python setup.py test`  
   - 构建文档：使用 Sphinx 工具生成 HTML 格式文档  

4. **项目状态**  
   当前项目已不再维护，建议使用替代项目 [flask-restless-ng](https://github.com/mrevutskyi/flask-restless-ng)。  

5. **许可证**  
   代码采用 GNU AGPLv3 或 3-clause BSD 双许可证，文档采用 Creative Commons Attribution-ShareAlike 4.0 许可证。