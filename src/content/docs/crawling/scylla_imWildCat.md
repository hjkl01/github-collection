
---
title: scylla
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/imWildCat/scylla?style=social) ](https://github.com/imWildCat/scylla)
### [imWildCat scylla](https://github.com/imWildCat/scylla)

Scylla 是一个智能代理池工具，用于从互联网抓取内容并构建大型语言模型。其核心功能包括：自动爬取和验证代理IP、提供JSON API接口、支持网页界面（可查看代理IP地理分布等信息）、集成Scrapy和requests库（仅需一行代码）、内置HTTP转发代理服务器。  

**使用方法**：  
1. **安装**：推荐使用Docker（`docker run`命令），或通过pip安装（`pip install scylla`），也可从源码安装。  
2. **访问API**：通过`http://localhost:8899/api/v1/proxies`获取代理IP列表，支持分页、匿名性、HTTPS协议、国家筛选等参数。  
3. **使用代理服务器**：默认在8081端口启动HTTP转发代理，可用`curl -x http://127.0.0.1:8081`或`requests`库调用。  
4. **网页界面**：访问`http://localhost:8899`查看代理列表及全球地理分布地图。  

**主要特性**：  
- 一键启动，无需复杂配置；  
- 支持多种爬虫框架集成；  
- 提供系统统计信息（如代理延迟、有效性等）；  
- 开源协议为Apache 2.0。