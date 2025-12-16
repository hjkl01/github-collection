
---
title: tree-sitter
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/tree-sitter/tree-sitter?style=social) ](https://github.com/tree-sitter/tree-sitter)
### [tree-sitter tree-sitter](https://github.com/tree-sitter/tree-sitter)

**项目核心内容总结：**  
tree-sitter 是一个解析器生成器工具和增量解析库，用于为源文件构建具体语法树，并在文件编辑时高效更新语法树。其主要特性包括：  
- **通用性**：支持解析任何编程语言；  
- **高效性**：可实现在文本编辑器中每键入一次即实时解析；  
- **鲁棒性**：即使存在语法错误仍能提供有用结果；  
- **无依赖**：纯 C 编写的运行时库，可嵌入任意应用。  

**使用方法**：  
提供文档、Rust 绑定、Wasm 绑定及命令行接口（CLI），支持多种编程语言和环境集成。