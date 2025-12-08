
---
title: medis
---

### [luin medis](https://github.com/luin/medis)

### 核心内容总结

**项目功能**  
Medis 是一款基于 Electron、React 和 Redux 构建的 Redis 图形化管理工具，支持键值查看/编辑、SSH 隧道连接远程服务器、终端执行命令、配置管理等基础功能。高级功能包括 JSON/MessagePack 格式支持、处理百万级键不阻塞 Redis 服务器、模式管理器等。Medis 2 版本新增树形视图、暗黑模式、流和警报模式等功能。

**使用方法**  
- **下载**：Windows 用户可从发布页面下载安装包，Mac 用户可从 App Store 或 GitHub 发布页获取。  
- **本地运行**：通过 `npm install` 安装依赖，执行 `npm run pack` 编译资源，最后用 `npm start` 启动。  
- **连接 Heroku**：通过 `heroku redis:credentials` 获取 Redis 凭证，输入主机、端口和密码完成连接。

**主要特性**  
- 支持 Redis 2.8 及以上版本（依赖 `SCAN` 命令）。  
- Medis 2 版本为原生技术重写，界面更现代、响应更快。  
- 提供免费下载（Mac App Store 可购付费版，含自动更新功能）。