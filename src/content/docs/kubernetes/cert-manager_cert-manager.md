
---
title: cert-manager
---

### [cert-manager cert-manager](https://github.com/cert-manager/cert-manager)  ![GitHub Repo stars](https://img.shields.io/github/stars/cert-manager/cert-manager?style=social)

cert-manager 是一个 Kubernetes 插件，用于将证书和证书颁发机构作为 Kubernetes 集群中的资源类型进行管理，简化证书的获取、更新和使用流程。

### 核心功能：
- **证书管理**：支持从多种来源（如 Let's Encrypt、HashiCorp Vault、CyberArk 等）签发证书。
- **自动续期**：在证书到期前自动尝试续期，减少服务中断风险。
- **资源抽象**：将证书和颁发机构抽象为 Kubernetes 资源（如 Issuer、Certificate 等）。

### 使用方法：
- 提供多种安装方式，详见 [安装文档](https://cert-manager.io/docs/installation/)。
- 可通过定义 Kubernetes 资源（如 Issuer 和 Certificate）实现证书的自动签发和管理。
- 支持自动为 Ingress 资源签发 TLS 证书。

### 主要特性：
- **多颁发机构支持**：包括 ACME（如 Let's Encrypt）、Vault、本地签发等。
- **高可用性保障**：通过自动续期机制确保证书始终有效。
- **活跃的社区支持**：提供详细的文档、Slack 频道支持和定期会议。
- **贡献友好**：支持 Linux 和 macOS 开发环境，提供开发指南和编码规范。

### 安全与维护：
- 提供安全报告机制，鼓励用户报告漏洞。
- 每个版本都有详细的变更日志和发布说明。
- 项目基于 kube-lego 等类似项目的经验发展而来。