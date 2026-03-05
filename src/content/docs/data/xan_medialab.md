
---
title: xan
---

### [medialab xan](https://github.com/medialab/xan)  ![GitHub Repo stars](https://img.shields.io/github/stars/medialab/xan?style=social)

`xan` 是一款基于 Rust 编写的高性能命令行工具，专为通过 Shell 处理 CSV 文件设计。它利用 SIMD 解析器和多线程技术，能够高效处理 GB 级的大数据文件。核心功能包括预览、过滤、切片、聚合、排序、连接和去重 CSV 数据，支持命令链式组合与专用表达式语言进行复杂计算。除标准 CSV 外，还支持多种学科格式（如 `.vcf`, `.cdx`）及与 JSON、Excel 等格式的转换。此外，工具具备终端可视化能力，可生成直方图、散点图、热力图等多种图表。