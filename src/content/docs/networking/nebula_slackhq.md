
---
title: nebula
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/slackhq/nebula?style=social) ](https://github.com/slackhq/nebula)
### [slackhq nebula](https://github.com/slackhq/nebula)

### Nebula 核心内容总结

**项目功能**  
Nebula 是一个高性能、易用且安全的可扩展 overlay 网络工具，支持跨平台（Linux、Windows、macOS、iOS、Android）连接全球设备，适用于小型网络或大规模（数万节点）场景。通过加密、证书、安全组等技术，实现节点间的安全通信。

**使用方法**  
1. **安装**：下载对应平台的二进制文件或通过包管理器（如 Arch、Debian、Homebrew 等）安装。  
2. **配置网络**：  
   - 生成证书权威（CA）：`nebula-cert ca`。  
   - 为节点生成证书：`nebula-cert sign`（需指定节点名、IP、分组）。  
   - 配置 `config.yml`，设置 lighthouse（发现节点）和网络参数。  
3. **部署**：将 `ca.crt`、节点证书、配置文件复制到各主机，运行 `nebula -config` 启动服务。  
4. **可选**：部署 lighthouse 节点（需公网 IP）以实现节点自动发现。

**主要特性**  
- **安全通信**：基于 Noise 协议框架，使用 ECDH 密钥交换和 AES-256-GCM 加密。  
- **灵活分组**：通过用户定义的组实现跨云服务商、数据中心的流量过滤。  
- **自动发现**：lighthouse 节点支持 UDP 穿透防火墙/NAT，帮助节点互联。  
- **跨平台兼容**：支持移动端（iOS/Android）及主流服务器/桌面系统。  
- **证书管理**：支持 CA 证书轮换、证书有效期控制（默认 1 年）。  

**其他**  
- 可通过 Go 从源码编译，支持 Curve P256（NIST 曲线）及 BoringCrypto（合规场景）。  
- 提供 Docker 镜像及详细文档（[nebula.defined.net](https://nebula.defined.net/docs/)）。