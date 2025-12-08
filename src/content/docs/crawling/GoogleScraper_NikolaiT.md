
---
title: GoogleScraper
---

### [NikolaiT GoogleScraper](https://github.com/NikolaiT/GoogleScraper)

**项目核心内容总结：**  
GoogleScraper 是一个用于爬取搜索引擎结果的 Python 工具，支持 Google、Bing、Yahoo 等主流搜索引擎，提供同步和异步两种模式。其主要功能包括：  
1. **多搜索引擎支持**：可爬取 Google、Bing、Yandex、Baidu 等平台的搜索结果，支持新闻、图片、视频等特殊搜索模式。  
2. **多线程/异步处理**：通过多线程和异步 IO 提高爬取效率，支持代理 IP（Socks5/Socks4/HttpProxy）以绕过反爬机制。  
3. **浏览器模拟**：使用 Selenium 模拟真实浏览器操作，避免被搜索引擎检测为爬虫。  
4. **命令行使用**：支持通过命令行指定关键词文件、搜索页数、爬取模式（如 `--scrape-method selenium`）等参数。  
5. **数据存储**：爬取结果以 SQLite 数据库形式保存，可通过 `--shell` 命令查看数据。  

**使用方法**：  
- 安装方式：通过 pip 安装或从 GitHub 克隆源码，需配置 Chrome/Firefox 浏览器驱动路径。  
- 命令行示例：`GoogleScraper --keyword-file keywords.txt --search-engine bing --num-pages-for-keyword 3`。  
- 异步模式：使用 `-m http` 参数触发低级 HTTP 请求模式，适用于简单爬取。  

**注意事项**：  
项目已不再维护，作者推荐使用基于 JavaScript 的 Puppeteer 项目作为替代方案。