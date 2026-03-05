
---
title: tonic
---

### [hyperium tonic](https://github.com/hyperium/tonic)  ![GitHub Repo stars](https://img.shields.io/github/stars/hyperium/tonic?style=social)

Tonic 是一个基于 Rust 的高性能 gRPC 框架实现，专注于互操作性与灵活性。该库基于 HTTP/2 协议，原生支持 async/await，底层依托 tokio 和 hyper 实现高效异步 I/O。功能涵盖双向流式传输、TLS 加密、负载均衡、自定义元数据、认证及健康检查。项目包含核心库、基于 prost 的代码生成工具、工具类型库以及健康检查和反射模块，旨在作为 Rust 生产系统中 gRPC 客户端与服务器的核心构建块。