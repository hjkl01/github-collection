
---
title: grex
---

### [pemistahl grex](https://github.com/pemistahl/grex)  ![GitHub Repo stars](https://img.shields.io/github/stars/pemistahl/grex?style=social)

grex 是一个基于 Rust 开发的库及命令行工具，用于根据用户提供的测试用例自动生成正则表达式。

主要特性：
1. **自动生成功能**：将输入字符串集转换为 Perl 兼容的正则表达式，默认确保精准匹配所有测试用例。
2. **多语言支持**：支持 Rust 原生库、Python 扩展模块及 WebAssembly 编译。
3. **灵活配置**：支持字符类转换（\d, \w, \s 等）、重复子串量化、大小写匹配、捕获组控制、锚点设置及输出美化。
4. **算法原理**：基于确定性有限自动机（DFA）最小化及 Brzozowski 代数方法求解。
5. **兼容性**：遵循 Unicode 16.0 标准，兼容 Rust regex crate，支持非 ASCII 字符转义及代理对处理。

使用建议：生成的正则表达式默认最精确，若需更通用或优化的表达式，需结合业务场景人工调整。