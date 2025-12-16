
---
title: awesome-stacks
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/ethibox/awesome-stacks?style=social) ](https://github.com/ethibox/awesome-stacks)
### [ethibox awesome-stacks](https://github.com/ethibox/awesome-stacks)

**核心内容总结：**

**项目功能**  
"Awesome Stacks" 是一个通过 Docker 部署 150+ 开源 Web 应用的工具集，支持一键部署、域名绑定、版本控制等，适用于 Docker Swarm 环境。

**主要特性**  
- 一键部署：通过单条 Docker 命令快速部署应用  
- 零配置：无需手动调整配置，自动完成服务设置  
- 安全性：集成 Traefik 和 Let's Encrypt 实现 HTTPS 加密  
- 可定制：支持修改域名、存储路径、应用版本等参数  
- 兼容 Portainer：可通过 `templates.json` 在 Portainer 中部署  

**使用方法**  
1. 安装 Docker 并初始化 Swarm  
2. 部署 Traefik（依赖 Docker Overlay 网络）  
3. 使用 `docker stack deploy` 命令加载对应 `.yml` 配置文件部署应用  
4. 通过环境变量（如 `DOMAIN`、`VERSION`）自定义部署参数  

**其他**  
- 项目代码遵循 GNU GPL v3.0 协议  
- 提供 GitHub、Ko-fi 等平台的捐赠支持渠道