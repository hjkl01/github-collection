
---
title: wsgidav
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/mar10/wsgidav?style=social) ](https://github.com/mar10/wsgidav)
### [mar10 wsgidav](https://github.com/mar10/wsgidav)

WsgiDAV 是一个基于 Python 和 WSGI 的通用 WebDAV 服务器，支持 SSL 和多线程，可作为独立脚本运行或集成到其他 WSGI 服务器中。主要功能包括：  
1. **使用方式**：通过 `pip` 安装后，用命令行启动（如 `wsgidav --host=0.0.0.0 --port=80 --root=/tmp`）；支持 PAM 认证（需额外安装依赖）；Windows 用户可使用 MSI 安装包或 winget；Docker 用户可通过镜像运行（如 `docker run` 挂载目录）。  
2. **核心特性**：支持匿名/认证访问、虚拟文件系统扩展、在线编辑文档；采用可配置的 WSGI 中间件架构，允许灵活集成；兼容 HTTP 协议，具备高性能。  
3. **其他**：支持 SSL、跨平台（Linux/OSX/Windows），提供 Docker 镜像和文档支持。