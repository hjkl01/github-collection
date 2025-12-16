
---
title: Scraperr
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/jaypyles/Scraperr?style=social) ](https://github.com/jaypyles/Scraperr)
### [jaypyles Scraperr](https://github.com/jaypyles/Scraperr)

**项目核心内容总结：**

**功能**  
Scraperr 是一个无需编写代码即可完成网页数据抓取的自托管工具，支持通过 XPath 精准提取页面元素、管理抓取任务队列、自动下载媒体文件，并提供数据表格可视化及导出（Markdown/CSV）功能。

**主要特性**  
- 支持域名内所有页面爬取  
- 自定义请求头与反爬策略  
- 多渠道通知任务完成状态  
- 提供可视化界面与结构化数据展示  

**使用方法**  
- 通过 Docker 部署：执行 `make up`  
- Helm 部署：参考官方文档指引  

**注意事项**  
- 必须遵守目标网站的 `robots.txt` 规则及服务条款  
- 需合理设置请求间隔，避免服务器过载  
- 仅限用于允许抓取的网站，开发者不承担滥用责任  

**其他**  
- 开源协议：MIT  
- 社区支持：可通过 Discord 参与交流（链接见原文）