
---
title: open-im-server
---

### [openimsdk open-im-server](https://github.com/openimsdk/open-im-server)

**项目核心内容总结：**

**项目功能**  
OpenIM 是一个开源的即时通讯解决方案，包含 OpenIM SDK 和 OpenIM Server 两部分。  
- **OpenIM SDK**：为客户端应用提供即时通讯功能集成，支持消息收发、用户管理、群组管理、会话处理等模块，基于 Golang 开发，支持跨平台部署。  
- **OpenIM Server**：采用微服务架构，支持集群模式、大规模用户（百万级用户、亿级消息）及多种部署方式（源码、Kubernetes、Docker）。提供 REST API 和 Webhooks 扩展业务功能（如群组创建、消息推送）。  

**使用方法**  
- 在线体验：通过 [OpenIM Online Demo](https://www.openim.io/en/commercial) 快速体验。  
- 部署方式：  
  - [源码部署](https://docs.openim.io/guides/gettingStarted/imSourceCodeDeployment)  
  - [Docker 部署](https://docs.openim.io/guides/gettingStarted/dockerCompose)  

**主要特性**  
1. **高扩展性**：微服务架构支持集群部署，适配大规模用户场景。  
2. **多平台支持**：兼容 Linux、Windows、Mac 系统及 ARM/AMD 架构。  
3. **灵活集成**：提供 REST API 和 Webhooks 接口，便于业务系统扩展。  
4. **跨平台 SDK**：OpenIM SDK 支持多端集成，包含本地存储、连接管理、回调监听等功能。