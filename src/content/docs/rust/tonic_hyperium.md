
---
title: tonic
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/hyperium/tonic?style=social) ](https://github.com/hyperium/tonic)
### [hyperium tonic](https://github.com/hyperium/tonic)

**项目核心内容总结：**  
`tonic` 是 Rust 实现的高性能 gRPC 框架，基于 HTTP/2 协议，支持异步编程模型（async/await），适用于构建生产级系统。  

**功能与特性：**  
- 支持双向流、TLS（基于 `rustls`）、负载均衡、自定义元数据、认证及健康检查。  
- 依赖 `hyper`（HTTP/2 实现）和 `tokio`（异步运行时），代码生成由 `prost` 支持。  
- 提供通用 gRPC 实现，兼容多种 HTTP/2 和编码方式。  

**使用方法：**  
- 通过示例教程（如 `helloworld` 和 `routeguide`）快速入门。  
- 示例代码位于 `examples` 目录，复杂场景可参考 `interop` 测试用例。  
- 需安装 `protoc` 编译器，Rust 版本需 ≥1.75。  

**注意事项：**  
- `master` 分支有重大变更，建议使用 `0.14.x` 分支获取稳定版本。