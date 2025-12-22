
---
title: croc
---

### [schollz croc](https://github.com/schollz/croc)  ![GitHub Repo stars](https://img.shields.io/github/stars/schollz/croc?style=social)

**项目核心内容总结：**  

`croc` 是一个支持跨平台（Windows、Linux、Mac）的命令行工具，用于在任意两台设备之间**安全、快速、可靠**地传输文件和文件夹。其核心功能包括：  
- **中继传输**：无需本地服务器或端口转发，通过中继服务器实现传输。  
- **端到端加密**：基于 PAKE 协议，确保数据传输安全性。  
- **断点续传**：支持中断后恢复传输。  
- **IPv6 优先**：默认使用 IPv6，兼容 IPv4。  
- **代理支持**：可通过 SOCKS5 代理（如 Tor）传输。  

**使用方法：**  
1. **发送文件**：`croc send [文件或文件夹]`，系统会生成一个代码短语（用于接收端验证）。  
2. **接收文件**：在目标设备运行 `croc [代码短语]`。  
3. **自定义选项**：  
   - 指定代码短语：`croc send --code [自定义短语]`。  
   - 使用代理：`croc --socks5 [代理地址] send [文件]`。  
   - 更改加密曲线：`croc --curve [曲线名称] [代码短语]`。  
   - 自托管中继：运行 `croc relay` 启动中继服务，并通过 `--relay [中继地址]` 指定中继。  

**主要特性：**  
- 支持多文件传输、跨平台、无需配置服务器。  
- 默认将代码短语复制到剪贴板，支持静默模式（`--quiet`）。  
- 提供 Docker 镜像和多种安装方式（Homebrew、Conda、源码编译等）。  

**其他：**  
- 支持通过管道传输数据（如 `cat 文件 | croc send`）。  
- 可自定义排除文件夹（`--exclude`）、覆盖文件（`--overwrite`）、发送文本（`--text`）等。