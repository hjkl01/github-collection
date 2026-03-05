
---
title: pingora
---

### [cloudflare pingora](https://github.com/cloudflare/pingora)  ![GitHub Repo stars](https://img.shields.io/github/stars/cloudflare/pingora?style=social)

Pingora 是一个基于 Rust 的框架，用于构建快速、可靠且可编程的网络系统。

**核心功能：**
- 支持 HTTP/1 和 HTTP/2 端到端代理。
- 支持多种 TLS 实现（OpenSSL, BoringSSL, s2n-tls, rustls）。
- 支持 gRPC 和 WebSocket 代理。
- 提供优雅重载（Graceful reload）。
- 支持可定制的负载均衡和故障转移策略。
- 兼容多种可观测性工具。

**主要优势：**
- 内存安全：提供比 C/C++ 服务更高的安全性。
- 高性能：快速且高效。
- 高可编程：API 高度灵活，支持深度定制。

**项目架构：**
包含 Pingora 主库、核心功能库、代理逻辑、HTTP 定义、SSL 扩展及缓存算法等多个组件模块。