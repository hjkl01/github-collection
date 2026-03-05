
---
title: axum
---

### [tokio-rs axum](https://github.com/tokio-rs/axum)  ![GitHub Repo stars](https://img.shields.io/github/stars/tokio-rs/axum?style=social)

Axum 是一个基于 Rust 的 HTTP 路由和请求处理库，专注于易用性与模块性。它提供无宏路由 API，支持通过提取器声明式解析请求，具备简单可预测的错误处理模型，并能以最小样板代码生成响应。Axum 不内置中间件系统，而是兼容 tower 生态系统，从而免费获得超时、追踪、压缩、认证等功能，并支持与 hyper 和 tonic 应用共享中间件。作为 hyper 的轻量级封装，Axum 性能开销极低，且确保 100% 安全 Rust 实现。