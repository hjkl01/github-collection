
---
title: fasthttp
---

### [valyala fasthttp](https://github.com/valyala/fasthttp)  ![GitHub Repo stars](https://img.shields.io/github/stars/valyala/fasthttp?style=social)

fasthttp 是 Go 语言编写的高性能 HTTP 实现库，提供 HTTP 服务器和客户端支持。相比标准库 net/http，其服务器性能最高快 6 倍，客户端性能最高快 4 倍，且采用零内存分配设计。该库专为需要处理每秒数千次请求且要求低延迟的高性能场景设计。API 与 net/http 不兼容，需手动迁移，且不自带路由功能，需配合第三方路由或框架使用。支持通过第三方扩展实现 HTTP/2 和 WebSocket 功能，并提供详细的迁移指南及性能优化建议。