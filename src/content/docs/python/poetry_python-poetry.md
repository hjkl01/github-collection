
---
title: poetry
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/python-poetry/poetry?style=social) ](https://github.com/python-poetry/poetry)
### [python-poetry poetry](https://github.com/python-poetry/poetry)

**项目核心内容总结：**  
Poetry 是一个 Python 依赖管理和打包工具，通过 `pyproject.toml` 文件替代传统的 `setup.py`、`requirements.txt` 等，简化依赖声明与项目配置。其核心功能包括：  
- **依赖管理**：支持语义化版本控制（如 `aiohttp (>=3.8.1,<4.0.0)`）、可选依赖分组（如 `dev`、`docs`）、Git 依赖（如 `cleo @ git+https://...`）及预发布版本控制。  
- **项目配置**：声明项目元数据（名称、版本、作者、许可证等）、脚本入口（如 `my_package_cli`）及多环境依赖（如 `pytest` 仅在开发环境安装）。  
- **安装与构建**：提供多种安装方式（如官方脚本 `install.python-poetry.org`），支持虚拟环境管理、包构建（`poetry build`）及发布到 PyPI。  

**使用方法**：  
1. 安装 Poetry（通过脚本或文档指引）。  
2. 创建项目：`poetry new my-package`。  
3. 添加依赖：`poetry add <package>`。  
4. 安装依赖：`poetry install`。  
5. 构建与发布：`poetry build`、`poetry publish`。  

**主要特性**：  
- 支持 Python 版本约束（如 `>=3.9,<4.0`）。  
- 依赖分组与可选依赖（如 `--with docs` 安装文档依赖）。  
- 集成 PyPI 与 Git 仓库，支持版本锁定（`poetry lock`）。  
- 提供脚本定义、项目元数据管理及多环境配置。