
---
title: crawlab
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/crawlab-team/crawlab?style=social) ](https://github.com/crawlab-team/crawlab)
### [crawlab-team crawlab](https://github.com/crawlab-team/crawlab)

**项目核心内容总结：**  
Crawlab 是一个基于 Go 语言的分布式网络爬虫管理平台，支持多种编程语言（如 Python、Java、Go 等）和爬虫框架（如 Scrapy、Puppeteer 等）。其核心功能包括：  
1. **任务管理**：提供图形化界面，支持爬虫任务调度、定时任务（Cron Job）、结果导出与分析。  
2. **分布式架构**：通过 Master 节点（任务调度）和 Worker 节点（任务执行）实现分布式爬虫，结合 SeaweedFS 文件系统和 MongoDB 存储数据。  
3. **灵活集成**：通过 SDK 提供的工具（如 `save_item` 方法）支持多种爬虫框架（如 Scrapy、通用 Python 爬虫）的数据保存，无需依赖特定技术栈。  
4. **便捷部署**：提供 Docker 部署方案，用户只需配置 `docker-compose.yml` 文件即可一键启动服务，无需手动安装依赖。  

**主要特性**：  
- 支持多语言、多框架，不限于 Python/Scrapy；  
- 提供在线代码编辑器、任务监控、通知提醒等管理功能；  
- 相比同类工具（如 ScrapydWeb、Gerapy），兼容性更广，性能更优；  
- 社区活跃，获 JetBrains 官方支持。