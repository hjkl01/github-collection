
---
title: tracing
---

### [tokio-rs tracing](https://github.com/tokio-rs/tracing)

**项目核心内容总结：**  
该项目是一个用于Rust语言的**诊断、日志记录和性能分析**工具库，提供结构化日志、跨度追踪（Span）和事件记录功能，帮助开发者分析程序行为和性能瓶颈。  

**主要功能与特性：**  
1. **结构化日志**：支持记录结构化数据，便于分析和处理。  
2. **跨度追踪**：通过`span`记录代码执行路径，支持上下文传播（如HTTP请求链路追踪）。  
3. **异步支持**：兼容异步编程模型（如`tokio`），可追踪异步任务。  
4. **过滤器机制**：通过`tracing-subscriber`动态控制日志级别和输出内容。  
5. **宏辅助**：使用`#[tracing::instrument]`自动记录函数调用信息，简化代码。  
6. **与现有日志库兼容**：可集成`log`、`env_logger`等库，支持自定义输出格式（如JSON、日志文件）。  

**使用方法：**  
1. 引入依赖（如`tracing`、`tracing-subscriber`）。  
2. 初始化订阅者（如`tracing_subscriber::fmt::Subscriber::builder().init()`）。  
3. 使用`#[tracing::instrument]`宏标记需追踪的函数。  
4. 通过`tracing::info!`等宏记录事件或日志。  

**适用场景：**  
适用于需要精细化调试、性能分析或分布式系统链路追踪的Rust项目。