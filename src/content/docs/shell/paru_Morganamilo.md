
---
title: paru
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/Morganamilo/paru?style=social) ](https://github.com/Morganamilo/paru)
### [Morganamilo paru](https://github.com/Morganamilo/paru)

**项目功能**  
Paru 是一个功能丰富的 AUR（Arch User Repository）助手，基于 pacman 封装，提供交互式安装、升级、搜索等操作，支持自定义配置和高级功能。

**使用方法**  
1. 安装：需先安装 `base-devel`，克隆 Paru 仓库后执行 `makepkg -si`。  
2. 常用命令：  
   - `paru <目标>`：交互式搜索并安装软件包。  
   - `paru -S <目标>`：安装指定包。  
   - `paru -Sua`：升级 AUR 软件包。  
   - `paru -Qua`：查看 AUR 可用更新。  
   - `paru --gendb`：生成数据库以跟踪 `-git` 包。  

**主要特性**  
- 支持 `pacman.conf` 中启用颜色显示。  
- 可通过 `paru.conf` 配置文件管理器（FileManager）、搜索顺序（BottomUp）等选项。  
- 允许编辑 PKGBUILD 文件并持久化修改。  
- 提供 `bat` 工具语法高亮支持。  
- 跟踪 `-git` 包的上游仓库更新。