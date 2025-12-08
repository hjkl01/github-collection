
---
title: Gerapy
---

### [Gerapy Gerapy](https://github.com/Gerapy/Gerapy)

**核心内容总结：**

1. **项目功能**  
   Gerapy 是基于 Scrapy、Scrapyd 等技术的分布式爬虫管理框架，提供可视化配置、项目管理、任务调度、爬虫部署与监控等功能，支持通过 Web 界面管理爬虫项目和任务。

2. **使用方法**  
   - 安装：`pip3 install gerapy`  
   - 初始化工作区：`gerapy init [工作区名称]`  
   - 数据库迁移：`gerapy migrate`  
   - 创建管理员账户：`gerapy createsuperuser`  
   - 启动服务：`gerapy runserver [IP:端口]`  
   - Docker 部署：`docker-compose up` 或指定镜像运行。

3. **主要特性**  
   - 可视化配置爬虫（含网页预览）  
   - Scrapyd 与 Gerapy 认证管理  
   - 定时任务调度  
   - 支持拖拽 Scrapy 项目到指定目录自动识别  
   - 提供部署、监控、日志管理等完整流程  

4. **待完善功能**  
   - Scrapy 可视化配置  
   - 网页智能分析功能（开发中）