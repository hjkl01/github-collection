
---
title: typer
---

### [tiangolo typer](https://github.com/tiangolo/typer)  ![GitHub Repo stars](https://img.shields.io/github/stars/tiangolo/typer?style=social)

Typer 是一个基于 Python 类型提示的命令行（CLI）应用程序构建库，被誉为"CLI 领域的 FastAPI"。

核心功能：
*   **开发直观**：使用标准 Python 类型声明参数，提供完善的编辑器支持和自动补全。
*   **自动辅助**：自动生成帮助文档及终端自动补全（支持多种 Shell）。
*   **代码简洁**：最小化代码重复，支持从简单脚本到复杂子命令树结构的扩展。
*   **脚本运行**：包含 `typer` 命令，可直接运行 Python 脚本并将其转换为 CLI 应用。
*   **底层依赖**：基于 Click 构建，集成 Rich 和 shellingham 用于美化输出和 Shell 检测。