
---
title: trivy
---

### [aquasecurity trivy](https://github.com/aquasecurity/trivy)

**Trivy核心内容总结：**

**项目功能**  
Trivy是一款多功能安全扫描工具，支持扫描容器镜像、文件系统、Git仓库、虚拟机镜像及Kubernetes集群，可检测以下内容：  
- 操作系统包及软件依赖（SBOM）  
- 已知漏洞（CVE）  
- 基础设施即代码（IaC）问题与配置错误  
- 敏感信息与密钥泄露  
- 软件许可证合规性  

**使用方法**  
1. **安装方式**  
   - `brew install trivy`  
   - `docker run aquasec/trivy`  
   - 从GitHub下载二进制文件  

2. **基本命令**  
   - 扫描镜像：`trivy image <镜像名>`  
   - 扫描文件系统：`trivy fs --scanners <扫描器列表> <路径>`  
   - 扫描Kubernetes：`trivy k8s --report summary <集群名>`  

**主要特性**  
- 支持主流编程语言、操作系统及平台（详见扫描覆盖范围）  
- 提供Canary版本（非生产环境推荐）  
- 集成GitHub Actions、Kubernetes Operator等生态工具  
- 支持多扫描器组合使用（如漏洞、密钥、配置检查）