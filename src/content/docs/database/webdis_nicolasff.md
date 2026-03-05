
---
title: webdis
---

### [nicolasff webdis](https://github.com/nicolasff/webdis)  ![GitHub Repo stars](https://img.shields.io/github/stars/nicolasff/webdis?style=social)

Webdis 是一个为 Redis 提供 HTTP 接口的轻量级 Web 服务器。它支持通过 HTTP 方法（GET、POST、PUT）执行 Redis 命令，输出格式包括默认 JSON、JSONP、RAW 协议、MessagePack 及自定义类型。主要功能特性包括：

1. **连接与认证**：支持连接 Redis 的 TCP 或 Unix Socket，提供 SSL/TLS 加密连接、Redis 密码及用户名认证、IP 范围限制和 HTTP Basic Auth。
2. **高级功能**：支持多线程处理、HTTP 1.1 流水线、WebSocket 通信、Pub/Sub 服务及文件上传。
3. **配置与管理**：采用 JSON 配置文件，支持环境变量注入，可配置日志持久化策略及权限控制列表（ACL）。
4. **部署方式**：支持源码编译构建（含 Docker 文件）及 Docker 镜像部署，镜像可选包含嵌入式 Redis 实例以便快速测试。