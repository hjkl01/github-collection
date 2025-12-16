
---
title: flask-graphql
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/graphql-python/flask-graphql?style=social) ](https://github.com/graphql-python/flask-graphql)
### [graphql-python flask-graphql](https://github.com/graphql-python/flask-graphql)

**Flask-GraphQL 核心内容总结：**

**项目功能**  
为 Flask 应用提供 GraphQL 接口支持，集成 GraphiQL 调试工具，支持批量查询（用于 Apollo-Client 等场景）。

**使用方法**  
1. 导入 `GraphQLView`，通过 `add_url_rule` 添加 `/graphql` 路由，绑定 `schema` 对象。  
2. 可选添加 `/graphql/batch` 路由以支持批量查询。  
3. 示例代码需提供 `schema`（可使用 Graphene 的 `graphql_schema` 或 `graphql-core` 的 `GraphQLSchema`）。

**主要特性**  
- 支持自定义 `context`、`root_value`、`middleware` 等参数。  
- 提供 GraphiQL 界面（默认启用），支持自定义版本、标题、初始查询等。  
- 支持动态 `root_value`（通过继承 `GraphQLView` 并重写 `get_root_value` 方法）。  
- 特别说明：若使用 Graphene v3，需通过 `graphql_schema` 属性传递 schema。  

**注意事项**  
- 批量查询需单独配置 `/graphql/batch` 路由。  
- GraphiQL 的默认版本为 "1.0.3"，可通过参数修改。