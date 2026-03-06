
---
title: ProxyPool
---

### [Python3WebSpider ProxyPool](https://github.com/Python3WebSpider/ProxyPool)  ![GitHub Repo stars](https://img.shields.io/github/stars/Python3WebSpider/ProxyPool?style=social)

ProxyPool 是一个简易高效的代理池系统，核心功能包括：定时抓取免费代理网站并支持自定义扩展爬虫；使用 Redis 存储代理并对可用性排序；定时测试筛选代理，自动剔除不可用代理；提供 API 随机获取测试通过的可用代理。项目支持 Docker 和 Python + Redis 环境运行，可通过环境变量配置连接参数、测试策略及代理源，并支持 Kubernetes 部署。