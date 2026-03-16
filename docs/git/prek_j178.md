### [j178 prek](https://github.com/j178/prek)  ![GitHub Repo stars](https://img.shields.io/github/stars/j178/prek?style=social)

prek 是一个基于 Rust 开发的钩子框架，旨在作为 pre-commit 的更快、无依赖且兼容的替代品。

- **零依赖**：提供单一二进制文件，无需安装 Python 或其他运行时环境。
- **高性能**：执行速度显著快于 pre-commit，磁盘空间占用更少。
- **全兼容**：完全兼容原有的 pre-commit 配置文件和钩子。
- **增强特性**：内置支持 monorepo 工作区模式，集成 uv 管理 Python 环境，优化多语言工具链安装，并提供 Rust 原生实现的内置钩子。