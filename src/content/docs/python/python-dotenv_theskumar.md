
---
title: python-dotenv
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/theskumar/python-dotenv?style=social) ](https://github.com/theskumar/python-dotenv)
### [theskumar python-dotenv](https://github.com/theskumar/python-dotenv)

**核心内容总结：**  
python-dotenv 是一个 Python 库，用于从 `.env` 文件中读取键值对并设置为环境变量，帮助开发符合 12-factor 原则的应用。  

**功能与使用方法：**  
- 安装后通过 `load_dotenv()` 加载 `.env` 文件中的变量到 `os.environ`，默认不覆盖已有环境变量（可通过 `override=True` 改变）。  
- 支持多种场景：  
  - 使用 `dotenv_values()` 加载配置到字典而不修改环境。  
  - 通过流（如网络数据）解析配置。  
  - 在 IPython 中通过 `%load_ext dotenv` 加载 `.env`。  
- 提供 CLI 工具，支持设置、查看、运行命令等操作（需安装 `python-dotenv[cli]`）。  

**主要特性：**  
- **文件格式**：支持 Bash 风格语法，包括注释、引号、多行值（用 `\"` 或 `\'` 包裹）、变量扩展（如 `${VAR}`）。  
- **变量扩展**：支持 `.env` 文件内变量引用其他变量，优先级根据 `override` 参数调整（默认优先环境变量，否则优先 `.env`）。  
- **安全性**：建议将 `.env` 加入 `.gitignore`，避免泄露敏感信息。  

**其他**：  
- 可通过 `PYTHON_DOTENV_DISABLED=1` 禁用加载功能。  
- 支持与 Django 等框架集成的扩展项目（如 django-dotenv）。