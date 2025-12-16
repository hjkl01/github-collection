
---
title: cloudreve-docker
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/justxuewei/cloudreve-docker?style=social) ](https://github.com/justxuewei/cloudreve-docker)
### [justxuewei cloudreve-docker](https://github.com/justxuewei/cloudreve-docker)

**项目核心内容总结：**

**功能**  
基于最新Cloudreve V3的Docker镜像，提供文件管理与云存储服务，支持SQLite/MySQL等数据库，包含Nginx反向代理和Aria2离线下载的部署教程。

**使用方法**  
1. 创建配置目录并编辑`conf.ini`（示例：设置数据库路径）；  
2. 通过Docker命令启动容器，需挂载上传目录、配置文件夹、数据库目录及头像目录，设置PUID/PGID和时区；  
3. 首次启动后通过`docker logs`获取初始密码。

**主要特性**  
- 镜像体积小，纯净无多余组件；  
- 支持多架构（amd64/arm64/arm32）；  
- 提供详细部署教程（含Nginx/Aria2）；  
- 长期维护，适配最新Cloudreve版本。