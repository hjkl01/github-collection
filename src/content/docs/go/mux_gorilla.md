
---
title: mux
---

### [gorilla mux](https://github.com/gorilla/mux)  ![GitHub Repo stars](https://img.shields.io/github/stars/gorilla/mux?style=social)

gorilla/mux 是一个 Go 语言的 HTTP 请求路由器和分发器，实现了 http.Handler 接口，兼容标准库。

核心功能包括：
1. **请求匹配**：支持基于 URL 路径、前缀、主机、方案、请求头、查询值、HTTP 方法及自定义匹配器进行路由。
2. **动态参数**：URL 路径和查询值支持定义变量，可配合正则表达式匹配。
3. **路由反转**：支持为路由命名，并基于变量构建（反转）URL。
4. **子路由**：支持嵌套路由，方便定义共享条件（如主机、前缀）的路由组，优化匹配性能。
5. **中间件支持**：可在路由上添加中间件，用于处理日志、认证、CORS 等逻辑。
6. **辅助功能**：支持静态文件服务、单页应用 (SPA) 服务、路由遍历、优雅关闭及服务端测试。