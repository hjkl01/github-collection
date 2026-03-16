### [theskumar python-dotenv](https://github.com/theskumar/python-dotenv)  ![GitHub Repo stars](https://img.shields.io/github/stars/theskumar/python-dotenv?style=social)

python-dotenv 是一个 Python 库，用于从 `.env` 文件读取键值对并设置为环境变量，遵循 12-factor 应用原则。主要功能包括：
1. 通过 `load_dotenv` 将配置加载到系统环境变量 `os.environ`。
2. 通过 `dotenv_values` 将配置解析为字典而不修改现有环境。
3. 支持从流（Stream）读取配置。
4. 提供命令行工具 `dotenv` 管理 `.env` 文件。
5. 支持 IPython 扩展。
6. 支持变量展开、多行值及类 Bash 语法格式。