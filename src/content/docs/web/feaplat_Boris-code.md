
---
title: feaplat
---

### [Boris-code feaplat](https://github.com/Boris-code/feaplat)  ![GitHub Repo stars](https://img.shields.io/github/stars/Boris-code/feaplat?style=social)

feaplat 是基于 Docker Swarm 的分布式爬虫管理系统，采用 Master 调度与 Worker 运行分离架构。
1. 支持任意 Python 脚本（如 feapder、scrapy）及浏览器渲染（Playwright、Selenium）。
2. 支持自动负载均衡、弹性伸缩、多实例分布式运行及 4 种定时启动方式。
3. Worker 节点随任务动态生成，完成后自动销毁，保障高稳定性。
4. 支持数据与请求监控，允许自定义监控内容及 Worker 运行环境镜像。
5. 提供项目、任务及实例日志的 Web 可视化管控。
6. 支持 Docker 一键部署，可动态扩展集群节点及私有项目 SSH 拉取。