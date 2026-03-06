
---
title: medis
---

### [luin medis](https://github.com/luin/medis)  ![GitHub Repo stars](https://img.shields.io/github/stars/luin/medis?style=social)

Medis 是一款基于 Electron、React 和 Redux 构建的开源 Redis 图形化管理客户端。

核心功能包括：
- **键值管理**：支持键值（Keys）的查看、编辑及配置查看编辑。
- **远程连接**：支持通过 SSH 隧道连接远程 Redis 服务器。
- **终端操作**：内置终端用于执行自定义命令。
- **格式支持**：支持 JSON 和 MessagePack 格式的查看、编辑，并提供内置高亮与验证。
- **高性能遍历**：利用 SCAN 命令高效处理海量键值，避免阻塞 Redis 服务器。
- **键组筛选**：提供模式管理器（Pattern Manager）方便筛选子键组。

支持 Windows 和 macOS 平台，兼容 Redis 2.8 及以上版本。