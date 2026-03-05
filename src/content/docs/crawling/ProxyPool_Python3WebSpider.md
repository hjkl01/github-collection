
---
title: ProxyPool
---

### [Python3WebSpider ProxyPool](https://github.com/Python3WebSpider/ProxyPool)  ![GitHub Repo stars](https://img.shields.io/github/stars/Python3WebSpider/ProxyPool?style=social)

ProxyPool 是一个简易高效的代理池项目，核心功能如下：
1. **代理获取**：定时抓取免费代理网站，支持通过扩展爬虫简单添加新源。
2. **代理存储**：使用 Redis 存储代理池，并对代理可用性进行排序。
3. **代理筛选**：定时测试和筛选，自动剔除不可用代理，保留可用代理。
4. **服务提供**：提供 HTTP API 接口，支持随机获取测试通过的可用代理。

项目支持 Docker 及 Python 环境运行，架构包含 Getter（抓取）、Tester（测试）、Server（服务）三个模块。可通过环境变量灵活配置 Redis 连接、运行周期、测试 URL 等参数，并允许在 crawlers 目录下扩展自定义爬虫源。