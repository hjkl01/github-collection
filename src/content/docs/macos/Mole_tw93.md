
---
title: Mole
---

### [tw93 Mole](https://github.com/tw93/Mole)  ![GitHub Repo stars](https://img.shields.io/github/stars/tw93/Mole?style=social)

**Mole 核心内容总结：**

Mole 是一款专为 Mac 设计的深度清理与优化工具，整合了 CleanMyMac、AppCleaner 等多款工具的核心功能，提供统一的清理、卸载、系统优化和磁盘分析能力。  

**主要功能：**  
- **深度清理**：扫描并删除缓存、日志、浏览器残留文件，释放数十GB空间。  
- **智能卸载**：彻底移除应用及关联的隐藏残留文件（如 Launch Agents、偏好设置等）。  
- **磁盘分析**：可视化磁盘使用情况，管理大文件并重建缓存。  
- **实时监控**：展示 CPU、内存、磁盘、网络等系统状态，辅助性能诊断。  
- **项目清理**：一键清除开发环境中的构建残留文件（如 `node_modules`、`target` 等）。  

**使用方式：**  
- 安装：通过 `curl` 或 Homebrew 安装（`brew install tw93/tap/mole`）。  
- 命令行操作：支持 `mo clean`（清理）、`mo uninstall`（卸载）、`mo optimize`（优化）、`mo analyze`（分析）、`mo status`（监控）等子命令，可配合 `--dry-run`（预览）、`--whitelist`（白名单）等参数使用。  

**特性亮点：**  
- 支持 Touch ID 配置免密操作，内置安全审计机制。  
- 提供快速启动器（Raycast/Alfred）实现命令一键调用。  
- 兼容主流终端（如 Alacritty、WezTerm 等），支持 Vim 键位操作。