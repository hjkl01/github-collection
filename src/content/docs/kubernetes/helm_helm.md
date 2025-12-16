
---
title: helm
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/helm/helm?style=social) ](https://github.com/helm/helm)
### [helm helm](https://github.com/helm/helm)

**核心内容总结：**  
Helm 是 Kubernetes 应用管理工具，通过 **Charts**（预配置的 Kubernetes 资源包）实现应用的安装、共享和管理。主要功能包括：  
- 安装和管理 Kubernetes 应用（类似 apt/yum/homebrew）；  
- 支持从远程仓库（如 ArtifactHub）获取或分享自定义 Charts；  
- 提供模板渲染、清单文件管理及版本化发布能力。  

**使用方法：**  
- 通过 [Releases 页面](https://github.com/helm/helm/releases/latest) 下载二进制文件，或使用 Homebrew、Chocolatey 等包管理器安装；  
- 参考 [Quick Start Guide](https://helm.sh/docs/intro/quickstart/) 快速上手。  

**主要特性：**  
- 支持本地存储或远程仓库获取 Charts；  
- Helm v4（开发中）与 v3（稳定版）分别位于 `main` 和 `dev-v3` 分支，版本间 API 不兼容；  
- 提供社区支持、贡献指南及代码规范。