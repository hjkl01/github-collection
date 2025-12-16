
---
title: velero
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/vmware-tanzu/velero?style=social) ](https://github.com/vmware-tanzu/velero)
### [vmware-tanzu velero](https://github.com/vmware-tanzu/velero)

**项目核心内容总结：**  
Velero（原Heptio Ark）是一款用于 Kubernetes 集群资源和持久卷备份与恢复的工具，支持公有云和本地部署。主要功能包括：  
- 备份集群数据并实现灾难恢复  
- 迁移集群资源至其他集群  
- 将生产环境复制到开发/测试环境  

**组成**：  
- 集群内运行的服务器组件  
- 本地执行的命令行客户端  

**使用方法**：  
通过官方文档获取入门指南、源码构建说明及扩展方法。需根据 Velero 版本选择对应文档。  

**关键特性**：  
- 支持 IPv4、IPv6 及双栈环境（测试覆盖至 v1.8）  
- 提供版本兼容性矩阵（如 v1.17 支持 Kubernetes 1.18-latest，测试环境包括 1.31.7、1.32.3 等）  
- 维护团队确保每版支持从 n-2 次版本升级路径（如 v1.10.x 支持从 v1.9.x/v1.8.x 恢复备份）  

**注意事项**：  
使用非推荐版本组合前需自行测试，具体能力参考 Velero 和 Kubernetes 官方发布说明。