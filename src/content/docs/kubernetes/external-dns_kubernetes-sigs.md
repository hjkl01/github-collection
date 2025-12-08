
---
title: external-dns
---

### [kubernetes-sigs external-dns](https://github.com/kubernetes-sigs/external-dns)

**项目核心内容总结：**  
ExternalDNS 是一个 Kubernetes 工具，用于根据集群内的资源（如 Service、Ingress）自动创建、更新和删除 DNS 记录，支持多云 DNS 提供商（如 Google、AWS、Azure、Cloudflare 等）。  

**主要功能：**  
1. **自动同步**：通过注解（Annotation）绑定 Kubernetes 资源（如 Service）到指定 DNS 域名，自动同步 IP 变化。  
2. **多 DNS 支持**：兼容主流云服务商（AWS、Azure、Google 等）及自建 DNS（如 PowerDNS）。  
3. **灵活配置**：支持自定义 TTL、内部服务记录（ClusterIP）、TXT 记录前缀等参数。  
4. **安全模式**：提供 `--dry-run` 模式预览 DNS 变更，确保无误后执行。  

**使用方法：**  
- **部署方式**：可部署到 Kubernetes 集群（如通过 Helm 或 YAML 模板），或本地运行。  
- **配置步骤**：  
  1. 创建 Kubernetes Service 并添加 `external-dns.alpha.kubernetes.io/hostname` 注解指定域名。  
  2. 使用 `external-dns` 命令行工具，指定 DNS 提供商、项目、资源来源（如 Service）等参数运行。  
- **示例命令**：`external-dns --txt-owner-id <集群ID> --provider google --google-project <项目名> --source service`  

**主要特性：**  
- 支持 LoadBalancer、Internal 服务类型及多资源来源（如 Ingress、Nodes）。  
- 提供教程覆盖主流云环境（AWS、Azure、GCP 等）和 Ingress 控制器集成。  
- 可通过注解控制记录类型（A、CNAME、TXT）及 TTL 值，兼容 MetalLB 等裸金属集群方案。