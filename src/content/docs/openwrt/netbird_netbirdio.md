
---
title: netbird
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/netbirdio/netbird?style=social) ](https://github.com/netbirdio/netbird)
### [netbirdio netbird](https://github.com/netbirdio/netbird)

NetBird 是一个基于 WireGuard 的开源网络工具，提供免配置的对等私有网络和集中访问控制，支持跨平台设备和多用户管理。其核心功能包括：  
1. **网络连接**：通过加密隧道自动建立对等连接，支持 NAT 穿透、路由外部网络及中继服务器回退。  
2. **安全管理**：集成 SSO/MFA、访问策略、设备状态检查、量子抗性加密（Rosenpass）及审计日志。  
3. **自动化与扩展**：提供 API、自托管部署方案、多身份提供商集成及批量设备注册功能。  

**使用方法**：  
- **云服务**：通过官网下载安装，注册后通过 Web UI 管理网络。  
- **自托管**：需 Linux 服务器（至少 1CPU/2GB 内存）、公网域名及 Docker 环境，运行一键脚本部署。  

**主要特性**：  
- 支持 Linux、Windows、Mac、iOS、Android、OpenWRT 等平台。  
- 提供 WebRTC ICE 协议实现 NAT 穿透，依赖 STUN/TURN 服务器。  
- 开源许可证：BSD-3-Clause（部分模块为 AGPLv3）。  

**适用场景**：企业/家庭私有网络构建、远程安全访问、多云环境互联。