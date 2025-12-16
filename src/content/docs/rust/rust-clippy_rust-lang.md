
---
title: rust-clippy
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/rust-lang/rust-clippy?style=social) ](https://github.com/rust-lang/rust-clippy)
### [rust-lang rust-clippy](https://github.com/rust-lang/rust-clippy)

Clippy 是一个用于 Rust 代码的静态分析工具，包含 750 多个 lint（代码检查规则），用于发现常见错误并优化代码风格。其核心功能包括：  
1. **分类 lint**：按功能分为正确性、可疑代码、风格、复杂度、性能等类别，每类有默认检查级别（如 warn/deny）。  
2. **灵活配置**：可通过代码注解（如 `#[deny(...)]`）或命令行参数（如 `-- -W clippy::lint_name`）控制 lint 的检查级别。  
3. **配置文件支持**：通过 `clippy.toml` 或 `.clippy.toml` 文件自定义部分 lint 行为（如禁用特定警告、设置最低 Rust 版本）。  
4. **使用方式**：支持作为 Cargo 子命令（`cargo clippy`）安装和运行，也可在非 Cargo 项目中通过 `clippy-driver` 使用。  

**主要特性**：  
- 提供自动修复部分代码问题的功能（`--fix` 参数）。  
- 支持工作区（workspace）中对指定 crate 运行检查。  
- 通过 `#![clippy::msrv]` 设置最低支持的 Rust 版本，避免新特性兼容性问题。  
- 部分 lint（如 `restriction` 类别）需谨慎启用，可能产生误报或与代码风格冲突。