
---
title: agent-sandbox
---

### [kubernetes-sigs agent-sandbox](https://github.com/kubernetes-sigs/agent-sandbox)  ![GitHub Repo stars](https://img.shields.io/github/stars/kubernetes-sigs/agent-sandbox?style=social)

**项目核心内容总结：**

Agent Sandbox 是 Kubernetes 的一个项目，提供一种声明式 API（通过 `Sandbox` CRD）来管理长期运行、有状态的单实例容器工作负载，适用于 AI 代理运行时等场景。其核心功能包括：

1. **稳定身份与持久存储**  
   每个 Sandbox 具有稳定的主机名和网络身份，并支持持久化存储，确保重启后数据不丢失。

2. **生命周期管理**  
   支持创建、删除、暂停和恢复 Sandbox 的生命周期操作。

3. **扩展功能**  
   - `SandboxTemplate`：定义可复用的 Sandbox 模板。  
   - `SandboxClaim`：通过模板声明式创建 Sandbox。  
   - `SandboxWarmPool`：预热池快速分配资源，减少启动时间。

**使用方法：**  
通过 YAML 文件定义 `Sandbox` 资源，指定容器镜像等参数即可创建实例。例如：
```yaml
apiVersion: agents.x-k8s.io/v1alpha1
kind: Sandbox
metadata:
  name: my-sandbox
spec:
  podTemplate:
    spec:
      containers:
      - name: my-container
        image: <IMAGE>
```
安装需通过 `kubectl apply` 部署控制器和 CRD，支持扩展组件及 Python SDK 编程调用。

**主要特性：**  
- 支持多种运行时（如 gVisor）实现强隔离。  
- 支持深度休眠、自动恢复、高效存储。  
- 可跨 Sandbox 共享内存（依赖运行时）。  
- 提供丰富网络身份和连接能力。  
- 支持编程化操作（如 SDK）。