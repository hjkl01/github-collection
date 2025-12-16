
---
title: prometheus
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/prometheus/prometheus?style=social) ](https://github.com/prometheus/prometheus)
### [prometheus prometheus](https://github.com/prometheus/prometheus)

**核心内容总结：**  
Prometheus 是 CNCF 旗下的一款系统和服务监控工具，通过定时抓取目标指标、评估规则并触发告警，支持多维数据模型（指标名+键值维度）、PromQL 查询语言、HTTP 拉取模式、服务发现、静态配置、图形化展示及联邦架构。  

**使用方法：**  
1. **预编译二进制**：从 [prometheus.io/download](https://prometheus.io/download/) 下载安装包。  
2. **Docker 镜像**：使用 `docker run` 命令快速启动容器。  
3. **源码构建**：需 Go、NodeJS 和 npm，执行 `make build` 编译，或通过 `go install` 安装（需额外构建前端资源）。  
4. **自定义插件**：修改 `plugins.yml` 文件可启用/禁用服务发现插件。  

**主要特性：**  
- 多维数据模型与 PromQL 查询能力；  
- 无需依赖分布式存储，单节点自主运行；  
- 支持 HTTP 拉取及通过网关推送指标；  
- 服务发现与静态配置结合；  
- 图表、仪表盘及联邦架构支持。