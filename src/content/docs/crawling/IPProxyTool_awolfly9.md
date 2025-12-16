
---
title: IPProxyTool
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/awolfly9/IPProxyTool?style=social) ](https://github.com/awolfly9/IPProxyTool)
### [awolfly9 IPProxyTool](https://github.com/awolfly9/IPProxyTool)

**项目核心内容总结：**

**功能：**  
使用Scrapy爬虫抓取多个免费代理网站，过滤有效代理IP并存入MySQL数据库，提供接口获取可用代理IP。

**使用方法：**  
1. 环境要求：Python3 + MySQL，安装依赖包（`pip install -r requirements.txt`）。  
2. 配置MySQL数据库，导入数据表结构（`source '/项目目录/db.sql'`）。  
3. 修改`config.py`中的数据库用户名、密码及服务器端口。  
4. 运行主脚本抓取代理IP（`python ipproxytool.py`）或异步验证模式（`python ipproxytool.py async`）。  
5. 通过HTTP接口（如`http://127.0.0.1:8000/select`）筛选、获取、删除或插入代理IP数据。

**主要特性：**  
- 支持抓取国内外多个代理网站（如快代理、IP181等）。  
- 提供多级验证机制（通过httpbin检测HTTPS支持、匿名度，再访问目标网站验证有效性）。  
- 支持异步验证、多进程处理。  
- 提供RESTful接口管理代理IP（筛选、删除、插入）。  
- 支持Docker部署。