
---
title: proxypool
---

### [henson proxypool](https://github.com/henson/proxypool)  ![GitHub Repo stars](https://img.shields.io/github/stars/henson/proxypool?style=social)

这是一个基于 Golang 开发的开源 IP 代理池项目，旨在采集免费代理资源并提供有效的 IP 给爬虫使用。

核心功能如下：
1. **多源采集**：内置 66ip、IP181、Proxylist+ 等多个免费代理网站抓取功能，支持用户自定义扩展采集接口。
2. **自动验证**：通过 Channel 机制和定时任务验证代理有效性，自动剔除无效或速度过慢的代理。
3. **多库支持**：支持 MySQL、PostgreSQL、SQLite 等多种数据库进行数据持久化存储。
4. **API 服务**：提供 HTTP 接口（GET 请求）返回 JSON 格式的可用代理 IP，支持随机获取 HTTP 及 HTTPS 代理。
5. **稳定容错**：具备异常恢复机制，单个采集源故障不影响整体服务；支持日志配置及多平台（Windows、Mac、Linux）部署。