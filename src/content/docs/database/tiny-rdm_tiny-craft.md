
---
title: tiny-rdm
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/tiny-craft/tiny-rdm?style=social) ](https://github.com/tiny-craft/tiny-rdm)
### [tiny-craft tiny-rdm](https://github.com/tiny-craft/tiny-rdm)

**项目功能**  
Tiny RDM 是一款现代轻量级跨平台 Redis 桌面管理工具，支持 Mac、Windows 和 Linux 系统。提供可视化界面管理 Redis 数据（如字符串、列表、哈希等），支持 SSH 隧道、SSL、集群、哨兵模式等连接方式，具备命令历史记录、实时监控、数据导入导出、发布订阅等功能。集成 Monaco 编辑器，支持自定义数据编解码器。

**使用方法**  
可从 GitHub 发布页免费下载安装包。Mac 用户若安装后无法打开，需执行命令 `sudo xattr -d com.apple.quarantine /Applications/Tiny\ RDM.app`。开发者可通过 Go、Node.js 等工具构建项目，执行 `wails dev` 启动开发环境。

**主要特性**  
- 基于 Webview2 构建，无嵌入浏览器，轻量高效；  
- 支持明暗主题、多语言（含中文、日文）；  
- 支持分段加载百万级键值、多种数据格式解码；  
- 提供慢日志、命令行模式、连接配置导入导出；  
- 集成 Monaco 编辑器，支持实时命令监控。