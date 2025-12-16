
---
title: django-environ
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/joke2k/django-environ?style=social) ](https://github.com/joke2k/django-environ)
### [joke2k django-environ](https://github.com/joke2k/django-environ)

**项目功能**  
`django-environ` 是一个 Python 包，通过环境变量实现 Django 应用的配置，遵循 Twelve-Factor 方法论。它支持从 `.env` 文件或操作系统环境变量中读取配置，并提供类型转换（如布尔值、数据库 URL 解析等），避免硬编码配置。

**使用方法**  
1. 导入 `environ` 模块，创建 `Env` 实例并定义变量类型和默认值（如 `DEBUG=(bool, False)`）。  
2. 通过 `read_env()` 方法加载 `.env` 文件内容到 `os.environ`。  
3. 使用 `env('VARIABLE_NAME')` 获取配置值，或通过 `env.db()`、`env.cache()` 等方法解析数据库、缓存 URL。  

**主要特性**  
- 支持多环境配置（如开发、生产）。  
- 自动将 `.env` 文件变量填充到 `os.environ`，避免覆盖真实环境变量。  
- 提供 URL 解析功能（如数据库、缓存连接字符串），返回 `ParseResult` 对象。  
- 支持 Docker 风格的文件配置（通过 `FileAwareEnv`）。  
- 兼容 Django 2.2 至 5.1，Python 3.9+。