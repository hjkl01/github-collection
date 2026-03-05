
---
title: crawlab
---

### [crawlab-team crawlab](https://github.com/crawlab-team/crawlab)  ![GitHub Repo stars](https://img.shields.io/github/stars/crawlab-team/crawlab?style=social)

Crawlab 是一个基于 Golang 的分布式 Web 爬虫管理平台，核心功能总结如下：

1. **多语言与框架兼容**：支持 Python、NodeJS、Go、Java、PHP 等多种编程语言，兼容 Scrapy、Puppeteer、Selenium 等爬虫框架，不限于单一技术栈。
2. **分布式架构管理**：采用主从架构（Master + Worker），Master 节点负责任务调度、节点管理及 API 服务，Worker 节点执行具体爬虫任务，支持横向扩展；配合 MongoDB 存储业务数据，SeaweedFS 存储文件与日志。
3. **全生命周期管理**：提供基于 Vue 3 的可视化前端界面，支持爬虫部署、任务调度（含 Cron）、任务日志监控、结果数据查看、节点管理及数据导出。
4. **便捷部署与集成**：支持 Docker Compose 一键部署，提供 SDK 方便爬虫程序接入并保存结果到数据库。