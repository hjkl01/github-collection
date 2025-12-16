
---
title: LazyVim
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/LazyVim/LazyVim?style=social) ](https://github.com/LazyVim/LazyVim)
### [LazyVim LazyVim](https://github.com/LazyVim/LazyVim)

**LazyVim 核心内容总结**  

**项目功能**  
LazyVim 是一个基于 Neovim 的配置框架，通过 [lazy.nvim](https://github.com/folke/lazy.nvim) 实现灵活的插件管理和配置扩展，兼具预配置便捷性与高度自定义能力，可将 Neovim 转变为功能完备的 IDE。  

**主要特性**  
- 基于 lazy.nvim 的插件管理，支持快速扩展和自定义  
- 内置合理默认设置（选项、自动命令、键位映射）  
- 预装大量常用插件，开箱即用  
- 高性能优化，运行速度快  

**使用方法**  
1. **安装**：通过 [LazyVim Starter 模板](https://github.com/LazyVim/starter) 初始化配置，或使用 Docker 快速体验。  
2. **配置**：替换原有 Neovim 配置文件，自定义插件逻辑（`lua/plugins/` 目录）及配置文件（`lua/config/` 目录）。  
3. **文档**：参考 [官方文档](https://lazyvim.github.io) 获取详细配置指南。  

**依赖要求**  
- Neovim 0.11.2+（需 LuaJIT 编译）  
- Git 2.19.0+（支持部分克隆）  
- C 编译器（用于 `nvim-treesitter`）  
- 可选：Nerd Font 字体