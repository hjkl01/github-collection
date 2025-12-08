
---
title: axum
---

### [tokio-rs axum](https://github.com/tokio-rs/axum)

**axum 核心内容总结：**

1. **项目功能**  
   axum 是一个基于 Rust 的 Web 应用框架，专注于易用性和模块化设计，提供高效、灵活的请求处理能力，支持构建高性能的 Web 服务。

2. **使用方法**  
   - 通过 `Router` 定义路由，使用宏免费（macro-free）API 映射请求路径到处理函数。  
   - 使用 `Json` 等提取器（extractors）自动解析请求体为结构体。  
   - 依赖 `tokio`、`hyper` 和 `serde` 等库，需通过 Cargo 安装。  
   - 示例代码包含 `GET`/`POST` 路由定义、请求处理及响应生成。

3. **主要特性**  
   - **无宏 API**：无需依赖宏定义路由，代码简洁。  
   - **声明式解析**：通过提取器自动解析请求参数、JSON 等数据。  
   - **错误处理**：提供简单、可预测的错误处理模型。  
   - **生态集成**：基于 `tower` 和 `tower-http`，支持中间件、压缩、日志、授权等功能，兼容 `hyper` 和 `tonic` 生态。  
   - **性能**：基于 `hyper` 实现，开销极低，性能接近原生 `hyper`。  
   - **安全性**：全程使用安全 Rust 实现，禁用 `unsafe_code`。  

4. **注意事项**  
   - 当前 `main` 分支处于 0.9 版本开发中，存在 breaking changes，稳定版本见 `0.8.x` 分支。  
   - 需 Rust 1.78 及以上版本支持。