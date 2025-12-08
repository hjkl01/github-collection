
---
title: ingress-nginx
---

### [kubernetes ingress-nginx](https://github.com/kubernetes/ingress-nginx)

**项目核心内容总结：**

**功能**：ingress-nginx 是 Kubernetes 的 Ingress 控制器，基于 NGINX 实现，用于管理 Kubernetes 集群中 HTTP/HTTPS 请求的路由，将外部流量转发至集群内服务。

**使用方法**：  
- 通过 Helm Chart 或 Kubernetes YAML 文件部署。  
- 配置 Ingress 资源定义路由规则，支持注解自定义配置（如 SSL、负载均衡等）。  

**主要特性**：  
1. 支持 Kubernetes Ingress API，兼容多种注解配置。  
2. 自动 SSL 证书管理（如 Let's Encrypt）。  
3. 负载均衡、访问控制、路径重写等高级功能。  
4. 日志记录与监控集成。  
5. 支持多版本 Kubernetes（如 v1.20 至最新版本）。  

**其他**：提供社区支持、贡献指南及中文文档（需自行翻译），遵循 Apache 2.0 协议。