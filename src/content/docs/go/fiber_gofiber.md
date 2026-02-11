
---
title: fiber
---

### [gofiber fiber](https://github.com/gofiber/fiber)  ![GitHub Repo stars](https://img.shields.io/github/stars/gofiber/fiber?style=social)

### 项目核心内容总结

**Fiber** 是一个受 [Express](https://github.com/expressjs/express) 启发、基于 [Fasthttp](https://github.com/valyala/fasthttp) 构建的高性能 Web 框架。它专为 Go 语言设计，目标是提供快速开发体验和极致性能。

---

### 📌 项目功能

- **快速搭建 Web 服务**：通过简单 API 可快速创建 Web 服务，支持路由、中间件、模板引擎、静态文件服务等。
- **兼容性支持**：支持 `net/http` 风格的处理函数，可以与现有 Go 标准库代码无缝集成。
- **内置中间件**：包括日志、CORS、限流、压缩、恢复（Recover）、会话管理、重定向等。
- **高性能优化**：基于 Fasthttp，实现零内存分配（Zero Allocation）和低内存占用，适合高并发场景。
- **模板引擎支持**：支持多种模板引擎，如 Pug、Handlebars、Mustache、Amber 等。
- **WebSocket 支持**：内置 WebSocket 升级功能，可轻松实现实时通信。
- **Server-Sent Events（SSE）**：支持服务器向客户端推送事件。
- **路由命名与分组**：支持路由命名、分组与嵌套，便于管理和维护大型项目结构。

---

### 🛠 使用方法

1. **安装 Go**：需要 Go 1.25 或更高版本。
2. **初始化项目**：
   ```bash
   go mod init github.com/your/repo
   ```
3. **安装 Fiber**：
   ```bash
   go get -u github.com/gofiber/fiber/v3
   ```
4. **快速启动一个服务**：
   ```go
   package main

   import (
       "log"
       "github.com/gofiber/fiber/v3"
   )

   func main() {
       app := fiber.New()
       app.Get("/", func(c fiber.Ctx) error {
           return c.SendString("Hello, World 👋!")
       })
       log.Fatal(app.Listen(":3000"))
   }
   ```

---

### ⚡ 主要特性

- **高性能**：基于 Fasthttp，性能优于多数 Web 框架，适合高并发场景。
- **零内存分配**：优化了上下文对象的使用，减少内存分配，提高性能。
- **简单易用**：API 风格类似 Express，便于 Node.js 开发者快速上手。
- **中间件丰富**：内置和外部中间件众多，满足各种开发需求。
- **支持多种开发模式**：支持 `net/http`、Express 风格、原生 Fiber 风格。
- **文档齐全**：提供详细的 API 文档和示例，便于查阅与学习。

---

### 🧩 支持的开发工具

- **模板引擎**：支持多种模板引擎，如 Pug、Handlebars、Mustache 等。
- **静态文件服务**：通过中间件轻松提供静态资源。
- **WebSocket**：支持 WebSocket 升级，用于实时通信。
- **SSE**：实现服务器向客户端推送数据。
- **限流与安全**：提供限流、CORS、CSRF 防护、认证中间件等。

---

### 🧾 授权协议

Fiber 采用 [MIT License](https://github.com/gofiber/fiber/blob/main/LICENSE) 开源协议，允许自由使用、修改和分发。官方 Logo 由 [Vic Shóstak](https://github.com/koddr) 创作，采用 [Creative Commons](https://creativecommons.org/licenses/by-sa/4.0/) 协议。