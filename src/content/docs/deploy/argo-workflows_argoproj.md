
---
title: argo-workflows
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/argoproj/argo-workflows?style=social) ](https://github.com/argoproj/argo-workflows)
### [argoproj argo-workflows](https://github.com/argoproj/argo-workflows)

**核心内容总结：**

Argo Workflows 是一个开源的容器原生工作流引擎，基于 Kubernetes 实现，通过自定义资源定义（CRD）管理任务。它支持以容器为步骤的多阶段工作流定义，通过有向无环图（DAG）或步骤序列描述任务依赖关系，适用于机器学习、数据处理、CI/CD 等场景。

**功能与使用方法：**  
- 提供 UI 界面管理工作流，支持日志查看、暂停/恢复、取消等操作。  
- 通过 Helm Chart 或 Kubernetes 部署，可结合 CLI、REST/GRPC 接口使用。  
- 快速入门方式包括交互式教程（[Killercoda](https://killercoda.com/argoproj/course/argo-workflows/)）和在线演示环境（[Argo Workflows Demo](https://workflows.apps.argoproj.io/workflows/argo)）。

**主要特性：**  
1. **灵活性**：支持 DAG/步骤声明式定义、参数化、条件判断、循环、超时重试、依赖管理。  
2. **扩展性**：兼容多种存储（S3、Git、GCS 等）、多执行器（容器、脚本）、资源调度（亲和性、节点选择）。  
3. **监控与运维**：集成 Prometheus 指标、自动资源清理、Pod 扰动预算（PDB）支持。  
4. **生态集成**：与 Argo Events、Kubeflow Pipelines、Metaflow 等工具联动，支持 Python（Hera SDK）、Java、Go 客户端。  
5. **生产就绪**：支持大规模并行任务、Windows 容器、多集群部署，符合 CNCF 标准。