
---
title: astrocommunity
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/AstroNvim/astrocommunity?style=social) ](https://github.com/AstroNvim/astrocommunity)
### [AstroNvim astrocommunity](https://github.com/AstroNvim/astrocommunity)

**项目功能**：AstroNvim社区仓库为AstroNvim（NeoVim配置）提供插件配置规范，整合社区贡献的插件，帮助管理插件的使用和设置。

**使用方法**：  
1. 在`lua/community.lua`中导入社区插件（如`"AstroNvim/astrocommunity"`及具体模块）。  
2. 通过自定义插件选项（如`opts`）调整插件行为，例如禁用功能、修改集成设置等。  
3. 使用完整仓库路径（而非简写）确保配置准确性。

**主要特性**：  
- 支持禁用插件或覆盖默认设置（如`enabled = false`）。  
- 允许通过`opts`自定义插件的集成选项（如`noice`、`cmp`等）。  
- 提供贡献指南，社区可提交插件配置以扩展仓库内容。