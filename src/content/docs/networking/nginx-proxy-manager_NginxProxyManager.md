
---
title: nginx-proxy-manager
---

### [NginxProxyManager nginx-proxy-manager](https://github.com/NginxProxyManager/nginx-proxy-manager)

**核心内容总结：**

**项目功能**  
Nginx Proxy Manager 是一个基于 Docker 的反向代理管理工具，可自动配置 SSL 证书（支持 Let's Encrypt 或自定义证书），无需深入了解 Nginx 或证书管理，适用于家庭网络或小型服务部署。

**使用方法**  
1. 安装 Docker 和 Docker-Compose。  
2. 创建 `docker-compose.yml` 文件，配置端口映射（80、443、81）及数据卷（用于存储配置和证书）。  
3. 运行 `docker compose up -d` 启动容器。  
4. 通过 `http://<服务器IP>:81` 访问管理界面，添加域名、配置转发规则等。

**主要特性**  
- 提供基于 Tabler 框架的图形化管理界面  
- 支持自动获取 Let's Encrypt 证书或手动上传自定义 SSL 证书  
- 可设置访问控制列表、HTTP 基本认证、404 页面等  
- 允许高级用户自定义 Nginx 配置  
- 包含用户权限管理和操作审计日志  
- 通过路由器端口转发和域名解析（如 DuckDNS）实现公网访问