
---
title: nginx-proxy-manager
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/NginxProxyManager/nginx-proxy-manager?style=social) ](https://github.com/NginxProxyManager/nginx-proxy-manager)
### [NginxProxyManager nginx-proxy-manager](https://github.com/NginxProxyManager/nginx-proxy-manager)

Nginx Proxy Manager 是一个基于 Docker 的反向代理管理工具，提供可视化界面简化 SSL 证书配置和网站流量转发。核心功能包括：  
1. **主要特性**  
- 提供图形化管理界面，无需 Nginx 或 Let's Encrypt 知识即可配置域名转发、重定向、SSL 证书等  
- 支持自动获取 Let's Encrypt 免费 SSL 证书或自定义证书  
- 包含访问控制、HTTP 认证、用户权限管理和操作日志功能  
- 允许高级用户自定义 Nginx 配置  

2. **使用方法**  
- 安装 Docker 和 Docker Compose  
- 创建包含镜像配置、端口映射（80/81/443）和数据卷的 docker-compose.yml 文件  
- 运行 `docker compose up -d` 启动容器，通过 `http://IP:81` 访问管理界面  
- 配置家庭网络需在路由器端口转发 80/443 到本机，并绑定域名  

3. **适用场景**  
适合需要为本地服务（如家庭服务器）提供 HTTPS 访问的用户，简化反向代理和 SSL 配置流程。