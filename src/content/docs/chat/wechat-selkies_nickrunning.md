
---
title: wechat-selkies
---

### [nickrunning wechat-selkies](https://github.com/nickrunning/wechat-selkies)

**项目核心内容总结：**

**项目功能**  
基于Docker的微信/QQ Linux客户端，通过Selkies WebRTC技术实现浏览器直接访问，无需本地安装客户端，适用于服务器部署和远程办公场景。

**主要特性**  
- 浏览器访问微信/QQ（支持Chrome/Firefox等现代浏览器）  
- Docker容器化部署，支持AMD64和ARM64架构  
- 数据持久化存储（配置/聊天记录）  
- 中文支持及本地输入法兼容  
- 支持图片复制、文件传输、硬件加速（GPU）  
- 自动启动微信/QQ（可配置）  
- 窗口切换器（便于后台窗口管理）  

**使用方法**  
1. **环境要求**：Docker、Docker Compose、支持WebRTC的浏览器  
2. **快速部署**：  
   - 直接运行Docker镜像（支持Docker Hub和GitHub Container Registry）  
   - 使用`docker-compose.yml`配置文件部署（含端口映射、数据卷、环境变量等）  
3. **访问方式**：通过HTTPS访问`https://<服务器IP>:3001`  

**注意事项**  
- 升级后若功能异常，需清空挂载目录下的`openbox`文件夹  
- 硬件加速需映射`/dev/dri`设备  
- 支持自定义用户名、密码、时区等环境变量  

**许可证**  
采用MIT开源协议，项目基于LinuxServer.io的Selkies基础镜像构建。