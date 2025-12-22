
---
title: cupp
---

### [Mebus cupp](https://github.com/Mebus/cupp)  ![GitHub Repo stars](https://img.shields.io/github/stars/Mebus/cupp?style=social)

**项目功能**  
CUPP 是一个用于生成常见用户密码的工具，主要用于渗透测试或法医调查。通过分析用户个人信息（如生日、昵称、姓名等）生成潜在密码，或基于现有字典、数据库进行扩展，帮助测试密码强度或破解弱密码。

**使用方法**  
- 交互式模式（`-i`）：通过回答问题生成密码。  
- 字典模式（`-w`）：使用现有字典或 WyD.pl 输出生成密码。  
- 下载字典（`-l`）：从远程仓库获取大型字典。  
- 数据库解析（`-a`）：从 Alecto 数据库提取用户名和密码。

**主要特性**  
- 支持 Python 3 运行。  
- 提供交互式密码生成和字典扩展功能。  
- 可解析 Alecto 数据库（整合 Phenoelit 和 CIRT 数据）。  
- 开源免费，采用 GNU GPL v3 许可证。