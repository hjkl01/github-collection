
---
title: rust-analyzer
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/rust-lang/rust-analyzer?style=social) ](https://github.com/rust-lang/rust-analyzer)
### [rust-lang rust-analyzer](https://github.com/rust-lang/rust-analyzer)

**项目核心内容总结：**  
rust-analyzer 是一个为 Rust 编程语言提供 IDE 功能的语言服务器，支持通过语言服务器协议（LSP）与各类编辑器（如 VS Code、Vim、Emacs 等）集成。  

**主要功能：**  
- 代码导航（跳转定义、查找引用）  
- 重构与代码补全  
- 集成格式化（基于 rustfmt）  
- 集成诊断（基于 rustc 和 clippy）  

**使用方法：**  
通过编辑器的 LSP 插件调用，具体安装和配置方法见项目手册的 [安装指南](https://rust-analyzer.github.io/book/installation.html)。  

**其他信息：**  
- 项目文档和使用技巧详见 [官方手册](https://rust-analyzer.github.io/book/)  
- 源码采用 MIT 和 Apache 2.0 双许可证（见 LICENSE-APACHE 和 LICENSE-MIT 文件）