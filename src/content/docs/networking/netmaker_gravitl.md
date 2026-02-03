
---
title: netmaker
---

### [gravitl netmaker](https://github.com/gravitl/netmaker)  ![GitHub Repo stars](https://img.shields.io/github/stars/gravitl/netmaker?style=social)

### 项目核心内容总结：

#### 项目功能：
Netmaker 是一个基于 WireGuard 的自动化虚拟网络工具，支持从家庭实验室（homelab）到企业级部署。它提供图形化管理界面，用于创建和管理 WireGuard 网络，包括远程访问网关、点对点网络（Mesh）、站点间连接（Site-to-Site）等。

#### 使用方法：
- **SaaS 服务**：可通过 [netmaker.io](https://account.netmaker.io) 快速注册并使用托管服务。
- **自托管开源部署**：
  1. 准备一个 Ubuntu 24.04 的云服务器，配置静态公网 IP。
  2. 开放 443、51821 端口的 TCP/UDP 入站流量。
  3. （推荐）设置 DNS 解析，如 `*.netmaker.example.com`。
  4. 运行部署脚本快速安装开源版 Netmaker。

#### 主要特性：
- 自动化创建和管理 WireGuard 虚拟网络。
- 提供图形化管理界面（Admin UI）。
- 支持 OAuth 身份验证与访问控制列表（ACL）。
- 支持 Linux、Mac、Windows 客户端。
- 支持 Docker 部署。
- 提供私有 DNS 服务。
- 可扩展性强，适用于小型业务到大型企业。
- 提供社区支持与教程资源。

#### 社区项目：
Netmaker 拥有多个社区开发的扩展项目，如与 Traefik、Kubernetes、VyOS 等集成的插件，以及 GUI 工具等。

#### 许可证：
Netmaker 源代码采用 Apache 2.0 协议，部分内容（如 pro/ 目录）可能使用其他许可证，详见 [LICENSE.md](./LICENSE.md)。