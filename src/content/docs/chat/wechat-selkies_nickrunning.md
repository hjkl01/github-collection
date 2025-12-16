
---
title: wechat-selkies
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/nickrunning/wechat-selkies?style=social) ](https://github.com/nickrunning/wechat-selkies)
### [nickrunning wechat-selkies](https://github.com/nickrunning/wechat-selkies)

**项目核心内容总结：**

**功能**  
基于 Docker 的微信/QQ Linux 客户端，通过 Selkies WebRTC 技术实现浏览器直接访问，无需本地安装客户端，适用于服务器部署和远程办公。

**使用方法**  
1. **快速部署**：使用 Docker 命令或 docker-compose.yml 文件启动容器，映射端口并挂载配置目录。  
2. **访问方式**：通过浏览器访问 `https://<服务器IP>:3001`。  
3. **源码部署**：克隆项目后通过 docker-compose 启动服务。

**主要特性**  
- 浏览器访问微信/QQ，支持中文输入法和本地化  
- Docker 容器化部署，支持 AMD64/ARM64 架构  
- 数据持久化存储（配置/聊天记录）  
- 可选 GPU 硬件加速  
- 自动启动微信/QQ（可配置）  
- 支持文件传输、图片复制、窗口切换器等  
- 升级时需清空 `./config/.config/openbox` 目录（如功能缺失）  

**配置说明**  
支持自定义用户名、密码、时区、自动启动设置等，通过 docker-compose.yml 中的环境变量配置。