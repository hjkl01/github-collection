
---
title: docker-webtop
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/linuxserver/docker-webtop?style=social) ](https://github.com/linuxserver/docker-webtop)
### [linuxserver docker-webtop](https://github.com/linuxserver/docker-webtop)

**核心内容总结：**  

**项目功能**  
该项目是一个基于Selkies的Webtop桌面环境Docker镜像，支持通过Web浏览器远程访问桌面应用，提供多种Linux发行版（如Alpine、Debian、Fedora等）的镜像选择，适用于远程办公、开发测试等场景。  

**使用方法**  
1. **部署方式**：通过Docker Compose或`docker run`命令启动容器，需设置用户ID（PUID）、组ID（PGID）、时区（TZ）等环境变量，并挂载配置目录（`/config`）。  
2. **配置优化**：建议设置共享内存（`--shm-size`）以提升性能，支持通过文件或Docker Secrets设置环境变量。  
3. **更新维护**：提供Docker Compose和Docker Run的容器更新方法，支持Diun工具实现镜像更新通知。  

**主要特性**  
- **多系统支持**：兼容Alpine、Debian、Fedora、Ubuntu等多种Linux发行版，定期更新基础镜像版本。  
- **扩展功能**：支持Docker Mods（如GPU/Nvidia）、PWA图标、本地化语言等，提供构建自定义镜像的脚本。  
- **权限管理**：通过PUID/PGID解决宿主机与容器目录权限冲突，支持umask设置文件权限。  
- **日志与监控**：提供容器日志实时查看、版本查询及容器状态管理功能。