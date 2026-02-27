
---
title: kustomize
---

### [kubernetes-sigs kustomize](https://github.com/kubernetes-sigs/kustomize)  ![GitHub Repo stars](https://img.shields.io/github/stars/kubernetes-sigs/kustomize?style=social)

**项目核心内容总结：**

**项目名称：** kustomize  
**项目功能：**  
kustomize 是一个用于定制原始、无模板的 Kubernetes YAML 文件的工具，支持多环境配置（如开发、测试、生产），无需修改原始 YAML 文件即可进行灵活定制。

**主要特性：**  
- 专为 Kubernetes 设计，理解并能修改 Kubernetes API 对象。  
- 使用声明式配置文件（`kustomization.yaml`）定义如何修改资源。  
- 支持创建基础配置（base）与覆盖配置（overlay），实现多环境配置管理。  
- 与 `kubectl` 深度集成，从 Kubernetes v1.14 开始支持内嵌的 kustomize 功能。  
- 支持资源生成器（如 ConfigMap）、标签管理、字段覆盖、资源引用等。

**使用方法：**  
1. **创建基础配置：**  
   在包含 YAML 资源文件的目录中创建 `kustomization.yaml`，声明资源及其修改规则。  
   例如：添加标签、生成 ConfigMap。

2. **构建并应用配置：**  
   使用命令 `kustomize build <目录>` 生成最终的 YAML 文件，  
   可通过 `kubectl apply -f -` 直接应用到 Kubernetes 集群。

3. **创建变体（Overlay）：**  
   在基础配置之上创建覆盖配置，通过 `kustomization.yaml` 引用基础配置并添加补丁文件（patches）来定制不同环境的配置。  
   例如：修改副本数、资源限制等。

**结构示例：**  
- `base` 目录包含基础资源和通用配置。  
- `overlays` 目录包含针对不同环境的覆盖配置，每个环境有自己的 `kustomization.yaml` 和补丁文件。

**版本集成：**  
Kubernetes 各版本中嵌入了不同版本的 kustomize，可通过 `kubectl version` 查看当前嵌入版本。  
Kustomize 的版本更新会反映在 Kubernetes 的发布说明中。

**社区支持：**  
提供提交 bug、贡献功能和提出增强建议的渠道，遵循 Kubernetes 社区行为准则。