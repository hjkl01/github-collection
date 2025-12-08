
---
title: ubicloud
---

### [ubicloud ubicloud](https://github.com/ubicloud/ubicloud)

Ubicloud 是一个开源的 IaaS 云平台，可运行于 Hetzner、AWS 等裸机服务商，提供类似 AWS 的云服务但完全开源。用户可通过托管服务直接使用，或自行部署：  
- **使用方法**：托管服务通过 [console.ubicloud.com](https://console.ubicloud.com) 访问；自建需克隆代码库、生成密钥、运行 Docker 容器，并配置 Hetzner 账户信息后执行云化脚本。  
- **核心功能**：  
  1. **弹性计算**：基于 Linux 裸机，使用 Cloud Hypervisor 虚拟化技术；  
  2. **网络**：支持 IPv4/IPv6 双栈，通过 IPsec 隧道加密通信，基于 nftables 实现防火墙与负载均衡；  
  3. **存储**：采用 SPDK 提供块存储，未来支持快照与复制；  
  4. **权限控制**：基于属性的访问控制（ABAC），支持细粒度权限管理。  
- **优势**：成本较 AWS 降低约 70%，支持裸机自建云，提供开源替代方案，避免供应商锁定。  
- **技术栈**：控制平面使用 Ruby/PostgreSQL，前端采用 Tailwind CSS，依赖 SSH 与裸机通信。