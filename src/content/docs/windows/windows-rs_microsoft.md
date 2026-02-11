
---
title: windows-rs
---

### [microsoft windows-rs](https://github.com/microsoft/windows-rs)  ![GitHub Repo stars](https://img.shields.io/github/stars/microsoft/windows-rs?style=social)

该项目为 Rust 语言提供了对 Windows API 的全面支持，使开发者能够通过 Rust 调用任何过去、现在和未来的 Windows API。它通过从微软提供的元数据中动态生成代码，并将其直接集成到 Rust 项目中，使得 Windows API 调用如同调用普通 Rust 模块一样自然。

**主要功能：**

- 提供对 Windows API 的绑定，包括 C 风格 API、COM 和 WinRT 接口。
- 使用标准 Rust 语言，无需特殊编译器或工具链。
- 支持异步、线程、注册表、字符串、集合等 Windows 特定类型和功能。
- 提供代码生成工具 `windows-bindgen`，用于从元数据生成 Rust 绑定代码。

**使用方法：**

- 通过 Cargo 使用相关 crate（如 `windows`、`windows-sys`）。
- 可参考官方提供的示例代码进行开发。
- 提供特征搜索功能，方便查找所需 API。

**主要特性：**

- 安全性高，提供安全绑定（`windows` crate）和原始绑定（`windows-sys` crate）。
- 与 C++/WinRT 保持一致的投影方式，符合 Rust 的语言习惯。
- 支持 Windows 的多种功能模块，如异步、线程、注册表、集合等。
- 提供版本信息、元数据解析、链接支持等辅助功能。

该项目是微软官方维护的 Windows Rust 项目集合，包括多个辅助 crate，适用于需要深度集成 Windows API 的 Rust 开发场景。