
---
title: goploy
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/zhenorzz/goploy?style=social) ](https://github.com/zhenorzz/goploy)
### [zhenorzz goploy](https://github.com/zhenorzz/goploy)

**核心内容总结：**  
Goploy 是一个基于 Web 的自动化部署工具，支持通过网页一键完成代码发布、回滚、监控和服务器管理。  

**功能：**  
- 支持 Git/SVN/FTP/SFTP 等多种版本控制和部署方式；  
- 跨操作系统部署；  
- 提供 RBAC 权限控制；  
- 支持 HTTP/TCP/Ping/进程/脚本/服务器监控；  
- 定时任务、终端交互（Xterm）、SFTP 和 LDAP 集成。  

**使用方法：**  
1. 通过 [Release](https://github.com/zhenorzz/goploy/releases) 下载安装包，或从源码构建；  
2. 运行生成的可执行文件（如 `./goploy`），通过浏览器访问 `http://ip:port`，初始账号密码为 `admin:admin!@#`。  

**主要特性：**  
- 提供完整的安装文档，易于上手；  
- 支持 Docker 部署（镜像地址：`zhenorzz/goploy`）；  
- 提供前端开发环境（Vue + NPM）和后端 Go 服务（需 Go 1.16+）；  
- 提供监控工具（Goploy-Agent）和开发插件（VSCode/JetBrains）。