
---
title: crawlee-python
---

### [apify crawlee-python](https://github.com/apify/crawlee-python)

Crawlee 是一个用于网络爬取和浏览器自动化的 Python 库，提供高效、可靠的爬虫构建方案。其核心功能包括：  
1. **两种爬虫模式**：  
   - `BeautifulSoupCrawler`：基于 HTTP 请求和 HTML 解析（使用 BeautifulSoup），适合静态页面，性能高效。  
   - `PlaywrightCrawler`：基于 Playwright 控制无头浏览器，支持 JavaScript 渲染和动态内容交互。  

2. **安装方法**：  
   - 通过 PyPI 安装：`pip install 'crawlee[all]'` 并执行 `playwright install`。  
   - 使用 Crawlee CLI 创建模板项目：`uvx 'crawlee[cli]' create my-crawler`。  

3. **主要特性**：  
   - 统一接口管理 HTTP 请求和浏览器操作。  
   - 自动重试、代理轮换、请求队列持久化。  
   - 异步处理（基于 Asyncio），支持类型提示提升开发体验。  
   - 数据存储灵活（支持表格数据和文件存储）。  

适用于需要处理静态或动态网页数据提取的场景，文档和示例可参考 [Crawlee 官网](https://crawlee.dev/python/)。