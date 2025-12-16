
---
title: dynaconf
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/rochacbruno/dynaconf?style=social) ](https://github.com/rochacbruno/dynaconf)
### [rochacbruno dynaconf](https://github.com/rochacbruno/dynaconf)

**核心内容总结：**  

**项目功能**  
Dynaconf 是 Python 的配置管理工具，支持多环境配置管理、敏感信息保护、配置验证与解析、多文件格式（TOML/YAML/JSON/INI/PY）加载，集成 Hashicorp Vault 和 Redis 作为配置存储，并提供 Django/Flask 框架扩展及 CLI 工具。  

**使用方法**  
1. 安装：`pip install dynaconf`  
2. 初始化项目：通过 `dynaconf init -f <格式>` 生成配置文件（如 `settings.toml` 和 `.secrets.toml`），并创建 `config.py` 用于导入配置对象。  
3. 配置管理：在 `settings.*` 文件中定义常规配置，在 `.secrets.*` 文件中定义敏感信息，环境变量可覆盖配置（如 `export DYNACONF_PORT=9900`）。  
4. 代码中使用：通过 `from config import settings` 导入配置对象，支持点符号访问（如 `settings.username`）或字典方式（如 `settings['password']`）。  

**主要特性**  
- 遵循 12-factor 应用配置规范  
- 支持多环境分层（开发/测试/生产）  
- 环境变量自动覆盖配置，内置 dotenv 支持  
- 敏感信息隔离存储（`.secrets.*` 文件）  
- 支持自定义配置加载器和模板替换  
- 提供 CLI 工具（初始化、导出、验证等）  
- 集成 Hashicorp Vault 和 Redis 作为安全存储  
- 与 Django/Flask 框架深度兼容