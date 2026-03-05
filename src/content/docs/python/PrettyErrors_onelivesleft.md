
---
title: PrettyErrors
---

### [onelivesleft PrettyErrors](https://github.com/onelivesleft/PrettyErrors)  ![GitHub Repo stars](https://img.shields.io/github/stars/onelivesleft/PrettyErrors?style=social)

pretty-errors 是一个用于美化 Python 异常输出的工具，旨在提升错误信息的可读性。

核心功能：
1. 异常美化：将标准异常追溯转换为格式清晰、易读的输出，支持彩色和单色模式。
2. 安装使用：支持通过命令全局激活（推荐，可捕获 SyntaxError）或在代码中导入。
3. 丰富配置：可自定义分隔符、显示格式、代码片段、局部变量、颜色及截断方式等。
4. 路径管理：支持文件路径的白名单/黑名单过滤，以及针对不同路径的差异化配置。
5. 兼容扩展：支持替换 STDERR 输出以兼容特殊框架，支持环境变量控制激活行为，支持自定义异常写入器进行深度扩展。