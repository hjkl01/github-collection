
---
title: cutile-python
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/NVIDIA/cutile-python?style=social) ](https://github.com/NVIDIA/cutile-python)
### [NVIDIA cutile-python](https://github.com/NVIDIA/cutile-python)

**核心内容总结：**  
cuTile Python 是一种用于 NVIDIA GPU 的编程语言，支持编写并行执行的 GPU 内核（如向量加法）。用户可通过 PyPI 安装（`pip install cuda-tile`）或从源码构建（需 CUDA Toolkit 13.1+、CMake 3.18+ 等依赖）。其核心特性包括基于 Tile IR 的编译器，要求 NVIDIA 驱动版本 r580 或更高，当前仅支持 Blackwell GPU（后续版本将扩展）。测试依赖 PyTest 及额外库（如 PyTorch），代码通过 `pytest` 运行。项目遵循 Apache 2.0 许可证，由 NVIDIA 2025 年版权所有。