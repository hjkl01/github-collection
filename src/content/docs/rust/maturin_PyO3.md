
---
title: maturin
---

### [PyO3 maturin](https://github.com/PyO3/maturin)  ![GitHub Repo stars](https://img.shields.io/github/stars/PyO3/maturin?style=social)

Maturin（原 pyo3-pack）是用于将 Rust 项目构建并发布为 Python 包的工具。支持使用 pyo3、cffi 和 uniffi 绑定生成 Python wheel 和源分发包（sdist），并可上传至 PyPI。

主要功能：
1. 跨平台构建：支持 Windows、Linux、macOS 和 FreeBSD，兼容 Python 3.8+、PyPy 及 GraalPy。
2. 便捷命令：提供 build 构建轮子、develop 快速安装至虚拟环境、new 初始化项目。
3. 配置集成：支持 pyproject.toml 管理元数据和依赖（符合 PEP 621），自动合并 Cargo.toml 信息。
4. 平台合规：内置 Linux manylinux 兼容性检查与修复，确保广泛兼容发布。
5. 项目支持：支持混合 Rust/Python 项目结构，无需额外配置文件，兼容现有 setuptools-rust 配置。