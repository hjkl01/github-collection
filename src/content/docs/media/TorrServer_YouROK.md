
---
title: TorrServer
---

### [YouROK TorrServer](https://github.com/YouROK/TorrServer)  ![GitHub Repo stars](https://img.shields.io/github/stars/YouROK/TorrServer?style=social)

**项目核心内容总结**  
TorrServer 是一个基于网络的流媒体服务器，支持通过智能电视、媒体播放器等设备远程播放媒体文件，具备跨平台兼容性（支持 Linux、macOS、Windows、Android 等）。  

**主要功能与特性**  
1. **流媒体播放**：支持多种协议（如 DLNA），可将本地媒体文件通过网络流式传输至智能电视等设备。  
2. **用户认证**：通过 `accs.db` 文件配置用户名密码，启用基本认证（需启动参数 `--httpauth`）。  
3. **IP 控制**：支持白名单（`wip.txt`）和黑名单（`bip.txt`）管理访问权限，白名单优先级更高。  
4. **API 文档**：提供 Swagger 格式的 API 文档（路径 `/swagger/index.html`），便于集成与调试。  
5. **容器化部署**：支持 Docker 快速部署，可通过环境变量（如 `TS_PORT`、`TS_PROXYURL`）自定义配置。  
6. **多平台支持**：提供 Linux/macOS 命令行构建、Web 前端开发、Android 适配等。  

**使用方法**  
- **本地运行**：下载二进制文件，通过命令行启动（如 `TorrServer-darwin-arm64 --port 8090`）。  
- **Docker 部署**：使用 `docker run` 命令，挂载配置目录并映射端口（如 `-p 8090:8090`）。  
- **智能电视**：安装 Media Station X，设置 TorrServer 的 IP 和端口（如 `127.0.0.1:8090`）。  

**其他**  
- 提供中文、简体中文、保加利亚语等多语言界面支持。  
- 通过 GitHub 社区维护，支持开发者贡献代码与文档。