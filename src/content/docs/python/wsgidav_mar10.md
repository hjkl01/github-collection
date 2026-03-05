
---
title: wsgidav
---

### [mar10 wsgidav](https://github.com/mar10/wsgidav)  ![GitHub Repo stars](https://img.shields.io/github/stars/mar10/wsgidav?style=social)

WsgiDAV 是一款基于 Python 和 WSGI 协议的通用可扩展 WebDAV 服务器。

主要功能：
- **独立服务**：支持 SSL 加密，可作为命令行脚本在 Linux、macOS 和 Windows 系统上直接运行。
- **灵活部署**：支持 Docker 容器化、Windows MSI 安装，也可作为 Python 库嵌入任意 WSGI 兼容的 Web 服务器后端。
- **架构扩展**：采用可配置的 WSGI 中间件堆栈，支持将数据结构暴露为虚拟可编辑文件系统，并提供在线编辑 MS Office 文档的能力。
- **认证支持**：支持匿名访问、PAM 登录等多种认证方式。
- **高性能 Web 服务**：基于 HTTP 协议，提供多线程高性能 Web 服务。