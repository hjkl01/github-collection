
---
title: IPProxyPool
---

### [qiyeboy IPProxyPool](https://github.com/qiyeboy/IPProxyPool)  ![GitHub Repo stars](https://img.shields.io/github/stars/qiyeboy/IPProxyPool?style=social)

IPProxyPool 是一个支持 Python 2 和 Python 3 的代理 IP 池项目，核心功能如下：
1. 自动采集：支持自定义多网站解析规则，自动爬取代理 IP。
2. 验证评分：定期检测 IP 有效性，采用评分机制自动清理无效代理。
3. 数据存储：默认 SQLite，基于 ORM 可扩展支持 MySQL、MongoDB 及 Redis。
4. API 服务：提供 Web 接口查询和删除代理 IP，支持按类型、协议、地区筛选，返回数据按评分和速度排序。
5. 性能优化：采用多进程加协程模式提升效率，支持自定义检测函数和反爬虫策略。