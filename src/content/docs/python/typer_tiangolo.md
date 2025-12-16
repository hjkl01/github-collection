
---
title: typer
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/tiangolo/typer?style=social) ](https://github.com/tiangolo/typer)
### [tiangolo typer](https://github.com/tiangolo/typer)

**核心内容总结：**  
Typer 是一个基于 Python 类型提示的 CLI（命令行接口）开发库，用于创建用户和开发者都喜欢的命令行应用。其核心功能包括自动生成帮助信息、自动补全、支持复杂命令结构（如子命令和分组），并能将普通脚本自动转换为 CLI 应用。  

**使用方法：**  
1. 安装：通过 `pip install typer` 安装。  
2. 基本用法：在代码中使用 `typer.run(main)` 或通过 `typer` 命令运行脚本（如 `typer main.py run`）。  
3. 示例：定义函数参数（如 `name: str`），Typer 会自动处理参数解析、帮助信息和补全功能。  

**主要特性：**  
- **直观开发**：无需学习新语法，直接使用 Python 类型提示（如 `int`、`bool`）定义参数。  
- **自动补全**：支持主流终端（Bash、Zsh 等）的自动补全，提升用户交互体验。  
- **灵活结构**：支持单命令、多命令、子命令分组及复杂参数验证。  
- **与 FastAPI 类似**：基于 Click 库构建，提供类似 FastAPI 的开发体验。