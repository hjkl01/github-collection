
---
title: dozzle
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/amir20/dozzle?style=social) ](https://github.com/amir20/dozzle)
### [amir20 dozzle](https://github.com/amir20/dozzle)

**项目核心内容总结：**  

**功能**：Dozzle 是一个轻量级工具，通过网页界面实时监控 Docker 容器日志，不存储日志文件，支持智能模糊搜索、正则表达式、SQL 查询、多屏分视图、实时资源统计、多用户认证、Swarm 模式及多主机监控（Agent 模式），并提供暗色模式。  

**使用方法**：  
1. **Docker 命令**：运行容器并挂载 `/var/run/docker.sock`，映射 8080 端口。  
2. **Docker Compose**：配置 `docker-compose.yml` 文件，挂载 socket 并开放端口。  
3. **Swarm 模式**：通过 `docker service create` 命令部署为全局服务。  
4. **Agent 模式**：运行容器时指定 `agent` 参数，用于监控多个 Docker 主机。  

**主要特性**：  
- 轻量高效（7MB 镜像），低内存占用；  
- 支持复杂查询（SQL、正则）与多容器日志对比；  
- 兼容 Docker Swarm、Podman 等环境；  
- 提供匿名使用数据统计（可关闭）。