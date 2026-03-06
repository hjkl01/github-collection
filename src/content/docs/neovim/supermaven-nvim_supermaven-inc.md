
---
title: supermaven-nvim
---

### [supermaven-inc supermaven-nvim](https://github.com/supermaven-inc/supermaven-nvim)  ![GitHub Repo stars](https://img.shields.io/github/stars/supermaven-inc/supermaven-nvim?style=social)

这是一个 Neovim 插件，用于在编辑器内集成 Supermaven AI 代码智能补全服务。主要功能包括：
- **安装与配置**：支持 lazy.nvim 和 packer.nvim 安装，可自定义快捷键、忽略特定文件类型、提示颜色及日志级别。
- **集成扩展**：原生兼容 nvim-cmp 补全来源与 lspkind 图标显示，提供 Lua API 实现程序化建议处理。
- **服务管理**：提供命令行和 API 接口控制插件启停、切换免费或专业版账号、退出登录及管理日志。
- **条件控制**：支持通过条件函数动态禁用插件，适应特定文件场景。