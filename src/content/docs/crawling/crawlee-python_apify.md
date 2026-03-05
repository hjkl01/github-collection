
---
title: crawlee-python
---

### [apify crawlee-python](https://github.com/apify/crawlee-python)  ![GitHub Repo stars](https://img.shields.io/github/stars/apify/crawlee-python?style=social)

Crawlee 是一个 Python 网页爬取和浏览器自动化库，旨在帮助用户快速构建可靠的爬虫应用。

核心功能：
1. **爬虫类型**：提供 `BeautifulSoupCrawler`（基于 HTTP，适合静态 HTML 高效提取）和 `PlaywrightCrawler`（基于无头浏览器，适合动态 JavaScript 页面）两种模式。
2. **抗反爬能力**：默认配置下可模拟人类行为，绕过现代反机器人保护，支持自动重试、代理轮换和会话管理。
3. **资源管理**：基于 Asyncio 实现自动并行爬取，支持持久化的 URL 队列和请求路由配置。
4. **数据存储**：集成可扩展的存储功能，支持将爬取数据持久化保存为数据集或键值存储。
5. **开发体验**：提供完整的类型提示，支持任务中断后的状态持久化，提供 CLI 工具快速初始化项目，并支持部署至 Apify 平台。