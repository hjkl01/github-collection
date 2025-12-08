
---
title: polars
---

### [pola-rs polars](https://github.com/pola-rs/polars)

### 核心内容总结

**项目功能**  
Polars 是一个用 Rust 编写的高性能 DataFrame 查询引擎，支持 Python、Rust、Node.js、R 和 SQL 等多种语言。其核心功能包括：  
- **懒加载与即时执行**：灵活控制查询执行方式。  
- **流式处理**：支持处理超出内存容量的数据集。  
- **多线程与 SIMD 优化**：利用硬件加速提升计算效率。  
- **查询优化**：自动优化执行计划以提高性能。  

**主要特性**  
- 基于 Apache Arrow 列式存储格式，兼容性强。  
- 性能远超 Pandas 和 NumPy（如导入时间：Polars 70ms，Pandas 520ms）。  
- 支持超大规模数据（如 250GB 数据集可本地处理）。  
- 提供丰富的表达式 API 和多语言接口。  

**使用方法**  
- **Python 安装**：`pip install polars`，支持通过 `pl.show_versions()` 查看版本及依赖。  
- **源码编译**：需安装 Rust 和 Maturin，通过 `make build` 等命令构建不同优化版本。  
- **扩展功能**：支持通过 Rust 编写自定义 UDF（用户自定义函数）。  

**其他**  
- 提供云服务（[cloud.pola.rs](https://cloud.pola.rs/)）用于分布式计算。  
- 支持特殊需求编译（如 `pip install polars[rt64]` 处理超 42 亿行数据，`pip install polars[rtcompat]` 适配老旧硬件）。