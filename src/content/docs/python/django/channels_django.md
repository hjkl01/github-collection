
---
title: channels
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/django/channels?style=social) ](https://github.com/django/channels)
### [django channels](https://github.com/django/channels)

**Django Channels 核心内容总结：**

1. **项目功能**  
   Django Channels 扩展 Django，支持 WebSocket、长轮询 HTTP、任务卸载等异步功能，采用 Django 熟悉的设计模式，并提供灵活的底层框架以支持自定义协议和需求。

2. **使用方法**  
   - 通过 PyPI 安装 `channels` 包（需 Python 3.9+ 和 Django 4.2+）。  
   - 文档、安装指南和教程见 [Channels 官方文档](https://channels.readthedocs.io)。

3. **主要特性**  
   - 基于 ASGI（异步服务器网关接口）实现异步支持。  
   - 支持自定义协议及行为扩展。  
   - 与 Django 深度集成，提供 WebSocket 和 HTTP 长轮询等能力。

4. **相关项目**  
   - **Daphne**：WebSocket 和 HTTP 终端服务器。  
   - **channels_redis**：Redis 通道后端。  
   - **asgiref**：ASGI 基础库及内存后端。