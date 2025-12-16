
---
title: kubernetes
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/kubernetes/kubernetes?style=social) ](https://github.com/kubernetes/kubernetes)
### [kubernetes kubernetes](https://github.com/kubernetes/kubernetes)

**核心内容总结：**  
Kubernetes（K8s）是一个开源系统，用于管理跨多台主机的容器化应用，提供部署、维护和扩展应用的基本机制。项目基于Google的Borg系统经验，由CNCF（云原生计算基金会）托管。  

**使用方法：**  
- 通过[kubernetes.io](https://kubernetes.io)官方文档开始使用，或参加[Scalable Microservices with Kubernetes]课程。  
- 作为库使用：参考[组件列表](https://git.k8s.io/kubernetes/staging/README.md)。  
- 开发：  
  - Go环境：`git clone https://github.com/kubernetes/kubernetes && make`  
  - Docker环境：`git clone https://github.com/kubernetes/kubernetes && make quick-release`  

**主要特性：**  
- 支持容器化应用的自动化部署、扩展和维护。  
- 结合Google生产级经验与社区最佳实践。  
- 提供跨主机资源调度、自我修复、负载均衡等能力（隐含于功能描述中）。