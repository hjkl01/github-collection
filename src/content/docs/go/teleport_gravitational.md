
---
title: teleport
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/gravitational/teleport?style=social) ](https://github.com/gravitational/teleport)
### [gravitational teleport](https://github.com/gravitational/teleport)

**核心内容总结：**  

**项目功能**  
Teleport 是一个用于基础设施连接、认证、访问控制和审计的工具，支持通过 SSO 设置、mTLS 端点保护、隧道建立、审计日志、RBAC 统一等特性，实现对服务器、应用和设备的安全访问管理。兼容多种协议（如 SSH、RDP、GraphQL）和云服务，适用于跨云、混合云及本地环境。  

**使用方法**  
- **安装运行**：通过官方下载链接获取社区版，支持单节点部署，需配置数据目录（如 `/var/lib/teleport`）。  
- **Docker 部署**：提供 Docker 镜像，支持快速部署。  
- **本地构建**：使用 Go 编译，支持热重载开发模式（通过 `CompileDaemon` 工具），并可自定义构建参数（如动态/静态链接 libfido2）。  
- **Web UI 开发**：通过 `make docker-ui` 重建 Web 界面，支持本地开发服务器实时调试。  

**主要特性**  
- **安全认证**：基于证书的双向认证（mTLS）、支持 2FA（如 Touch ID）和 GitHub SSO（社区版）。  
- **跨平台兼容**：支持多云、混合云、本地服务器及设备，适配多种操作系统。  
- **开发效率**：提供热重载、本地 Web UI 开发环境，简化迭代流程。  
- **生产就绪**：通过多轮安全审计，支持企业级应用，被多家公司用于生产环境。  

**许可证**  
- API 模块使用 Apache 2.0 许可证，其余代码使用 GNU Affero GPL 许可证。社区版下载链接提供修改后的 Apache 2.0 许可证。