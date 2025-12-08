
---
title: MediaCrawler
---

### [NanmiCoder MediaCrawler](https://github.com/NanmiCoder/MediaCrawler)

**项目核心内容总结：**

1. **项目功能**  
   - 多平台数据爬取：支持小红书、抖音、快手、B站、微博、知乎等主流自媒体平台，可抓取帖子信息、评论（含二级评论）、用户数据等。  
   - 数据存储：支持CSV、JSON、Excel、SQLite、MySQL等多种格式存储。  
   - 附加功能：生成评论词云图，支持IP代理池和登录态缓存。  

2. **主要特性**  
   - 技术实现：基于Playwright框架，无需JS逆向，通过模拟登录获取签名参数，降低开发门槛。  
   - 灵活性：提供配置文件（`config/base_config.py`）自定义功能（如是否启用评论抓取）。  
   - 进阶版本（MediaCrawlerPro）：支持断点续爬、多账号管理、脱离Playwright依赖、Linux环境适配等优化。  

3. **使用方法**  
   - 依赖安装：需安装Python、uv（或pip）、Node.js及Playwright浏览器驱动。  
   - 运行命令：通过`python main.py`或`python3 main.py`启动，参数指定平台、模式（如`--type search`关键词搜索或`--type detail`指定帖子ID）。  
   - 验证方式：使用二维码登录验证（`--lt qrcode`参数）。  

4. **注意事项**  
   - **仅限学习用途**：明确禁止用于商业或非法活动，开发者不承担因违规使用导致的法律风险。  
   - **文档支持**：提供详细数据存储指南及项目文档链接（[MediaCrawler 完整文档](https://nanmicoder.github.io/MediaCrawler/)）。  

**其他**：项目包含开源教程（如[CrawlerTutorial](https://github.com/NanmiCoder/CrawlerTutorial)）及合作推广渠道（如TikHub数据接口服务）。