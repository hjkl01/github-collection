
---
title: go-whatsapp-web-multidevice
---

### [aldinokemal go-whatsapp-web-multidevice](https://github.com/aldinokemal/go-whatsapp-web-multidevice)  ![GitHub Repo stars](https://img.shields.io/github/stars/aldinokemal/go-whatsapp-web-multidevice?style=social)

该项目是一个基于 Go 语言的 WhatsApp Web 多设备客户端（GoWA），旨在实现高效的内存使用。

**核心功能总结：**

1.  **多设备管理**：支持在单服务器实例中同时连接和管理多个 WhatsApp 账号，所有设备范围 API 调用需指定设备 ID。
2.  **消息通信**：提供 HTTP REST API 和 MCP（模型上下文协议），支持发送文本、媒体、贴纸、文件、联系人及位置消息，具备群组创建、成员管理及对话操作功能。
3.  **自动化交互**：内置自动回复、自动标记已读、自动下载媒体、自动拒接通话及连接状态（在线/离线）配置。
4.  **集成支持**：支持 Webhook 事件推送（含事件过滤与 HMAC 安全验证）、Chatwoot 客服系统集成以及 AI 工具的 MCP 服务器对接。
5.  **部署兼容性**：提供源码编译、Docker 容器及独立二进制文件部署方式，兼容 Linux、macOS、Windows 及 ARM/AMD 架构。
6.  **灵活配置**：支持通过命令行参数、环境变量或 .env 文件进行应用配置。