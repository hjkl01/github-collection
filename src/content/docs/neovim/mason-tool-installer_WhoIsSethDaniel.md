
---
title: mason-tool-installer
---

### [WhoIsSethDaniel mason-tool-installer](https://github.com/WhoIsSethDaniel/mason-tool-installer)  ![GitHub Repo stars](https://img.shields.io/github/stars/WhoIsSethDaniel/mason-tool-installer?style=social)

mason-tool-installer 是一个基于 Mason 的 Neovim 插件，用于安装或升级第三方工具，以确保开发环境的一致性。

主要功能：
1. 支持启动时自动安装/更新配置的工具，也支持通过命令（:MasonToolsInstall、:MasonToolsUpdate、:MasonToolsClean）手动操作。
2. 支持灵活配置需安装的工具列表，可指定版本、目标架构、条件安装、单工具自动更新开关及安装防抖动时间。
3. 可选集成 mason-lspconfig、mason-null-ls、mason-nvim-dap，允许使用对应模块的工具名称。
4. 提供安装开始（MasonToolsStartingInstall）和完成（MasonToolsUpdateCompleted）的用户事件通知。

依赖要求：必须安装并配置 Mason。