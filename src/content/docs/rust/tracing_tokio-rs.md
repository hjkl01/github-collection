
---
title: tracing
---

### [tokio-rs tracing](https://github.com/tokio-rs/tracing)  ![GitHub Repo stars](https://img.shields.io/github/stars/tokio-rs/tracing?style=social)

`tracing` 是一个用于为 Rust 程序添加插桩以收集结构化、基于事件诊断信息的框架。由 Tokio 项目维护，但不依赖 Tokio 运行时。

核心功能与特性：
1. **应用程序与库支持**：应用程序通过 `Subscriber` 收集追踪数据（如输出到日志），库仅使用宏记录有用信息而不安装 `Subscriber`。
2. **插桩工具**：提供宏（如 `info!`, `debug!`）和过程宏属性（如 `#[instrument]`），用于在代码中定义事件和调用上下文。
3. **异步追踪**：支持 `async` 代码追踪，通过 `Future::instrument` 或属性宏正确处理异步生命周期。
4. **模块化生态**：包含核心库（`tracing`, `tracing-core`）、订阅者实现（`tracing-subscriber`）、过程宏（`tracing-attributes`）及多个兼容工具（如日志兼容、序列化、错误追踪、性能分析等），支持第三方扩展集成。