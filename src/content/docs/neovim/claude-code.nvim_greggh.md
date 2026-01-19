
---
title: claude-code.nvim
---

### [greggh claude-code.nvim](https://github.com/greggh/claude-code.nvim)  ![GitHub Repo stars](https://img.shields.io/github/stars/greggh/claude-code.nvim?style=social)

**项目核心内容总结：**

**功能**  
该插件将Anthropic的Claude Code AI助手集成到Neovim中，提供以下功能：  
- 通过快捷键一键在终端窗口中切换Claude Code  
- 支持`--continue`等命令行参数及自定义变体  
- 自动检测并重新加载Claude Code修改的文件  
- 实时同步外部文件变更到缓冲区  
- 可自定义窗口位置、大小（含浮动窗口）  
- 支持which-key集成及Git项目根目录作为工作目录  

**使用方法**  
- 安装方式支持lazy.nvim、packer.nvim、vim-plug  
- 配置项包含窗口设置、刷新规则、Git行为、命令参数、快捷键映射等  
- 启动命令：`:ClaudeCode` 或自定义快捷键（如 `<leader>cc`）  
- 提供`:ClaudeCodeContinue`、`:ClaudeCodeResume`等子命令管理对话  

**主要特性**  
- 基于Neovim 0.7+，依赖Claude Code CLI和plenary.nvim  
- 支持浮动窗口布局、多窗口导航（`<C-h/j/k/l>`）及页面滚动（`<C-f/b>`）  
- 内置44个测试用例的测试框架，代码含类型注解（LuaCATS）和配置校验  
- 开发者可自定义命令变体（如`--verbose`）、窗口样式（边框、比例等）  

**其他**  
- 项目完全由Claude Code构建，采用MIT许可证  
- 提供详细的贡献指南、开发环境配置及社区支持渠道