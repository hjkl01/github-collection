
---
title: xxh
---

### [xxh xxh](https://github.com/xxh/xxh)  ![GitHub Repo stars](https://img.shields.io/github/stars/xxh/xxh?style=social)

xxh 是一款通过 SSH 在远程主机上部署便携 Shell 环境的工具，无需远程 root 权限或系统安装。它支持 xonsh、zsh、fish、bash、osquery 等多种 Shell，允许用户将本地配置、插件和工具无缝迁移至任何远程位置。

核心功能：
1. **零安装**：环境在本地构建并上传，远程主机无需修改或安装软件。
2. **环境隔离**：远程会话独立于宿主环境，清理 `~/.xxh` 目录即可完全恢复原状。
3. **多 Shell 支持**：可根据任务需求轻松切换不同 Shell（如 xonsh 用于 Python 开发，zsh/fish 用于日常）。
4. **插件化扩展**：支持 Prerun 插件及自定义入口，可携带 Dotfiles、Python 环境、Docker 等工具。
5. **兼容 SSH**：命令用法与 ssh 类似，保留原有 SSH 参数支持，可直接替换。
6. **本地模式**：支持在无法 SSH 但拥有 Shell 访问权限的本地环境中构建环境（`xxh local`）。