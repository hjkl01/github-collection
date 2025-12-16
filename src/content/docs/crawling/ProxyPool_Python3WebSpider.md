
---
title: ProxyPool
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/Python3WebSpider/ProxyPool?style=social) ](https://github.com/Python3WebSpider/ProxyPool)
### [Python3WebSpider ProxyPool](https://github.com/Python3WebSpider/ProxyPool)

**项目核心内容总结：**

**功能：**  
ProxyPool 是一个代理池工具，支持定时抓取免费代理网站、通过 Redis 存储和管理代理、定时测试代理可用性，并提供 API 接口获取有效代理。支持自定义爬虫扩展，可适配不同代理源。

**使用方法：**  
1. **Docker 方式**：通过 `docker-compose up` 启动 Redis 和 ProxyPool 容器，配置环境变量（如 Redis 地址、测试 URL 等）。  
2. **常规方式**：安装 Python 和 Redis，设置环境变量，运行 `pip install` 安装依赖，执行脚本启动服务。  

**主要特性：**  
- 通过 Redis 存储代理，支持多数据库和自定义键名；  
- 支持定时抓取（默认 100 秒）、测试（默认 20 秒）和 API 接口（默认端口 5555）；  
- 提供日志管理（支持文件记录、轮转、保留周期等）；  
- 可扩展爬虫：继承 `BaseCrawler` 类，定义 `urls` 和 `parse` 方法即可添加新代理源；  
- 支持 Kubernetes 部署。  

**注意事项：**  
免费代理可用性较低，不适合直接用于高要求场景，建议结合付费代理使用。