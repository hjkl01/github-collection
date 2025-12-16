
---
title: syncthing
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/syncthing/syncthing?style=social) ](https://github.com/syncthing/syncthing)
### [syncthing syncthing](https://github.com/syncthing/syncthing)

**项目功能**  
Syncthing 是一款用于在多台计算机之间持续同步文件的工具，注重数据安全与隐私保护，支持跨平台使用（Windows、macOS、Linux 等）。

**使用方法**  
1. 通过 [Getting Started 指南](https://docs.syncthing.net/intro/getting-started.html) 快速上手。  
2. 使用 Docker 部署：参考 [Docker README](https://github.com/syncthing/syncthing/blob/main/README-Docker.md)。  
3. 从源码构建：运行 `go run build.go` 生成二进制文件。  

**主要特性**  
- **数据安全**：防止数据丢失和未授权访问，支持端到端加密。  
- **自动同步**：最小化用户交互，自动处理文件同步。  
- **跨平台兼容**：支持主流操作系统，无需依赖最新技术。  
- **开源免费**：采用 [MPLv2 许可证](https://github.com/syncthing/syncthing/blob/main/LICENSE)，提供 GUI 界面（多平台）。  
- **社区支持**：通过 [论坛](https://forum.syncthing.net/) 或 [GitHub Issues](https://github.com/syncthing/syncthing/issues) 反馈问题，安全漏洞可通过邮件提交。  

**其他**  
- 提供详细文档（[官方文档](https://docs.syncthing.net/)）和自动升级机制。  
- 二进制文件支持 GPG 签名，确保来源可信。