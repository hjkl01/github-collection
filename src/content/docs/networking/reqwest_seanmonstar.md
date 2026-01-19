
---
title: reqwest
---

### [seanmonstar reqwest](https://github.com/seanmonstar/reqwest)  ![GitHub Repo stars](https://img.shields.io/github/stars/seanmonstar/reqwest?style=social)

**核心内容总结：**

reqwest 是一个功能全面的 Rust HTTP 客户端库，支持异步和同步请求，提供以下核心功能：  
- 支持多种请求体格式（纯文本、JSON、表单、多部分文件）  
- 可自定义重定向策略和 HTTP 代理  
- 通过 rustls 或系统 TLS 实现 HTTPS（Linux 需 OpenSSL 或启用 vendored 版本）  
- 内置 Cookie 管理及 WASM 支持  

**使用方法**：  
集成需在 `Cargo.toml` 中添加 `reqwest` 依赖（示例启用 `json` 特性），结合异步运行时（如 Tokio）发送请求，例如：  
```rust
reqwest::get("https://httpbin.org/ip").await?.json().await?
```  

**许可证**：采用 Apache 2.0 或 MIT 双许可。