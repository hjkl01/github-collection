
---
title: xxh
---

### [xxh xxh](https://github.com/xxh/xxh)  ![GitHub Repo stars](https://img.shields.io/github/stars/xxh/xxh?style=social)

xxh 是一个通过 SSH 将用户自定义 Shell 环境便携至远程服务器的工具，客户端兼容多种系统，无需远程主机 root 权限或安装。

核心特性：
1. **便携隔离**：Shell 和插件在本地构建后上传，远程环境隔离于 `~/.xxh` 目录，删除即可恢复主机原状。
2. **多 Shell 支持**：支持 xonsh、zsh、fish、bash、osquery 等，可灵活按需切换。
3. **高度扩展**：支持集成 Docker、Python、Dotfiles 等插件及自定义便携式工具入口。
4. **无缝集成**：命令兼容 SSH 用法，支持多种安装方式及本地无 SSH 连接运行。

该项目主要面向 Linux x86_64 主机，旨在提供一致且隔离的交互式体验。