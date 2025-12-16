
---
title: oxker
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/mrjackwills/oxker?style=social) ](https://github.com/mrjackwills/oxker)
### [mrjackwills oxker](https://github.com/mrjackwills/oxker)

**项目功能**  
oxker 是一个基于 Rust 的终端用户界面（TUI）工具，用于查看和控制 Docker 容器，支持容器管理、日志查看、命令执行等功能。

**使用方法**  
- **安装方式**：支持 Cargo、Docker（ghcr.io 和 Docker Hub）、Nix、AUR、Homebrew 及预编译二进制文件安装。  
- **运行命令**：`oxker`，支持通过快捷键（如 Tab 切换面板、Enter 执行命令、F1 过滤等）和命令行参数（如 `-d` 设置更新间隔、`-r` 显示原始日志等）自定义操作。  
- **配置文件**：通过 `config.toml`/`config.json` 等文件可自定义键位映射、颜色方案等设置，优先级高于命令行参数。

**主要特性**  
- 跨平台支持（x86_64、ARM64、ARMv6 等）。  
- 支持 Docker 容器日志实时查看、搜索及保存。  
- 提供丰富的快捷键和命令行参数，增强操作灵活性。  
- 可通过配置文件持久化设置，适配不同用户需求。  
- 构建支持本地编译及跨平台构建（如 Raspberry Pi）。  
- 测试覆盖基础功能，确保安全性（不影响运行容器）。