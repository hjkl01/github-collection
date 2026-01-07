
---
title: minikube
---

### [kubernetes minikube](https://github.com/kubernetes/minikube)  ![GitHub Repo stars](https://img.shields.io/github/stars/kubernetes/minikube?style=social)

**minikube核心内容总结：**  
minikube是一个用于在macOS、Linux和Windows上运行本地Kubernetes集群的工具，旨在为本地Kubernetes应用开发提供最佳体验，支持主流Kubernetes特性。  

**功能与特性：**  
- 支持Kubernetes核心功能：负载均衡（通过`minikube tunnel`）、多集群（通过`minikube start -p <name>`）、NodePort访问、持久卷、Ingress、Dashboard（通过`minikube dashboard`）、容器运行时配置（如Docker、containerd）等。  
- 开发者友好功能：插件市场（Addons）、NVIDIA/AMD GPU支持（用于机器学习）、文件系统挂载。  

**使用方法：**  
1. 安装：通过[Getting Started Guide](https://minikube.sigs.k8s.io/docs/start/)获取安装指引。  
2. 在GitHub Codespace中运行：点击链接启动环境，执行`minikube start`和`minikube dashboard`命令。  
3. 本地开发：支持通过命令行配置apiserver和kubelet参数，适配常见CI环境。  

**文档与社区：**  
- 官方文档地址：[https://minikube.sigs.k8s.io/docs/](https://minikube.sigs.k8s.io/docs/)  
- 社区资源包括Slack频道、邮件列表及贡献指南。