
---
title: loki
---

### [grafana loki](https://github.com/grafana/loki)

**项目核心内容总结：**  
Loki 是一个水平扩展、高可用、多租户的日志聚合系统，灵感来源于 Prometheus。它通过标签而非全文索引日志，简化操作并降低成本，特别适合 Kubernetes 环境。Loki 与 Grafana 集成，支持通过标签统一管理日志和指标，且无需依赖复杂组件。  

**主要特性：**  
- 仅索引日志元数据（标签），不存储日志内容全文，节省成本；  
- 支持 Kubernetes 容器日志自动采集与标签化；  
- 与 Grafana 原生集成，便于日志查询与可视化；  
- 使用 Alloy 作为日志采集代理（替代 Promtail），未来开发重点转向 Alloy；  
- 提供安装、升级、配置文档及社区支持。  

**使用方法：**  
1. 安装 Loki、Alloy 和 Grafana；  
2. 配置日志采集规则（如通过 Alloy 或 Docker Driver）；  
3. 使用 Grafana 查询与展示日志；  
4. 参考文档进行高级配置（如标签管理、管道处理、故障排查）。  

**构建与运行：**  
- 使用 Go 编译源码，支持单机运行；  
- 需安装 Go 及依赖库（如 systemd 开发包以启用 Journal 支持）；  
- 提供本地配置文件示例（`loki-local-config.yaml`）用于启动。