
---
title: flower
---

### [mher flower](https://github.com/mher/flower)

**核心内容总结：**

Flower 是一个开源的 Web 应用，用于监控和管理 Celery 集群。其核心功能包括：  
- **实时监控**：查看任务进度、历史记录、任务详情（参数、耗时等）。  
- **远程控制**：重启/关闭 worker、调整池大小、管理队列、撤销任务、设置限速等。  
- **经纪人监控**：统计所有 Celery 队列的状态。  
- **认证支持**：HTTP Basic Auth、OAuth（Google、GitHub、GitLab、Okta）。  
- **集成能力**：支持 Prometheus 监控和 REST API 管理（如通过 HTTP 调用任务、终止任务）。  

**使用方法**：  
1. 安装：通过 `pip install flower` 或 Docker 镜像。  
2. 运行：使用 `celery --broker=... flower` 命令，或通过 Docker 挂载配置文件。  
3. 默认端口为 5555，可通过 `--port` 参数修改。  

**主要特性**：  
- 实时任务跟踪与历史记录。  
- 丰富的 worker 管理和任务控制功能。  
- 多种认证方式及 Prometheus 集成。  
- 提供 REST API 实现远程操作。