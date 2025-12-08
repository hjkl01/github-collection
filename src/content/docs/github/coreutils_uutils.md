
---
title: coreutils
---

### [uutils coreutils](https://github.com/uutils/coreutils)

**项目功能**  
uutils coreutils 是用 Rust 语言实现的 GNU coreutils 工具集，旨在成为 GNU 工具的替代品，功能与 GNU 保持一致，同时改进错误提示、支持 UTF-8 国际化、提升性能，并在适当场景下增加扩展功能（如 `--progress`）。  

**使用方法**  
可通过 `cargo install coreutils` 快速安装，或使用 GNU Make 进行构建与安装。支持跨平台（Linux、macOS、Windows 等），安装时可自定义路径、前缀，也可单独安装特定工具（如 `uu_cat`）。  

**主要特性**  
- 严格匹配 GNU 的输出与错误代码，差异视为缺陷  
- 支持多语言（UTF-8）及跨平台兼容性  
- 提供 shell 补全（bash、zsh 等）和 manpages 文档  
- 构建时可选择性编译工具（如通过 `--features` 指定平台特性）  
- 支持通过 `uudoc` 生成 manpages 和 shell 补全脚本