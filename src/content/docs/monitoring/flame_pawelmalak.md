
---
title: flame
---

### [pawelmalak flame](https://github.com/pawelmalak/flame)

**Flame** 是一款自托管的服务器启动页应用，灵感源自 SUI，提供图形化界面管理应用和书签，无需手动编辑文件即可快速搭建个人应用中心。  

**核心功能**：  
- 通过 GUI 创建/编辑/删除应用和书签，支持首页固定、本地搜索（含 11 个搜索引擎）、自定义 CSS 和 15 种主题。  
- 集成天气模块（需 API 密钥），显示实时天气信息。  
- 支持 Docker 和 Kubernetes 集成，通过容器标签自动识别应用（如 `flame.type=application`）。  

**使用方法**：  
- **Docker 安装**：  
  ```bash  
  docker run -p 5005:5005 -v /path/to/data:/app/data -e PASSWORD=flame_password pawelmalak/flame  
  ```  
  可通过 Docker-Compose 配置文件部署，支持密钥文件认证。  
- **非 Docker 安装**：参考 Wiki 中的 [无 Docker 安装指南](https://github.com/pawelmalak/flame/wiki/Installation-without-docker)。  

**主要特性**：  
- 支持自定义 CSS 和主题，提供主题构建器。  
- 搜索栏支持自定义引擎（如 `/g` 前缀调用 Google）。  
- Docker 集成需在容器标签中定义 `flame.type`、`flame.name`、`flame.url` 等参数。  
- 可通过 Python 脚本导入 HTML 书签（实验性功能）。