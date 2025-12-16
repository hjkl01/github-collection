
---
title: beszel
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/henrygd/beszel?style=social) ](https://github.com/henrygd/beszel)
### [henrygd beszel](https://github.com/henrygd/beszel)

**Beszel 核心内容总结**  
Beszel 是一款轻量级服务器监控工具，支持 Docker 容器监控、历史数据记录、告警通知、多用户管理及 OAuth 认证。其核心功能包括：  
- **监控指标**：CPU、内存、磁盘、网络、负载、温度、GPU、电池、容器状态及 S.M.A.R.T. 硬盘健康数据。  
- **特性**：资源占用低、配置简单、支持自动备份（兼容 S3 存储）、多用户协作、集成 OAuth2 认证。  
- **架构**：由 **Hub**（基于 PocketBase 的 Web 管理界面）和 **Agent**（部署于被监控系统的数据采集组件）组成。  
- **使用方法**：通过 [Beszel 官方文档](https://beszel.dev) 的快速入门指南部署，支持 Docker 部署及 API 调用。  
- **开源许可**：采用 MIT 开源协议。  

**主要适用场景**：适用于需要轻量级监控、多用户协作及自动化告警的服务器和容器环境。