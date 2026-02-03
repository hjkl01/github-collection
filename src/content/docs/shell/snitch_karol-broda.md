
---
title: snitch
---

### [karol-broda snitch](https://github.com/karol-broda/snitch)  ![GitHub Repo stars](https://img.shields.io/github/stars/karol-broda/snitch?style=social)

snitch 是一款用于监控网络连接的工具，提供交互式 TUI 界面和表格视图，功能类似 `ss`/`netstat` 但更友好。其核心功能包括实时查看 TCP/UDP 连接状态、过滤监听端口或已建立连接、支持多种输出格式（表格、JSON、CSV 等），并可通过主题自定义界面样式。  

**使用方法**：  
- 安装方式包括 Homebrew、Go、Nix、Arch AUR、Shell 脚本、Docker 等。  
- 命令行操作如 `snitch`（交互式界面）、`snitch ls`（表格输出）、`snitch json`（JSON 输出）、`snitch watch`（流式输出）等，支持通过参数过滤协议、状态、端口等。  

**主要特性**：  
- 支持 Linux/macOS，需权限读取系统网络信息；  
- 提供 17 种主题样式，支持动态刷新（默认 2 秒）；  
- 可通过配置文件或环境变量自定义 DNS 解析、缓存、主题等；  
- 支持 Docker 镜像运行，适配多种操作系统；  
- 可通过 `snitch upgrade` 自动更新版本。