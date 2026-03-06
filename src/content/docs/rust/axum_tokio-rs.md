
---
title: axum
---

### [tokio-rs axum](https://github.com/tokio-rs/axum)  ![GitHub Repo stars](https://img.shields.io/github/stars/tokio-rs/axum?style=social)

Axum 是一个注重易用性和模块化的 Rust HTTP 路由及请求处理库。它提供无需宏的 API 进行请求路由，支持使用提取器（extractors）声明式解析请求，拥有简单可预测的错误处理模型及简洁的响应生成方式。Axum 基于 `tower` 和 `tower-http` 生态系统构建，不维护独立的中间件系统，从而免费利用超时、追踪、压缩、授权等能力，并能与 `hyper` 或 `tonic` 共享中间件。该项目基于 `hyper` 构建，性能相当，且代码 100% 安全。