
---
title: Scrapling
---

### [D4Vinci Scrapling](https://github.com/D4Vinci/Scrapling)  ![GitHub Repo stars](https://img.shields.io/github/stars/D4Vinci/Scrapling?style=social)

Scrapling 是一个现代、强大的网页抓取框架，支持从单个请求到大规模爬取的全方位功能。其核心特点包括：

---

### 项目功能

- **网页抓取与解析**：支持 CSS/XPath 等多种选择器，自动适应网页结构变化。
- **反爬绕过**：内置 StealthyFetcher，可绕过 Cloudflare 等常见反爬系统。
- **浏览器自动化**：支持 Playwright 和 Chrome，适用于动态加载网页。
- **爬虫框架**：Scrapy 风格的 Spider API，支持并发爬取、会话管理、暂停/恢复。
- **代理轮换**：支持代理自动切换，可配置轮换策略。
- **MCP 服务器**：集成 AI 支持，用于智能数据提取和处理。
- **CLI 工具**：无需编写代码即可直接从命令行抓取网页内容。

---

### 使用方法

1. **简单抓取**：
   ```python
   from scrapling.fetchers import Fetcher
   page = Fetcher.get('https://example.com')
   data = page.css('.product::text').getall()
   ```

2. **爬虫示例**：
   ```python
   from scrapling.spiders import Spider, Response

   class MySpider(Spider):
       name = "demo"
       start_urls = ["https://example.com/"]

       async def parse(self, response: Response):
           for item in response.css('.product'):
               yield {"title": item.css('h2::text').get()}
   
   MySpider().start()
   ```

3. **命令行使用**：
   ```bash
   scrapling extract get 'https://example.com' output.txt --css-selector '#content'
   ```

---

### 主要特性

- **自适应解析**：智能识别网页结构变化，自动定位元素。
- **多会话支持**：支持多种抓取方式（HTTP、Stealthy、Dynamic）在同一个爬虫中切换。
- **性能优秀**：比多数 Python 抓取库快 10 倍以上。
- **暂停/恢复**：支持爬取过程保存和恢复。
- **类型提示完整**：IDE 支持良好，开发体验佳。
- **Docker 支持**：提供包含所有浏览器的镜像。

---

### 安装方式

```bash
pip install scrapling
```

可选依赖：
- `pip install "scrapling[fetchers]"`：安装抓取功能
- `pip install "scrapling[shell]"`：安装 CLI 工具
- `pip install "scrapling[all]"`：安装全部功能

---

### 性能表现

- **文本提取速度**：比 PyQuery 快 12 倍，比 BeautifulSoup 快 700 倍以上。
- **元素相似性查找**：比 AutoScraper 快 5 倍。

---

Scrapling 适合需要高效、稳定、智能抓取的开发者，尤其适用于处理现代网页中的动态内容和反爬机制。