
---
title: expr
---

### [expr-lang expr](https://github.com/expr-lang/expr)  ![GitHub Repo stars](https://img.shields.io/github/stars/expr-lang/expr?style=social)

Expr 是一款专为 Go 语言设计的表达式评估引擎，旨在提供安全、快速且准确的动态配置能力。其核心功能包括：

1. **安全隔离**：内存安全、无副作用且保证程序有限终止，防止无限循环。
2. **Go 原生集成**：与 Go 类型系统无缝对接，无需重新定义类型。
3. **静态类型**：编译时检查类型，防止运行时类型错误。
4. **功能丰富**：支持多种操作符及内置函数（如 all、filter、map 等），并提供友好的错误提示。
5. **高性能**：采用优化编译器和字节码虚拟机，执行效率极高。

目前被广泛用于业务规则引擎、云平台配置、自动化决策及数据处理等领域。