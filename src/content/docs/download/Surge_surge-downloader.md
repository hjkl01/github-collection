
---
title: Surge
---

### [surge-downloader Surge](https://github.com/surge-downloader/Surge)  ![GitHub Repo stars](https://img.shields.io/github/stars/surge-downloader/Surge?style=social)

**Surge 项目总结**

**简介**
Surge 是一个基于 Go 语言构建的、面向高级用户的超快命令行下载管理器，旨在通过多连接和多镜像技术最大化带宽利用率。

**主要特性**
*   **多界面支持**：包含美观的终端用户界面 (TUI)、后台无头服务器 (Headless Server) 和 CLI 工具。
*   **极速下载**：支持单文件多连接（最多 32 个）并行下载，性能显著优于 curl 和 wget。
*   **多镜像与故障转移**：自动分配任务到多个镜像源，失败时自动切换。
*   **守护进程架构**：单一后台引擎统一管理，支持多个终端同时接入同一个下载队列。
*   **流媒体模式**：支持顺序下载，适合边下载边预览。
*   **浏览器扩展**：支持 Chrome/Edge/Brave 和 Firefox，可拦截浏览器下载任务。

**使用方法**
1.  **安装**：提供预编译二进制、Homebrew、Winget、AUR、Docker 及 Go 环境安装。
2.  **交互模式**：运行 `surge` 启动 TUI 界面管理任务；支持直接传入 URL 或批量文件。
3.  **服务器模式**：运行 `surge server` 启动后台服务，支持 Docker 部署，默认绑定 HTTP API 端口。
4.  **远程连接**：使用 `surge connect` 命令连接本地或远程服务器。
5.  **配置与认证**：通过 `surge token` 生成 API 令牌，支持通过 `--host` 和 `--token` 参数配置连接。

**许可证**
MIT License。