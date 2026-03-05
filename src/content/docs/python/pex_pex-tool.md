
---
title: pex
---

### [pex-tool pex](https://github.com/pex-tool/pex)  ![GitHub Repo stars](https://img.shields.io/github/stars/pex-tool/pex?style=social)

PEX 是一个生成 .pex（Python 可执行文件）的库，用于创建独立的可执行 Python 环境，类似于 virtualenv。它简化了 Python 应用的部署过程，支持单个 .pex 文件在 Linux 和 OS X 等跨平台环境中运行。PEX 提供命令行工具以构建包含依赖的独立环境，支持冻结当前虚拟环境、创建临时执行环境、基于 entry points 生成独立可执行文件以及指定特定 Python 解释器（如 PyPy）。项目支持 pip 安装，也可结合 Pants、Buck 等构建系统使用。