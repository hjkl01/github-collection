### [lazydev.nvim](https://github.com/folke/lazydev.nvim) ![GitHub Repo stars](https://img.shields.io/github/stars/folke/lazydev.nvim?style=social)

lazydev.nvim 是用于 Neovim 配置的 LuaLS 辅助插件，通过按需加载仅当前文件中 require/模块注解涉及的库来更新工作区，从而加快补全；可自动加载第三方 LLS-Addons 库，支持 nvim-cmp、blink.cmp、coq 的模块补全源，并修复 LuaLS 工作区管理。适用于 Neovim 0.10+，与 lazy.nvim 或原生包管理配合使用。