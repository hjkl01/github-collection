
---
title: chanify
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/chanify/chanify?style=social) ](https://github.com/chanify/chanify)
### [chanify chanify](https://github.com/chanify/chanify)

**项目核心内容总结：**

Chanify 是一个跨平台的消息推送工具，支持通过命令行、浏览器扩展、Windows 客户端等方式发送文本、图片、音频、链接及自定义操作指令到设备。其核心功能包括：

1. **消息发送**  
   支持多种格式消息（文本/图片/音频/链接）发送，可通过 CLI、浏览器插件、Windows 右键菜单等途径操作，消息可配置声音提醒、中断级别等参数。

2. **服务端部署**  
   提供可自托管的 Node 服务，支持 Docker 部署，配置包括监听地址、端口、数据库连接（MySQL）、SSL 证书等，支持用户注册白名单、私有服务器设置。

3. **高级功能**  
   - 自定义操作指令（如脚本执行）  
   - 支持 Lua 插件扩展（如 GitHub Webhook 事件处理）  
   - 支持 Token 管理（有效期可配置，泄露后可加入黑名单）  
   - 多平台兼容（Windows、Chrome 浏览器、移动端等）

4. **使用方法**  
   - 通过 CLI 命令发送消息（如 `chanify send --token <token> --text "测试"`）  
   - 浏览器安装扩展，选中内容右键发送  
   - Windows 客户端集成到“发送到”菜单  
   - Docker 部署需配置 `docker-compose.yml` 文件  

5. **特性**  
   - 轻量级服务端，支持高并发  
   - 安全机制（Token 有效期、白名单、黑名单）  
   - 可扩展插件系统（Lua 脚本）  
   - 支持 HTTPS 和自定义域名  

**注意事项：**  
- Token 需妥善保管，泄露后可通过服务端加入黑名单。  
- 私有服务器需关闭用户注册并设置白名单。  
- Docker 部署需配置反向代理（如 Nginx）及 SSL 证书。