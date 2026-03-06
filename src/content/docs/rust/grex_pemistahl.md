
---
title: grex
---

### [pemistahl grex](https://github.com/pemistahl/grex)  ![GitHub Repo stars](https://img.shields.io/github/stars/pemistahl/grex?style=social)

grex 是一个库和命令行工具，用于根据用户提供的测试用例自动生成正则表达式。它生成的 Perl 兼容正则表达式默认精确匹配输入，但可通过选项调整为更通用的形式。

主要功能包括：
- 支持字面量、字符类、前后缀检测、重复子串量化、交替、分组及锚点。
- 支持大小写不敏感、非 ASCII 转义、Surrogate Pairs 转换及 Unicode 兼容。
- 支持命令行交互、文件读取、管道传输及多种输出格式。

该项目提供多语言支持：Rust CLI 与库、Python 扩展模块、WebAssembly（JavaScript 环境）。底层算法基于 DFA 最小化及 Brzozowski 代数方法。建议将其用于生成初始正则表达式，后续通常需人工审核与优化。