
---
title: nginx-ui
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/schenkd/nginx-ui?style=social) ](https://github.com/schenkd/nginx-ui)
### [schenkd nginx-ui](https://github.com/schenkd/nginx-ui)

**核心内容总结：**  
该项目是一个基于Docker的Nginx配置管理工具，提供图形化界面（UI）供用户在线编辑和管理Nginx配置文件。  

**功能：**  
- 通过UI添加域名、编辑配置文件，支持保存、删除及启用/禁用操作。  
- 动态读取并同步宿主机`/etc/nginx`目录下的配置文件，实时反映手动新增文件。  

**使用方法：**  
- 使用Docker命令或Docker Compose部署，需挂载宿主机的`/etc/nginx`目录至容器，并映射端口（如8080）。  

**主要特性：**  
- 无需直接操作Nginx配置文件，简化协作流程。  
- 支持通过Nginx的Basic Auth机制实现访问认证（需额外配置`.htpasswd`文件及Nginx配置）。