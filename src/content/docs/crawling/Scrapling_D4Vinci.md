
---
title: Scrapling
---

### [D4Vinci Scrapling](https://github.com/D4Vinci/Scrapling)  ![GitHub Repo stars](https://img.shields.io/github/stars/D4Vinci/Scrapling?style=social)

Scrapling 是一个现代化的自适应网页抓取 Python 框架，支持从单次请求到全规模爬取的全流程任务。

**核心功能：**
1.  **自适应解析**：智能感知网站结构变化，自动重新定位目标元素，确保抓取数据在网页改版后依然有效。
2.  **高级抓取**：内置反爬绕过能力（如 Cloudflare Turnstile），支持 HTTP 请求及动态浏览器自动化（Playwright/Chrome），提供会话管理与代理轮换。
3.  **爬虫框架**：提供类 Scrapy 的 Spider API，支持并发爬取、多会话路由、断点续传、流式输出及自动检测被屏蔽请求。
4.  **AI 集成**：内置 MCP 服务器，支持利用 AI 辅助进行定向内容提取，降低 token 使用成本。
5.  **工具支持**：提供命令行接口 (CLI) 和交互式 Shell，方便直接提取数据，支持 Docker 部署。
6.  **性能优化**：高性能解析引擎，低内存占用，JSON 序列化速度快。