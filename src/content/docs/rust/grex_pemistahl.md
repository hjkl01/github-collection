
---
title: grex
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/pemistahl/grex?style=social) ](https://github.com/pemistahl/grex)
### [pemistahl grex](https://github.com/pemistahl/grex)

**项目核心内容总结：**  
grex 是一个基于 Rust 开发的工具，用于从一组输入字符串自动生成对应的正则表达式。其核心功能包括：  
1. **正则生成**：通过 DFA 最小化和 Brzozowski 代数方法，将输入字符串转换为精确的正则表达式，支持多种字符集替换（如 `-d` 数字、`-s` 空格、`-w` 单词字符等）和转义选项（`-e` Unicode 转义）。  
2. **多平台支持**：提供命令行工具、Python 扩展模块（通过 PyO3 和 Maturin 构建）及 WebAssembly 版本，适用于浏览器或 Node.js 环境。  
3. **灵活配置**：支持重复字符合并（`-r`）、选项组合（如 `-drsw` 同时启用数字、空格、单词字符替换和重复优化），并兼容复杂字符（如 emoji、阿拉伯数字等）。  
4. **高效构建**：通过 Cargo 管理 Rust 代码，支持单元测试、基准测试及跨平台编译（包括 WASM）。  

**使用方法**：  
- 命令行：`grex <输入字符串>` 或 `grex -e -r <输入字符串>` 添加选项。  
- Python：安装 `pip install grex` 后，使用 `from grex import RegExpBuilder` 构建正则。  
- WebAssembly：通过 `wasm-pack` 编译后，在 JavaScript 中调用生成的 `RegExpBuilder`。