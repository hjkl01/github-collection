
---
title: nginxpulse
---

### [likaia nginxpulse](https://github.com/likaia/nginxpulse)  ![GitHub Repo stars](https://img.shields.io/github/stars/likaia/nginxpulse?style=social)

**项目核心内容总结：**

nginxpulse 是一个用于分析 Nginx 日志的工具，支持实时统计、可视化展示及数据存储。其主要功能包括：

1. **日志处理**  
   - 支持多种 Nginx 日志格式（如 `combined`、`common`）及 Gzip 压缩日志解析。  
   - 提供 IP 过滤规则（如排除内网地址），可自定义是否统计内网 IP 的 PV（页面浏览量）。  

2. **统计与存储**  
   - 实时统计访问量、IP 地理分布等数据，存储至 SQLite 数据库。  
   - 支持通过 API 获取统计结果，或通过 Web 界面查看可视化数据。  

3. **部署与使用**  
   - 通过配置文件（如 `nginxpulse_config.json`）设置日志路径、存储目录等参数。  
   - 支持本地运行（使用 `dev_local.sh` 脚本）或 Docker 部署（通过 `docker-compose.yml`）。  
   - Web 界面默认访问地址为 `http://localhost:8080`，提供基础的 PV 统计与过滤功能。  

4. **扩展性**  
   - 核心逻辑模块化，统计规则、IP 地理定位等功能可通过代码扩展。  
   - 提供 HTTP 服务与中间件，便于集成到其他系统。  

**使用方法**  
- 配置 `nginxpulse_config.json` 文件，指定日志路径、数据库位置等。  
- 运行项目：本地开发使用 `scripts/dev_local.sh`，或通过 Docker 启动。  
- 访问 Web 界面查看统计结果，或调用 API 接口获取数据。  

**主要特性**  
- 实时处理与可视化；  
- 支持多日志格式及 Gzip 解压；  
- 内置 IP 过滤与地理定位；  
- 数据持久化至 SQLite；  
- 提供 Web UI 与 RESTful API。