
---
title: actions-runner-controller
---

### [actions actions-runner-controller](https://github.com/actions/actions-runner-controller)

**核心内容总结：**  
Actions Runner Controller（ARC）是一个基于 Kubernetes 的开源工具，用于管理和自动扩展 GitHub Actions 的自托管运行器。其核心功能包括：  
1. **自动扩展**：根据仓库、组织或企业中的工作流运行需求，动态调整运行器数量。  
2. **容器化运行器**：支持以容器形式快速创建和销毁临时运行器，实现高效资源利用。  
3. **多场景适配**：可将运行器部署到指定的仓库、组织或企业，并支持自定义卷、Windows 系统等场景。  

**使用方法**：  
- 通过 Helm 在 Kubernetes 上部署 ARC。  
- 参考官方文档的快速入门指南配置运行器规模集（Runner Scale Sets）。  

**主要特性**：  
- 支持 GitHub 官方维护的自动扩展模式及社区维护的遗留模式。  
- 提供丰富的文档和社区支持，可贡献代码或通过 GitHub 赞助支持项目。