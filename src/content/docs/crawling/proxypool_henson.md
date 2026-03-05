
---
title: proxypool
---

### [henson proxypool](https://github.com/henson/proxypool)  ![GitHub Repo stars](https://img.shields.io/github/stars/henson/proxypool?style=social)

这是一个基于 Golang 实现的 IP 代理池项目，用于采集免费代理资源并为爬虫提供有效 IP。

核心功能：
1. **多源采集**：支持从多个免费网站抓取代理，可自定义扩展采集接口。
2. **代理验证**：临时存储并验证代理有效性，定时检测并剔除无效或低速代理。
3. **多数据库支持**：支持 MySQL、PostgreSQL、SQLite3 等多种数据库存储。
4. **API 服务**：提供 HTTP 和 HTTPS 代理的 JSON 查询接口，方便爬虫调用。
5. **异常容错**：具备异常恢复机制，单个采集源故障不影响整体程序运行。