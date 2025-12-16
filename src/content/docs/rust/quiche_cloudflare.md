
---
title: quiche
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/cloudflare/quiche?style=social) ](https://github.com/cloudflare/quiche)
### [cloudflare quiche](https://github.com/cloudflare/quiche)

quiche 是一个基于 Rust 实现的 QUIC 和 HTTP/3 协议库，提供低级 API 用于处理网络连接和数据传输。其核心功能包括：  
1. **协议支持**：完整实现 QUIC 协议及 HTTP/3，支持加密握手（基于 BoringSSL 或 OpenSSL）。  
2. **跨语言集成**：提供 Rust 原生 API 及 C 语言薄封装，便于嵌入 C/C++ 应用。  
3. **使用方式**：通过配置 `Connection` 对象处理数据包收发、超时管理、流控制，HTTP/3 模块支持高层应用开发。  
4. **构建支持**：需 Rust 1.85+，支持多平台（Linux、Android、iOS、Docker），可通过 `cargo` 构建，Android/iOS 需额外配置 NDK 或 Xcode 工具链。  
5. **特性**：提供示例代码（如 `examples/` 目录），支持 FFI 功能，兼容性测试覆盖主流环境。