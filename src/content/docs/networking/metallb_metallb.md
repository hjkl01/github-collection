
---
title: metallb
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/metallb/metallb?style=social) ](https://github.com/metallb/metallb)
### [metallb metallb](https://github.com/metallb/metallb)

**核心内容总结：**  
MetalLB 是一个为裸金属 Kubernetes 集群设计的负载均衡器，通过标准路由协议（如 BGP、ARP）实现服务暴露。主要功能包括：  
- **使用场景**：适用于无云服务商支持的裸金属集群，提供类似云环境的负载均衡能力。  
- **部署方式**：通过 Kubernetes 的 Helm Chart 或 YAML 文件安装，建议使用官方文档推荐的稳定分支（而非开发中的 main 分支）。  
- **特性**：支持多协议（BGP、ARP）、高可用性、自动分配 IP 地址，开源协议为 Apache 2.0。  
- **社区支持**：提供安全漏洞报告渠道（邮件联系维护者），鼓励用户反馈使用情况以优化项目。  

**注意事项**：  
- main 分支为开发版，可能不稳定，生产环境应使用稳定分支。  
- 安装时需参考官方文档的部署指引，避免兼容性问题。