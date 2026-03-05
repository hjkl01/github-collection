
---
title: python-dotenv
---

### [theskumar python-dotenv](https://github.com/theskumar/python-dotenv)  ![GitHub Repo stars](https://img.shields.io/github/stars/theskumar/python-dotenv?style=social)

python-dotenv 是一个 Python 库，用于从 `.env` 文件读取键值对并设置为环境变量，以支持遵循 12 因子原则的应用开发。

主要功能包括：
1. 环境变量管理：通过 `load_dotenv` 加载配置到 `os.environ`（默认不覆盖现有变量），或通过 `dotenv_values` 以字典形式获取配置。
2. 灵活加载：支持从流（如网络源）读取、在 IPython 中使用及通过环境变量禁用加载。
3. 命令行工具：提供 CLI 接口用于查看、设置 `.env` 变量或运行脚本。
4. 文件格式：支持类似 Bash 的语法，包含注释、引号、多行值及变量扩展功能。