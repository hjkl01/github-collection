### [WhoIsSethDaniel mason-tool-installer](https://github.com/WhoIsSethDaniel/mason-tool-installer)  ![GitHub Repo stars](https://img.shields.io/github/stars/WhoIsSethDaniel/mason-tool-installer?style=social)

mason-tool-installer.nvim 是一个基于 Mason 的 Neovim 插件，用于自动安装和升级第三方开发工具以维持环境一致性。

核心功能：
1. **工具管理**：支持启动时自动或手动执行命令，进行工具的安装、更新及清理。
2. **灵活配置**：可指定工具版本、目标架构、自动更新策略及条件安装逻辑。
3. **多生态兼容**：集成 mason-lspconfig、mason-null-ls、mason-nvim-dap，支持使用对应工具名进行配置。
4. **事件与防抖**：提供安装开始与完成的用户事件钩子，支持防抖设置以避免频繁重复安装。