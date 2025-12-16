
---
title: rancher
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/rancher/rancher?style=social) ](https://github.com/rancher/rancher)
### [rancher rancher](https://github.com/rancher/rancher)

**Rancher 核心内容总结**  

**项目功能**  
Rancher 是一个开源的容器管理平台，专为生产环境部署容器的组织设计，简化 Kubernetes 的部署与管理，满足 IT 要求并赋能 DevOps 团队。  

**使用方法**  
通过 Docker 快速启动：  
```bash  
sudo docker run -d --restart=unless-stopped -p 80:80 -p 443:443 --privileged rancher/rancher  
```  
访问 `https://localhost` 进入管理界面。  

**主要特性**  
- 提供多个稳定版本（如 v2.13.0、v2.12.3 等），支持版本升级与降级。  
- 安装需满足特定操作系统、硬件和软件要求（详见官方文档）。  
- 提供详细文档、社区支持（论坛、Slack）及安全漏洞提交渠道。  
- 基于 Apache 2.0 许可证开源。