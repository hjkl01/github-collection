
---
title: k3s
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/k3s-io/k3s?style=social) ](https://github.com/k3s-io/k3s)
### [k3s-io k3s](https://github.com/k3s-io/k3s)

**K3s核心内容总结：**

**项目功能**  
K3s是轻量级、生产级的Kubernetes发行版，专为资源受限环境设计，内存占用仅为原生Kubernetes的一半，二进制文件体积小于100MB。支持边缘计算、物联网、CI/CD、开发环境、ARM架构及嵌入式Kubernetes场景。  

**主要特性**  
1. **轻量化**：单二进制文件安装，集成Containerd、Flannel、CoreDNS、Traefik等组件，无需复杂依赖。  
2. **灵活存储**：默认使用SQLite3，支持Etcd3、MariaDB、MySQL、PostgreSQL等。  
3. **简化管理**：自动管理TLS证书、节点连接、集群资源部署及嵌入式etcd集群。  
4. **安全默认**：轻量环境中合理的安全配置，无需额外调整。  
5. **兼容性**：符合Kubernetes Conformance标准，移除原生存储驱动和云提供商，改用CSI/CCM等替代方案。  

**使用方法**  
- **快速安装**：通过脚本一键部署，执行命令`curl -sfL https://get.k3s.io | sh -`，自动生成kubeconfig文件。  
- **手动安装**：下载二进制文件后运行`sudo k3s server`启动服务，工作节点通过`K3S_URL`和`K3S_TOKEN`加入集群。  

**适用场景**  
适合资源受限设备、需要简化部署流程的场景，以及希望减少运维复杂度的用户。