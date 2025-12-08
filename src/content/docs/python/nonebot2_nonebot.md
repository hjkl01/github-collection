
---
title: nonebot2
---

### [nonebot nonebot2](https://github.com/nonebot/nonebot2)

**NoneBot2 核心内容总结：**

1. **项目功能**  
   NoneBot2 是一个基于 Python 的异步机器人框架，支持多平台（如 QQ、Telegram、B站等）和多协议（如 WebSocket、HTTP），通过适配器实现与不同平台的通信，提供事件处理、插件扩展等功能。

2. **使用方法**  
   - 安装 `pipx` 后通过 `nb-cli` 脚手架创建项目；
   - 执行 `nb run` 启动项目。

3. **主要特性**  
   - **异步处理**：基于 asyncio 实现高性能并发；
   - **插件系统**：支持官方及第三方插件扩展功能；
   - **多协议适配**：兼容多种平台协议（如 QQ、Telegram 等）；
   - **驱动框架支持**：集成 FastAPI、Quart、aiohttp 等主流框架；
   - **文档支持**：提供本地化文档插件（`nonebot_plugin_docs`）及社区资源。