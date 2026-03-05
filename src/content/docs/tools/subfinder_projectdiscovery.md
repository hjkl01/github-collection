
---
title: subfinder
---

### [projectdiscovery subfinder](https://github.com/projectdiscovery/subfinder)  ![GitHub Repo stars](https://img.shields.io/github/stars/projectdiscovery/subfinder?style=social)

subfinder 是一款快速、轻量的被动子域名枚举工具，用于通过被动在线源发现网站的有效子域名。该项目架构简单模块化，专注于速度和隐蔽性，适用于渗透测试人员和漏洞猎人。

主要功能包括：
- 支持多种输出格式（JSON、文件、stdout）及 STDIN/OUT 集成，方便工作流整合。
- 提供精选的被动数据源，具备快速解析和通配符消除模块。
- 支持自定义 DNS 解析器、代理、速率限制及源过滤配置。
- 部分数据源需配置 API 密钥，同时支持作为 Go 库使用。