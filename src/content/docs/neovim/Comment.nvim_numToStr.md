
---
title: Comment.nvim
---

### [numToStr Comment.nvim](https://github.com/numToStr/Comment.nvim)

**Comment.nvim** 是一款为 Neovim 设计的智能注释插件，支持以下核心功能：

- **注释方式**：支持行注释（`//`）和块注释（`/* */`），兼容 `commentstring` 自定义注释格式。
- **操作特性**：支持 `gcc`/`gbc` 快捷键切换注释、计数（如 `[count]gcc`）、重复操作（`.`）、文本对象（如 `gci{`）和多方向运动（如 `gcw`、`gc$`）。
- **高级功能**：提供预处理/后处理钩子（`pre_hook`/`post_hook`），支持通过 Lua 正则忽略特定行，集成 Treesitter 解析注释格式（部分语言如 JSX 需额外配置）。
- **配置灵活**：可通过 Lua 脚本自定义映射键、注释格式、忽略规则等，支持多种安装方式（lazy.nvim、packer.nvim、vim-plug）。

**使用方法**：
1. 安装插件后调用 `require('Comment').setup()` 初始化。
2. 默认映射：`gcc`/`gbc` 切换单行注释，`gc`/`gb` 在可视模式下注释选区。
3. 高级操作：`gco`/`gcO`/`gcA` 插入注释并进入编辑模式，`pre_hook` 可集成 Treesitter 上下文注释。

**适用场景**：适用于需要高效注释代码的 Neovim 用户，尤其适合多语言开发环境和需要自定义注释规则的场景。