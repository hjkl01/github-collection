
---
title: IPProxyPool
---

### [qiyeboy IPProxyPool](https://github.com/qiyeboy/IPProxyPool)

**项目核心内容总结：**

**1. 项目功能**  
IPProxyPool 是一个用于爬虫的代理IP池管理系统，支持自动爬取、验证和维护代理IP，提供HTTP API接口供用户调用。支持多种数据库（SQLite/MySQL/MongoDB），具备评分机制筛选稳定IP，可自定义代理检测规则。

**2. 使用方法**  
- 配置 `config.py` 中的数据库连接、线程数、API端口等参数。  
- 启动爬虫自动采集代理IP（支持多网站解析规则）。  
- 通过 `http://localhost:8000` 接口获取代理IP，支持按 `country`（国内/国外）、`type`（代理类型）、`protocol`（协议）等参数过滤。  
- 自定义检测函数（如替换为百度验证）以提升代理可用性。

**3. 主要特性**  
- **多数据库兼容**：适配 SQLite、MySQL、MongoDB。  
- **自动维护机制**：定时检测IP有效性，失效IP自动降分并删除。  
- **高效爬取**：基于多进程+协程技术，爬取速度提升50倍以上。  
- **灵活扩展**：支持XPath/正则解析网页，可添加新代理网站规则。  
- **兼容性强**：同时支持 Python 2 和 Python 3。