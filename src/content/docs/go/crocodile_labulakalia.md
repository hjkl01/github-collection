
---
title: crocodile
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/labulakalia/crocodile?style=social) ](https://github.com/labulakalia/crocodile)
### [labulakalia crocodile](https://github.com/labulakalia/crocodile)

**项目核心内容总结：**  

**功能**  
Crocodile 是一个基于 Golang 的分布式任务调度系统，支持通过 Web 界面管理任务，支持 HTTP 请求、Shell、Python、Go 等多种脚本语言任务。提供父子任务依赖关系、实时日志查看与终止、多调度算法（随机、轮询、权重、最小负载）、自定义报警策略（邮件、微信、钉钉等）、主机组管理、安全认证（证书加密、Token）等功能。  

**使用方法**  
1. **快速启动**：通过 `docker-compose up -d` 部署，访问 `http://yourip:8080` 初始化系统。  
2. **手动安装**：下载并解压，安装 Redis 和 MySQL，配置 `core.toml` 文件，生成证书（如需），运行调度中心（`./crocodile server -c core.toml`）和 Worker 节点（`./crocodile client -c core.toml`）。  

**主要特性**  
- 支持多种任务类型（HTTP、Shell、Python、Go 等）。  
- 父子任务依赖与串并行控制。  
- 四种调度算法（随机、轮询、权重、最小负载）。  
- 自定义报警策略，支持多平台通知（邮件、微信、钉钉、Slack、Telegram 等）。  
- 权限分级控制（管理员、普通用户、访客）。  
- 支持多平台（Linux、Mac、Windows）。  
- 任务日志管理、审计记录与清理。
