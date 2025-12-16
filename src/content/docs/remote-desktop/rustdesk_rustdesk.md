
---
title: rustdesk
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/rustdesk/rustdesk?style=social) ](https://github.com/rustdesk/rustdesk)
### [rustdesk rustdesk](https://github.com/rustdesk/rustdesk)

**项目核心内容总结：**  
RustDesk 是一个基于 Rust 语言开发的远程桌面工具，支持无需配置快速使用，用户可完全掌控数据安全。项目提供官方中继服务器供选择，也支持自建或自定义服务器。  

**使用方法：**  
- **构建依赖**：需安装 Rust 环境及 vcpkg，不同平台需额外安装对应依赖库（如 Linux 的 libx11、Windows 的 GDI 等）。  
- **构建方式**：支持常规命令行构建和 Docker 容器化构建，后者通过挂载目录和缓存加速重复构建。  

**主要特性：**  
- **模块化设计**：包含视频编解码、屏幕捕获、剪贴板传输等独立模块，便于扩展和维护。  
- **跨平台支持**：兼容 Windows、Linux、macOS 及移动端（通过 Flutter 实现）。  
- **安全可靠**：强调数据控制权在用户手中，支持 TCP 穿透和中继连接，确保通信稳定。  
- **社区驱动**：支持多语言本地化，鼓励开发者贡献代码。