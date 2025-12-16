
---
title: exatorrent
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/varbhat/exatorrent?style=social) ](https://github.com/varbhat/exatorrent)
### [varbhat exatorrent](https://github.com/varbhat/exatorrent)

**项目核心内容总结：**

**功能**  
exatorrent 是一个用 Go 语言编写的自托管 BitTorrent 客户端，提供轻量级、跨平台的磁盘下载与流媒体服务。支持通过 Web 界面（基于 Svelte 和 TypeScript）管理 torrent，具备多用户模式、文件解锁/锁定、速率限制、自动添加 tracker 等功能。下载的文件可通过 HTTP 浏览器或媒体播放器（如 VLC）直接访问。

**使用方法**  
1. **下载预编译版本**：从 GitHub 发布页获取对应系统的二进制文件，赋予权限后运行。  
   示例：`wget` 下载后执行 `chmod +x` 并运行。  
2. **Docker 镜像**：通过 `docker pull` 获取镜像，运行容器时映射端口并挂载存储目录。  
3. **手动构建**：使用 `make web && make app` 编译源码。  

**主要特性**  
- 单个静态二进制文件，无外部依赖，跨平台（Linux/macOS/Windows）。  
- 支持磁力链接、InfoHash 或 Torrent 文件添加，可控制单个文件的下载/停止/删除。  
- 提供 WebSocket API，支持自定义客户端开发。  
- 多用户模式（含认证），可配置下载目录、种子完成动作、块列表过滤等。  
- 支持 ZIP/Tarball 导出下载目录，文件流媒体播放。  
- 默认用户初始密码为 `adminpassword`（用户名不可更改），支持后续修改。  

**许可证**  
采用 [GPL-v3](LICENSE) 开源协议。