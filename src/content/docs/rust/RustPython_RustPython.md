
---
title: RustPython
---

### [RustPython RustPython](https://github.com/RustPython/RustPython)  ![GitHub Repo stars](https://img.shields.io/github/stars/RustPython/RustPython?style=social)

RustPython 是一个完全使用 Rust 语言编写的 Python 3 解释器（支持 CPython 3.14.0+），不依赖 CPython 绑定。它支持交互式 Shell、虚拟环境 (venv) 和 Pip 包管理（可配置 SSL 以支持 HTTPS 请求），并能编译为 WebAssembly (WASI) 模块以实现在 Web 环境或任意平台运行。项目还包含实验性的 JIT 编译器以提升性能，支持嵌入到 Rust 应用程序中执行 Python 脚本。目前项目尚处于开发阶段，未达到完全生产就绪状态。