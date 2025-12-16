
---
title: cadvisor
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/google/cadvisor?style=social) ](https://github.com/google/cadvisor)
### [google cadvisor](https://github.com/google/cadvisor)

**核心内容总结：**  
cAdvisor 是一个容器监控工具，用于实时收集、聚合和导出容器的资源使用情况（如CPU、内存、网络等）及性能数据。其核心功能包括：  
1. **支持容器类型**：原生支持Docker容器，兼容其他容器类型。  
2. **数据导出**：通过存储插件（如Prometheus）导出数据，支持自定义配置。  
3. **可视化与接口**：提供Web UI查看数据，并通过REST API供外部调用。  
4. **部署方式**：  
   - 通过Docker命令快速部署（需挂载宿主机目录）。  
   - 在Kubernetes中以DaemonSet形式运行。  
5. **特性**：支持容器分层结构、历史数据统计、资源隔离参数分析。  

**使用方法**：  
- 使用Docker命令一键部署（需指定版本和挂载目录）。  
- 参考文档进行独立运行、构建镜像或配置存储插件。  
- Kubernetes用户可通过提供的部署文件集成到集群。  

**其他**：项目提供详细文档、社区支持及贡献者信息，目标是通过资源使用分析优化容器性能。