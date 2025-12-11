
---
title: docker-headless-vnc-container
---

### [ConSol docker-headless-vnc-container](https://github.com/ConSol/docker-headless-vnc-container)

**项目核心内容总结：**

该项目提供基于Docker的无头VNC容器镜像，包含Xfce4或IceWM桌面环境、VNC服务器（默认端口5901）、noVNC HTML5客户端（默认端口6901）及Firefox/Chromium浏览器，支持Rocky 9和Debian 11系统。  

**主要功能与特性：**  
1. **使用方法**  
   - 通过`docker run`命令启动容器，映射端口后可通过VNC客户端（如`localhost:5901`）或noVNC网页（`http://localhost:6901`）访问桌面环境。  
   - 支持自定义用户权限（如`--user $(id -u):$(id -g)`）、调整VNC分辨率（`VNC_RESOLUTION`）、修改密码（`VNC_PW`）或启用只读模式（`VNC_VIEW_ONLY=true`）。  

2. **扩展性**  
   - 可通过自定义Dockerfile安装额外软件（需切换至root用户）。  

3. **已知问题**  
   - 高分辨率下Chromium可能崩溃，需通过`--shm-size=256m`参数扩展共享内存。  

4. **部署支持**  
   - 提供Kubernetes和OpenShift部署文档。  

**默认配置：**  
- VNC密码：`vncpassword`  
- 默认用户ID：1000（可修改）  
- 环境变量可自定义分辨率、密码等。