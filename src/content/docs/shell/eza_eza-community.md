
---
title: eza
---

### [eza-community eza](https://github.com/eza-community/eza)  ![GitHub Repo stars](https://img.shields.io/github/stars/eza-community/eza?style=social)

**项目核心内容总结：**  
eza 是 `ls` 命令的现代替代工具，提供更丰富的功能和更友好的默认设置。它通过颜色区分文件类型和元数据，支持符号链接、扩展属性、Git 状态、SELinux 上下文输出、可读的相对日期等。特点包括：修复 exa 的历史问题、支持超链接、自定义主题（通过 `theme.yml` 文件配置颜色和图标）、单个二进制文件、跨平台（Windows/macOS/Linux）。

**使用方法：**  
- 通过 Nix 安装：`nix run github:eza-community/eza`  
- 支持多种命令行选项（如 `--long` 显示详细信息、`--tree` 树形展示、`--git` 显示 Git 状态等）。  
- 安装方式详见 [INSTALL.md](INSTALL.md)，支持主流平台和发行版。  

**主要特性：**  
- 修复 exa 的“网格错误”等历史问题；  
- 支持超链接、SELinux 上下文、Git 仓库状态；  
- 可自定义颜色、图标及主题；  
- 提供多种排序、过滤、显示模式（如列表、网格、树形）；  
- 跨平台、单文件、性能高效。