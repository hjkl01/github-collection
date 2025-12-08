
---
title: kubevirt
---

### [kubevirt kubevirt](https://github.com/kubevirt/kubevirt)

**KubeVirt 核心内容总结：**

**项目功能**  
KubeVirt 是 Kubernetes 的虚拟机管理扩展，通过自定义资源定义（CRD）向 Kubernetes 添加虚拟机资源类型（如 `VM`），实现通过 Kubernetes API 声明式管理虚拟机。支持创建、调度、启动、停止、删除虚拟机等操作。

**使用方法**  
- 快速入门：通过 [kubevirt.io/get_kubevirt](https://kubevirt.io/get_kubevirt/) 获取指南。  
- 用户文档：参考 [kubevirt.io/docs](https://kubevirt.io/user-guide) 了解详细用法。  
- 开发者：通过 [Getting Started Guide](docs/getting-started.md) 搭建环境，[CONTRIBUTING.md](https://github.com/kubevirt/kubevirt/blob/main/CONTRIBUTING.md) 参与贡献。

**主要特性**  
1. **Kubernetes 集成**：基于 Kubernetes CRD 扩展，无需修改 Kubernetes 核心代码。  
2. **声明式管理**：通过 YAML/JSON 定义虚拟机配置，实现自动化运维。  
3. **控制器与代理**：提供必要的控制器和代理组件，实现虚拟机生命周期管理。  
4. **社区支持**：提供 Slack、邮件组、博客等资源，支持版本矩阵和发布计划。  
5. **开源协议**：遵循 Apache License 2.0，支持 FOSSA 和 SonarCloud 等质量工具。