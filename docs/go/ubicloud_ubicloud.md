### [ubicloud ubicloud](https://github.com/ubicloud/ubicloud)  ![GitHub Repo stars](https://img.shields.io/github/stars/ubicloud/ubicloud?style=social)

Ubicloud 是一个开源的基础设施即服务（IaaS）云平台，旨在提供商业云（如 AWS、Azure）的开源替代方案。它支持在裸金属提供商（如 Hetzner、AWS Bare Metal）上运行，既提供托管服务，也支持用户自行搭建控制平面来管理裸金属机器。

核心功能包括：
1. **弹性计算**：通过 SSH 管理裸金属服务器，使用 Cloud Hypervisor 作为虚拟机监控器。
2. **网络**：使用 IPsec 隧道建立加密私有网络，支持 IPv4/IPv6 双栈，通过 nftables 实现防火墙和负载均衡。
3. **块存储**：基于 SPDK 提供虚拟化块存储，支持数据加密。
4. **安全**：支持基于属性的访问控制（ABAC），实现细粒度权限管理。

项目致力于降低云成本、消除供应商锁定，并为用户提供便携且可控的基础设施体验。