
---
title: webdis
---

### [nicolasff webdis](https://github.com/nicolasff/webdis)

**项目核心内容总结**：  
Webdis 是一个将 Redis 数据库功能通过 HTTP/WebSocket 暴露给客户端的工具，支持多种数据操作和格式输出。  

**功能与使用方法**：  
1. **HTTP 操作**：通过 URL 路径执行 Redis 命令（如 `/SET/key/value`），支持 `.raw` 后缀获取原始 Redis 协议输出，或通过 `?type=` 指定返回内容类型（如 JSON、TXT、PNG 等）。  
2. **文件上传**：使用 HTTP PUT 方法上传文件，如 `/SET/key` 将请求体作为值存储，并通过扩展名（如 `.png`）自动设置内容类型。  
3. **Pub/Sub 通信**：通过 HTTP 流式传输（chunked encoding）实时接收 Redis 通道消息，支持 JavaScript 等客户端订阅。  
4. **WebSocket 支持**：启用后可通过 `ws://.../.json` 或 `ws://.../.raw` 连接，发送 Redis 命令并接收响应，支持 JSON 或原始协议格式。  

**主要特性**：  
- 支持 Redis 常用命令（SET、GET、LPUSH 等）及文件存储。  
- 多格式输出（JSON、MSGPACK、TXT、HTML 等）及自定义分隔符。  
- WebSocket 实时交互，支持 JSON 和原始 Redis 协议。  
- 通过 `webdis.json` 配置启用 WebSocket、日志级别等参数。  
- 提供 ETag、内容类型自动识别、HTTP 状态码等完整 Web 功能。