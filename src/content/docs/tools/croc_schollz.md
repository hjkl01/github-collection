
---
title: croc
---

### [schollz croc](https://github.com/schollz/croc)  ![GitHub Repo stars](https://img.shields.io/github/stars/schollz/croc?style=social)

`croc` 是一款跨平台命令行工具，允许任意两台计算机简单且安全地传输文件和文件夹。

主要功能：
- **端到端加密**：使用 PAKE 协议生成密钥，确保传输安全，无需本地服务器或端口转发。
- **灵活传输**：支持多文件/文件夹传输、断点续传、发送文本，支持自定义传输代码及排除特定文件夹。
- **网络兼容**：支持 IPv6 优先及 IPv4 回退，支持通过代理（如 Tor）传输。
- **部署灵活**：兼容 Windows、Linux、macOS 等主流系统，支持自建中继服务器及多种安装方式。