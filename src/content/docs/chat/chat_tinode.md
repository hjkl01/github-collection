
---
title: chat
---

### [tinode chat](https://github.com/tinode/chat)

**项目核心内容总结：**  
Tinode 是一个使用 Go 语言开发的即时通讯后端服务器，支持 Android、iOS、Web 等多平台客户端及 gRPC 接口。主要功能包括一对一/群组聊天、视频通话、消息同步、频道管理、访问控制、多语言支持等。  

**使用方法：**  
通过 `INSTALL.md` 文档安装，支持 Docker 部署。  

**主要特性：**  
1. **多平台支持**：兼容 Android、iOS、Web 及多种编程语言（如 Java、Swift、Python 等）。  
2. **消息管理**：支持大文件存储（本地或 S3）、消息持久化、多数据库后端（MySQL、PostgreSQL、MongoDB 等）。  
3. **扩展性**：可配置媒体处理、数据库适配器，支持协议选择（JSON 或 Protobuf）。  
4. **国际化**：提供中文、英文、俄语、西班牙语等多语言支持，部分语言可由社区贡献。  

**计划功能**：  
包括联邦通信、位置共享、端到端加密、消息搜索等。  

**其他**：  
部分图形资源采用开源许可，支持第三方适配器（如 ArangoDB、DynamoDB）。