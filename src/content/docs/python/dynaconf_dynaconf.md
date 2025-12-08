
---
title: dynaconf
---

### [dynaconf dynaconf](https://github.com/dynaconf/dynaconf)

**Dynaconf** 是一个 Python 配置管理工具，支持多环境、多格式配置文件（TOML/YAML/JSON/INI/PY），并提供以下核心功能：  
- **环境变量覆盖**：通过环境变量（如 `DYNACONF_PORT`）动态修改配置值。  
- **敏感信息保护**：使用 `.secrets.toml` 存储密码、令牌等敏感数据，并支持 Hashicorp Vault 和 Redis 作为安全存储。  
- **多环境支持**：通过分层系统管理不同环境（开发、测试、生产）的配置。  
- **框架集成**：内置 Django 和 Flask 的扩展支持。  
- **CLI 工具**：提供 `init`、`list`、`write` 等命令初始化和管理配置。  
- **配置验证与模板**：支持设置默认值、验证配置结构及模板替换。  

**使用方法**：  
1. 安装：`pip install dynaconf`。  
2. 初始化项目：运行 `dynaconf init -f toml`，生成 `config.py`、`settings.toml` 和 `.secrets.toml`。  
3. 在代码中导入配置对象：`from path.to.config import settings`，通过 `settings.key` 或 `settings['key']` 访问配置。  
4. 环境变量覆盖：设置 `export DYNACONF_KEY=value` 覆盖配置文件中的值。  

**主要特性**：  
- 基于 12-Factor 应用配置规范。  
- 支持自定义配置加载器和多格式文件解析。  
- 提供配置文件的分层加载与优先级管理。