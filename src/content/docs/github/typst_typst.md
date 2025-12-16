
---
title: typst
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/typst/typst?style=social) ](https://github.com/typst/typst)
### [typst typst](https://github.com/typst/typst)

Typst 是一个功能强大且易于学习的基于标记的排版系统，旨在替代 LaTeX。其核心功能包括：  
- **内置标记语法**：简化常见格式化操作（如标题、列表）；  
- **脚本系统**：支持通过代码实现复杂逻辑（如动态生成表格）；  
- **数学排版与参考文献管理**：兼容 LaTeX 数学公式和引用格式；  
- **高效编译**：通过增量编译技术实现快速预览，提升工作效率；  
- **友好错误提示**：清晰定位并提示用户修改错误。  

**使用方法**：  
1. **安装**：支持多种方式，包括下载二进制文件、通过包管理器（如 Homebrew、Windows 的 winget）、Rust 工具链编译，或使用 Docker。  
2. **命令行操作**：使用 `typst compile` 生成输出文件，`typst watch` 实现实时预览；支持自定义字体路径以适配不同需求。  

**主要特性**：  
- 通过一致性设计降低学习成本（如标题语法 `= 标题` 与 `#heading[标题]` 等效）；  
- 强调可组合性，提供灵活的模块化功能（如自定义样式规则）；  
- 基于 `comemo` 系统实现增量编译，优化性能。