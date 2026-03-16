### [joke2k django-environ](https://github.com/joke2k/django-environ)  ![GitHub Repo stars](https://img.shields.io/github/stars/joke2k/django-environ?style=social)

django-environ 是一个 Python 包，允许通过环境变量配置 Django 应用，遵循 Twelve-factor 方法论。它能从 .env 文件或操作系统读取变量，自动进行类型转换，并解析数据库及缓存等连接的 URL 字符串以生成 Django 设置。该包支持多环境部署，避免使用多个未版本控制的 settings 文件，同时兼容 Docker 风格配置。支持 Python 3.9+ 及 Django 2.2 至 6.0。