
---
title: maturin
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/PyO3/maturin?style=social) ](https://github.com/PyO3/maturin)
### [PyO3 maturin](https://github.com/PyO3/maturin)

**项目核心内容总结：**  
Maturin 是一个将 Rust 代码转换为 Python 模块的工具，支持生成 Python 绑定（如 cffi、pyo3 等），并处理跨平台兼容性问题。  

**主要功能与特性：**  
1. **功能**：  
   - 将 Rust 库封装为 Python 可用的模块，支持多种绑定类型（如 cffi、pyo3、bin 等）。  
   - 自动检测依赖并生成符合 manylinux 标准的 Linux 轮子（wheel），确保兼容性。  
   - 提供命令行工具（如 `maturin build`、`maturin sdist`）简化构建流程。  

2. **使用方法**：  
   - 安装 Maturin 后，通过 `maturin build` 构建 Python 模块，支持指定参数（如 `--release`、`--manylinux`）。  
   - 使用 Docker 容器（如 `ghcr.io/pyo3/maturin`）在 manylinux 环境中构建，确保 Linux 轮子合规。  

3. **关键特性**：  
   - **跨平台兼容**：支持 Windows、macOS、Linux，自动处理 manylinux 依赖。  
   - **高效构建**：集成 Rust 编译器与 Python 工具链，支持增量构建和调试模式。  
   - **社区支持**：提供示例项目（如 polars、deltalake-python）和贡献指南，支持多种 Rust 库的绑定。  

**适用场景**：需要将高性能 Rust 代码集成到 Python 生态中的开发者，或需发布跨平台 Python 轮子的项目。