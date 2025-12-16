
---
title: overlord
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/bilibili/overlord?style=social) ](https://github.com/bilibili/overlord)
### [bilibili overlord](https://github.com/bilibili/overlord)

**Overlord** 是哔哩哔哩基于 Go 语言开发的缓存服务解决方案，提供 memcache 和 redis 集群的代理及自动化管理功能，核心特性包括：  
1. **代理模块（proxy）**：支持 memcache 和 redis 代理，兼容 redis-cluster 模式，可伪装成 cluster 模式运行，实现高可用缓存代理。  
2. **平台组件（platform）**：集成 API 服务器、Mesos 框架及任务管理功能，支持缓存节点的自动化管理。  
3. **可视化管理（GUI）**：提供 Web 界面，支持集群的创建、删除、扩缩容及节点管理等操作。  
4. **工具集**：包含 anzi（redis-cluster 数据同步工具）和 enri（redis-cluster 集群管理工具），支持集群操作与数据迁移。  
**使用方法**：通过 GUI 界面或 API 接口进行集群配置与管理，结合 Mesos 和 etcd 实现节点自动化调度，适用于生产环境的高可用缓存服务场景。