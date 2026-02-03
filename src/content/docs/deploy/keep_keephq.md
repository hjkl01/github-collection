
---
title: keep
---

### [keephq keep](https://github.com/keephq/keep)  ![GitHub Repo stars](https://img.shields.io/github/stars/keephq/keep?style=social)

**核心内容总结：**  
Keep 是一个用于监控工具的自动化工作流平台，功能类似 GitHub Actions。用户可通过 YAML 文件定义工作流，实现警报和事件管理的自动化，包含触发器（如警报、定时任务）、数据处理步骤（如上下文丰富）和操作（如创建 Jira 工单、发送 Slack 消息）。  

**主要特性：**  
- **集成支持**：兼容 Sentry、Jira、Slack、Kubernetes、AWS SQS 等工具。  
- **企业级功能**：支持 SSO、RBAC、高可用部署及私有化部署。  
- **灵活部署**：支持 Docker、Kubernetes、AWS ECS、OpenShift 等多种环境。  

**使用方法：**  
通过 Docker Compose、Kubernetes 或云平台部署，编写 YAML 工作流文件定义规则（如根据 Sentry 的严重警报自动创建 Jira 工单）。  

**其他：**  
提供开源示例（GitHub 示例库），支持社区贡献及企业级扩展。