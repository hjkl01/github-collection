
---
title: gochat
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/LockGit/gochat?style=social) ](https://github.com/LockGit/gochat)
### [LockGit gochat](https://github.com/LockGit/gochat)

**gochat核心内容总结**  

**项目功能**：gochat是一个基于Go语言开发的轻量级即时通讯系统，支持私信聊天、房间广播消息、WebSocket和TCP协议接入，并实现跨协议消息互通。系统采用模块化设计，包含逻辑层（logic）、连接层（connect）、任务层（task）、API层和站点层，各模块通过RPCX通信，支持水平扩展。  

**主要特性**：  
- 使用etcd实现服务发现，支持动态扩容；  
- 消息存储与投递基于Redis（可替换为Kafka/RabbitMQ），保证高并发下的消息可靠性；  
- 提供Docker一键部署方案，支持快速搭建聊天室环境；  
- 数据库使用SQLite3（支持替换为MySQL等），存储用户基础信息；  
- 消息ID采用Snowflake算法生成，理论QPS达409.6万/秒；  
- 支持前端UI访问，可多账号登录测试聊天功能。  

**使用方法**：  
1. **Docker部署**：拉取镜像后执行`run.sh`脚本，无需手动编译，自动启动各模块；  
2. **手动安装**：依次启动logic、connect（WebSocket/TCP）、task、api和site模块，确保etcd、Redis服务已运行；  
3. **访问方式**：通过浏览器访问`http://IP:8080`登录聊天室，使用预设账号（如demo/test/admin，密码均为111111）进行测试。  

**其他**：项目提供开源License（MIT），支持通过JetBrains赞助计划获取开发工具授权。