
---
title: uptime-kuma
---

### [louislam uptime-kuma](https://github.com/louislam/uptime-kuma)

**项目核心内容总结：**

**功能**  
Uptime Kuma 是一款自托管的监控工具，支持 HTTP(s)/TCP/HTTP(s) 关键字/JSON 查询/WebSocket/Ping/DNS 记录/Push/Steam 游戏服务器/Docker 容器等多种监控类型，提供多语言支持、多状态页面、证书信息、代理支持及 2FA 安全验证。

**使用方法**  
1. **Docker 安装**  
   - Docker Compose：创建目录，下载 `compose.yaml`，执行 `docker compose up -d`。  
   - Docker 命令：运行 `docker run` 指令，映射端口和数据卷。  
2. **非 Docker 安装**：需 Node.js 20.4+、Git 和 pm2，执行 `git clone`、`npm run setup`，通过 `node server/server.js` 或 `pm2` 启动服务。

**主要特性**  
- 界面美观、响应迅速，支持 20 秒监控间隔。  
- 支持 90+ 通知服务（如 Telegram、Slack 等）。  
- 可创建多状态页面，将状态页面映射到特定域名。  
- 提供网络请求图表、证书信息及代理支持。  

**注意事项**  
- 不支持 NFS 文件系统，需使用本地目录或 Docker 卷。  
- 非 Docker 安装需特定平台（如 Linux、Windows 10/Server）。