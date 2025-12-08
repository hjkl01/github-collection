
---
title: mux
---

### [gorilla mux](https://github.com/gorilla/mux)

**项目功能**：Gorilla Mux 是一个用于 Go 语言的高性能 URL 路由器，支持路径变量、中间件、CORS 请求处理及单元测试。  

**使用方法**：  
1. 创建路由器对象，通过 `HandleFunc` 定义路由路径与处理函数；  
2. 使用 `Methods` 设置 HTTP 方法（如 GET、POST）；  
3. 集成中间件（如认证、日志）通过 `Use` 方法添加；  
4. 启动服务时将路由器作为 `http.ListenAndServe` 的参数。  

**主要特性**：  
- 支持路径参数（如 `/user/{id}`）及正则表达式匹配；  
- 提供 `CORSMethodMiddleware` 自动设置 `Access-Control-Allow-Methods` 响应头；  
- 支持中间件链式调用，可中断请求处理流程；  
- 提供测试工具，通过 `httptest` 模拟请求并验证响应结果；  
- 支持 OPTIONS 方法处理，满足 CORS 预检请求需求。