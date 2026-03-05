
---
title: Surge
---

### [surge-downloader Surge](https://github.com/surge-downloader/Surge)  ![GitHub Repo stars](https://img.shields.io/github/stars/surge-downloader/Surge?style=social)

Surge 是一款基于 Go 语言构建的极速命令行下载管理器，专为高级用户设计。

核心功能：
*   **多模式支持**：提供美观的终端界面（TUI）、后台无头服务器模式及 CLI 工具，支持远程连接。
*   **高性能下载**：支持多线程并行下载（最多 32 连接），可从多个镜像源自动分发任务并故障转移。
*   **守护架构**：采用单引擎后台服务，允许在一个管理器中汇聚多个终端会话的下载队列。
*   **特色功能**：支持顺序下载（流媒体模式），提供浏览器扩展拦截下载，跨平台运行（Windows/macOS/Linux）及 Docker 支持。
*   **速度优势**：相比 curl、wget 等工具，带宽利用率更高，下载速度显著提升。