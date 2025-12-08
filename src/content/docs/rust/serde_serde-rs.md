
---
title: serde
---

### [serde-rs serde](https://github.com/serde-rs/serde)

**核心内容总结：**  
Serde 是一个高效、通用的 Rust 数据结构序列化与反序列化框架，支持 JSON、Bincode 等多种数据格式。  

**使用方法：**  
1. 在 `Cargo.toml` 中添加 `serde` 依赖（需启用 `derive` 特性），并根据需求引入对应数据格式的 crate（如 `serde_json`）。  
2. 使用 `#[derive(Serialize, Deserialize)]` 宏为结构体或枚举添加序列化/反序列化能力。  
3. 通过 `serde_json::to_string` 和 `serde_json::from_str` 等方法实现数据转换。  

**主要特性：**  
- 支持广泛的数据格式（如 JSON、XML、CBOR 等）。  
- 提供 `derive` 宏简化自定义类型处理。  
- 高效性能，适用于复杂数据结构。  
- 兼容 Rust 1.56（核心库）和 1.68（derive 宏）及以上版本。