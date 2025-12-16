
---
title: KubePi
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/KubeOperator/KubePi?style=social) ](https://github.com/KubeOperator/KubePi)
### [KubeOperator KubePi](https://github.com/KubeOperator/KubePi)

**核心内容总结：**  
KubePi 是一个现代化的 Kubernetes 管理面板，支持多集群管理、权限控制和故障排查。管理员可导入多个 Kubernetes 集群，并分配不同集群/命名空间的权限给指定用户；开发人员可管理应用并进行故障排查。  

**使用方法：**  
通过 Docker 命令快速部署：`docker run --privileged -d --restart=unless-stopped -p 80:80 1panel/kubepi`，默认用户名 `admin`，密码 `kubepi`。也可通过 [1Panel 应用商店](https://apps.fit2cloud.com/1panel) 部署。  

**主要特性：**  
- 多集群管理与权限分配  
- 开发者友好的应用管理及故障排查界面  
- 开源，遵循 GPLv3 许可证