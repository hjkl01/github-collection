
---
title: feaplat
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/Boris-code/feaplat?style=social) ](https://github.com/Boris-code/feaplat)
### [Boris-code feaplat](https://github.com/Boris-code/feaplat)

**核心内容总结：**  
FEAPLAT是一款基于Docker的爬虫管理系统，支持多种爬虫框架（如feapder、scrapy）和浏览器渲染，具备任务管理、监控、集群部署、弹性伸缩等功能。主要特性包括：支持动态生成Worker节点、任务隔离、自动负载均衡、自定义监控、Docker一键部署及集群扩展。  

**使用方法：**  
1. 安装Docker及Swarm，配置docker-compose启动服务。  
2. 访问默认地址（http://localhost），使用admin/admin登录。  
3. 通过添加服务器节点实现集群扩展，支持私有项目配置（需添加SSH密钥）。  
4. 自定义爬虫镜像时，修改.env文件中的SPIDER_IMAGE参数。  

**核心特性：**  
- 支持多框架、浏览器渲染及有头模式；  
- 动态生成Worker节点，任务隔离，稳定性高；  
- 自定义监控、弹性伸缩、集群管理；  
- Docker一键部署，支持私有项目与镜像定制。