
---
title: lo
---

### [samber lo](https://github.com/samber/lo)  ![GitHub Repo stars](https://img.shields.io/github/stars/samber/lo?style=social)

samber/lo 是基于 Go 1.18+ 泛型的 Lodash 风格 Go 工具库，旨在简化对切片、映射、字符串、通道和函数的常见操作。

主要功能包括：
*   **集合处理**：提供切片和映射的过滤、映射、分组、去重、扁平化、查找、统计及转换等数十种函数。
*   **并发工具**：支持并行处理、异步执行、重试、防抖/节流、同步锁及事务管理。
*   **通道操作**：实现通道与切片互转、分派、缓冲及 FanIn/FanOut 等并发原语。
*   **类型与错误**：包含指针转换、空值检测、Coalesce、Try/Must、ErrorsAs 等工具。
*   **其他辅助**：涵盖字符串处理、数学运算、元组操作、时间测量及控制流辅助。

项目包含 `parallel`、`mutable`、`it` 等扩展包，无外部依赖。