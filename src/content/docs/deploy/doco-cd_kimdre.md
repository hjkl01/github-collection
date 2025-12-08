
---
title: doco-cd
---

### [kimdre doco-cd](https://github.com/kimdre/doco-cd)

**doco-cd** 是一个轻量级 GitOps 工具，用于自动部署和更新 Docker Compose 项目及 Swarm 堆栈，支持通过轮询和 Webhook 触发部署。其核心功能包括：

1. **部署方式**  
   支持通过 Git 仓库的代码变更自动触发部署，适用于 Docker Compose 项目和 Swarm 模式堆栈。

2. **特性**  
   - 极简设计，使用最小化镜像，资源占用低（Go 语言开发，对 CPU 和内存需求极小）。  
   - 支持多种 Git 提供商、外部密钥管理及数据加密（SOPS）。  
   - 提供部署通知、Prometheus 监控指标等运维功能。  
   - 兼容 Docker Compose 和 Swarm 模式，无需额外配置。  

3. **使用场景**  
   作为 Portainer 或 ArgoCD 的替代方案，适合需要轻量级、自动化部署的 Docker 环境。  

**文档和社区支持**  
提供 Wiki 文档、GitHub 讨论区及问题反馈渠道，支持用户贡献代码。