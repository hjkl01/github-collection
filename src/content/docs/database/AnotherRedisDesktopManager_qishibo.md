
---
title: AnotherRedisDesktopManager
---

### [qishibo AnotherRedisDesktopManager](https://github.com/qishibo/AnotherRedisDesktopManager)

**项目核心内容总结：**

Another Redis Desktop Manager 是一款功能强大的 Redis 图形化管理工具，支持连接 Redis 服务器、集群、哨兵模式，提供以下核心功能：  
1. **多连接方式**：支持 SSH 隧道、SSL 加密、集群、哨兵模式连接，可自定义主机、端口、认证信息等参数。  
2. **自定义数据查看器**：允许用户通过脚本（如 Python、Shell）解析和显示 Redis 中的二进制、Pickle 等特殊格式数据。  
3. **命令行启动**：支持通过 CLI 参数快速连接 Redis，如指定主机、端口、认证、集群模式等。  
4. **跨平台支持**：提供 Windows、Mac、Linux 的桌面客户端构建方式，支持通过 npm 脚本进行开发和打包。  
5. **特色功能**：暗色模式、自动更新、支持多种数据格式（Hash、Set、Zset 等）的搜索与查看。  

**使用方法**：  
- 图形界面：通过配置连接参数（如主机、端口、SSH、SSL）连接 Redis。  
- 命令行：使用 `--host`、`--port`、`--cluster` 等参数启动应用并连接。  
- 开发构建：克隆代码后通过 `npm install` 安装依赖，使用 `npm start` 启动开发服务器，`npm run electron` 构建桌面客户端。  

**主要特性**：  
- 支持 Redis 集群、哨兵、SSH 隧道、SSL 加密连接。  
- 提供自定义脚本解析非标准数据格式（如二进制、Pickle）。  
- 支持跨平台打包（Windows、Mac、Linux）。  
- 暗色模式、自动更新、命令行参数启动等便捷功能。