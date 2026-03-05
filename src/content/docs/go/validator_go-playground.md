
---
title: validator
---

### [go-playground validator](https://github.com/go-playground/validator)  ![GitHub Repo stars](https://img.shields.io/github/stars/go-playground/validator?style=social)

go-playground/validator 是一个 Go 语言的结构体和字段验证库，基于标签机制实现值验证。核心功能涵盖：
1. 支持跨字段与跨结构验证。
2. 支持切片、数组和映射的多层级遍历验证。
3. 处理接口类型及自定义字段类型（如 SQL Valuer）。
4. 提供丰富的内置验证标签（涵盖网络、字符串、格式、哈希、UUID 等）。
5. 支持验证标签别名、自定义字段名提取及国际化错误消息。
6. 作为 Gin 框架的默认验证器。
7. 采用标准错误类型返回机制优化错误处理流程。