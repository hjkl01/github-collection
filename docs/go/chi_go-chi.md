### [go-chi chi](https://github.com/go-chi/chi)  ![GitHub Repo stars](https://img.shields.io/github/stars/go-chi/chi?style=social)

chi 是一个轻量、快速且符合 Go 惯用法的 HTTP 路由库，专为构建可维护的大型 REST API 服务而设计。

核心功能特性：
* **轻量无依赖**：核心代码约 1000 行，仅依赖 Go 标准库，完全兼容 net/http。
* **模块化设计**：支持中间件链、路由组（Group）和子路由（Route）挂载，便于系统分解。
* **上下文控制**：基于 Go context 包，支持请求范围内的值传递、取消信号和超时处理。
* **丰富中间件**：提供可选的 middleware 包，包含日志、恢复、超时、压缩等常用功能。
* **强大路由**：采用 Radix 树结构，支持 URL 命名参数、通配符及正则匹配。
* **工具支持**：支持 go.mod，可通过 docgen 自动生成路由文档。
* **生产验证**：性能优越，已在多家大型企业生产环境广泛使用。