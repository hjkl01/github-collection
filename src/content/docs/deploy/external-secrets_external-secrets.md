
---
title: external-secrets
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/external-secrets/external-secrets?style=social) ](https://github.com/external-secrets/external-secrets)
### [external-secrets external-secrets](https://github.com/external-secrets/external-secrets)

**核心内容总结：**  
External Secrets Operator 是一个 Kubernetes 操作符，用于集成外部秘密管理系统（如 AWS Secrets Manager、HashiCorp Vault、Google Secrets Manager 等），通过读取外部 API 数据，自动将敏感信息注入 Kubernetes Secret 中。  

**主要功能：**  
- 支持多种外部秘密管理后端（AWS、Vault、Azure、IBM 等）。  
- 自动同步外部系统中的秘密到 Kubernetes Secret，无需手动维护。  
- 提供文档、社区贡献指南及安全漏洞报告机制。  

**使用方法：**  
1. 部署 External Secrets Operator 到 Kubernetes 集群。  
2. 配置外部秘密管理系统的连接参数（如访问密钥、地址等）。  
3. 通过自定义资源（如 `ExternalSecret`）声明需要同步的秘密，Operator 会自动拉取并注入 Kubernetes Secret。  

**主要特性：**  
- 多后端兼容，支持主流云服务提供商和秘密管理工具。  
- 自动化同步，减少人工干预和错误风险。  
- 提供安全性保障（如漏洞报告、SBOM 文件）。  
- 社区驱动，支持贡献和协作开发。