
---
title: sqlc
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/sqlc-dev/sqlc?style=social) ](https://github.com/sqlc-dev/sqlc)
### [sqlc-dev sqlc](https://github.com/sqlc-dev/sqlc)

sqlc 是一个 SQL 编译器，其核心功能是根据 SQL 查询生成类型安全的代码。使用方法为：编写 SQL 查询后，运行 sqlc 生成对应代码（包含类型安全接口），再在应用代码中调用生成的接口。主要特性包括：  
- 支持多语言代码生成（Go、Kotlin、Python、TypeScript 等，可通过插件扩展）  
- 提供在线演示环境和文档指导  
- 通过类型安全接口减少 SQL 注入风险，提升代码可靠性