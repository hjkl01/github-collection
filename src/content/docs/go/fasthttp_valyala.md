
---
title: fasthttp
---

### [valyala fasthttp](https://github.com/valyala/fasthttp)  ![GitHub Repo stars](https://img.shields.io/github/stars/valyala/fasthttp?style=social)

fasthttp 是 Go 语言中极高性能的 HTTP 实现库，提供 HTTP 服务器和客户端功能。相比标准库 net/http，其服务器性能快 6 倍，客户端快 4 倍，且通过对象复用实现零内存分配。该库专为处理高并发、低延迟的极端性能场景设计，常规场景建议使用 net/http。fasthttp 的 API 与 net/http 不兼容，需使用 RequestHandler 函数处理请求，但提供适配工具方便迁移。使用时需特别注意禁止在请求处理返回后持有 RequestCtx 引用以防止数据竞争。社区拥有丰富的第三方路由和框架（如 Fiber）支持。