
---
title: icecream
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/gruns/icecream?style=social) ](https://github.com/gruns/icecream)
### [gruns icecream](https://github.com/gruns/icecream)

**IceCream 核心内容总结：**

IceCream 是一个 Python 调试工具，用于替代传统的 `print()` 语句，简化调试流程。其核心功能包括：

1. **自动打印变量与表达式**：无需手动写 `print("变量名", 变量)`，`ic()` 会自动输出变量名和值，例如 `ic(foo(123))` 输出 `ic| foo(123): 456`。
2. **格式化输出**：支持数据结构（如字典、列表）的美观打印，语法高亮。
3. **上下文信息**：可选显示调用 `ic()` 的文件名、行号及函数名，便于定位问题。
4. **灵活配置**：支持自定义输出格式（如前缀、绝对路径）、禁用/启用调试输出、集成日志模块等。
5. **无侵入性**：`ic()` 的返回值不影响原代码逻辑，可直接替换 `print()`。

**使用方法**：
- 安装：`pip install icecream`。
- 导入并调用：`from icecream import ic; ic(变量)`。
- 全局安装：通过 `install` 选项避免重复导入。

**其他特性**：
- 支持 Python 3 和 PyPy3。
- 提供多语言版本（如 Rust、Node.js、Go 等）。