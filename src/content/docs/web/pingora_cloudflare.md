
---
title: pingora
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/cloudflare/pingora?style=social) ](https://github.com/cloudflare/pingora)
### [cloudflare pingora](https://github.com/cloudflare/pingora)

**Pingora 核心内容总结**  

**项目功能**  
Pingora 是一个基于 Rust 的框架，用于构建高性能、可靠且可编程的网络系统和代理服务。支持 HTTP/1、HTTP/2、gRPC、WebSocket 代理，提供负载均衡、故障转移、TLS 加密（支持 OpenSSL、BoringSSL、s2n-tls、rustls）等功能，适用于构建负载均衡器、自定义代理逻辑等场景。  

**使用方法**  
- 通过 [快速入门指南](./docs/quick_start.md) 学习如何构建负载均衡器。  
- 参考 [用户指南](./docs/user_guide/index.md) 配置服务器、开发自定义代理逻辑。  
- 查阅 API 文档了解各模块（如 `pingora-core`、`pingora-proxy`）的详细接口。  

**主要特性**  
- 基于异步 Rust，性能高效且内存安全。  
- 支持多种 TLS 实现和自定义负载均衡策略。  
- 提供可观测性工具集成、内存缓存（实验性）、高效定时器等扩展功能。  
- 支持优雅重启、缓存算法（如 Ketama）、流量控制等高级特性。  

**系统要求**  
- 主要支持 Linux 系统，部分功能在 macOS（Unix 环境）可用，Windows 为社区支持。  
- 需 Rust 1.84 及以上版本，部分功能需更高版本（如 `boringssl` 需 Rust 1.80）。  
- 构建依赖 Clang（用于 BoringSSL）和 Perl 5（用于 OpenSSL）。  

**其他**  
- 项目采用 Apache 2.0 许可证，贡献需遵循 [指南](./.github/CONTRIBUTING.md)。  
- 缓存相关功能目前为实验性，API 可能不稳定。