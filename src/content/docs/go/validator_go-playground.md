
---
title: validator
---

### [go-playground validator](https://github.com/go-playground/validator)  ![GitHub Repo stars](https://img.shields.io/github/stars/go-playground/validator?style=social)

这是一个 Go 语言的结构体验证库，通过标签对结构体和字段进行值验证。其核心功能包括支持跨字段和跨结构体验证，可深入验证切片、数组、映射及接口类型的底层数据，并支持自定义字段类型和别名验证标签。项目提供可定制的国际化错误消息及自定义字段名提取，同时也是 Gin Web 框架的默认验证器。内置丰富的预定义验证标签，涵盖网络地址（如 IP、URL）、字符串、数据格式（如 UUID、Email）、比较操作、文件系统检查及条件逻辑等。该库经过性能优化，支持高并发验证，采用 MIT 协议开源。