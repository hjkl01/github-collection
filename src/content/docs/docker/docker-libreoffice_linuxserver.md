
---
title: docker-libreoffice
---

### [linuxserver docker-libreoffice](https://github.com/linuxserver/docker-libreoffice)

**项目核心内容总结：**

该项目是一个基于Selkies和Alpine Linux的Docker容器镜像，提供远程桌面服务，需通过HTTPS访问。主要功能包括：

1. **功能**  
   - 支持通过Docker部署远程桌面应用，提供图形界面访问。  
   - 集成Selkies（可能为VNC或类似远程控制方案），基于Alpine Linux精简系统。  
   - 强制要求HTTPS连接（自12.07.25版本起）。  

2. **使用方法**  
   - **部署方式**：通过Docker Compose或CLI命令运行容器，需映射端口（如3000:3000 HTTP、3001:3001 HTTPS）、设置环境变量（如PUID、PGID、TZ）、挂载配置目录（`/config`）。  
   - **参数配置**：支持通过环境变量调整用户权限、时区、HTTPS等，支持Docker Secrets从文件加载变量。  
   - **更新维护**：提供Docker Compose或CLI的更新流程，包括拉取镜像、重启容器及清理旧镜像。  

3. **主要特性**  
   - **轻量高效**：基于Alpine Linux，资源占用低。  
   - **灵活配置**：支持环境变量自定义用户权限、时区、HTTPS等，兼容Docker Mods扩展功能。  
   - **权限管理**：通过PUID/PGID避免挂载目录权限冲突，支持UMask设置。  
   - **日志与监控**：提供容器日志实时查看及版本查询方法。  

**版本更新**：持续优化基础镜像（如Alpine 3.22）、强制HTTPS、集成PWA图标等。