
---
title: colly
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/gocolly/colly?style=social) ](https://github.com/gocolly/colly)
### [gocolly colly](https://github.com/gocolly/colly)

**项目核心内容总结：**  

**功能**：Colly 是一个为 Go 语言开发者设计的高效爬虫框架，支持网页数据抓取、结构化提取及多种应用场景（如数据挖掘、归档等）。  

**主要特性**：  
- 提供简洁的 API 接口；  
- 高性能（单核每秒可处理超 1000 次请求）；  
- 支持请求延迟控制、域名并发限制；  
- 自动处理 Cookie 和会话；  
- 支持同步/异步/并行抓取；  
- 内置缓存机制；  
- 自动识别非 Unicode 编码响应；  
- 遵循 robots.txt 协议；  
- 支持分布式爬虫；  
- 可通过环境变量配置；  
- 提供扩展功能。  

**使用方法**：  
通过 `go get github.com/gocolly/colly/v2` 安装。示例代码展示如何创建爬虫，提取链接并访问目标页面。  

**适用场景**：适用于需要高效抓取和处理网页数据的项目，如数据采集、分析、存档等。