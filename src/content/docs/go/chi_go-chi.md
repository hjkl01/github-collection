
---
title: chi
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/go-chi/chi?style=social) ](https://github.com/go-chi/chi)
### [go-chi chi](https://github.com/go-chi/chi)

**项目核心内容总结：**

chi 是一个基于 Go 语言的高性能 HTTP 路由器，支持中间件，适用于构建 RESTful API。其主要功能包括：

1. **高性能路由**  
   使用 radix 树实现高效路由匹配，支持参数提取（如 `/user/:id`）、静态路由、通配符路由等。

2. **中间件支持**  
   提供丰富的中间件（如日志、限流、CORS、JWT 认证等），支持自定义中间件，用于请求处理前后的逻辑（如鉴权、日志记录）。

3. **灵活的路由管理**  
   支持路由分组（通过 `chi.Router` 嵌套）、子路由定义，便于组织大型项目结构。

4. **上下文管理**  
   集成 Go 标准库 `context`，支持在请求处理过程中传递和管理上下文信息（如用户身份、请求ID）。

5. **兼容性与扩展性**  
   兼容标准库 `http`，可与现有 Go 工具链无缝集成；支持额外功能包（如 CORS、请求日志、HTTP 跟踪等）。

**使用方法：**  
- 安装：`go get github.com/go-chi/chi/v5`  
- 基本用法：  
  ```go
  r := chi.NewRouter()
  r.Get("/user/{id}", func(w http.ResponseWriter, r *http.Request) {
      // 处理逻辑
  })
  http.ListenAndServe(":8080", r)
  ```  
- 中间件示例：  
  ```go
  r.Use(middleware.Logger)
  r.Use(middleware.RedirectSlashes)
  ```

**主要特性：**  
- 高性能（基准测试显示低延迟、高并发处理能力）  
- 简洁的 API 设计，易于学习和使用  
- 支持动态路由参数、子路由、中间件链式调用  
- 与 Go 标准库及第三方工具（如 gRPC、GraphQL）兼容  
- 社区维护的扩展包生态（如 cors、docgen、jwtauth 等）