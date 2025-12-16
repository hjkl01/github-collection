
---
title: hardtime.nvim
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/m4xshen/hardtime.nvim?style=social) ](https://github.com/m4xshen/hardtime.nvim)
### [m4xshen hardtime.nvim](https://github.com/m4xshen/hardtime.nvim)

**hardtime.nvim** 是一个 Neovim 插件，旨在帮助用户纠正不良键盘习惯，提升 Vim 操作效率。其核心功能包括：

1. **阻止重复按键**：在短时间内重复按键时进行限制，避免误操作。
2. **操作提示**：提供 Vim 操作建议（如用 `5j` 代替 `↓`），帮助用户学习更高效的操作方式。
3. **坏习惯报告**：记录并展示用户最常使用的低效按键组合。

**使用方法**：
- 安装需 Neovim 0.10+，通过包管理器（如 lazy.nvim）安装后，执行 `require("hardtime").setup()` 初始化。
- 默认启用，可通过 `:Hardtime enable/disable/toggle` 控制插件状态，用 `:Hardtime report` 查看报告，日志存储在 `~/.local/state/nvim/hardtime.nvim.log`。

**配置选项**：
- 可自定义禁用按键（如 `disabled_keys`）、文件类型（`disabled_filetypes`）、提示信息（`hints`）等。
- 支持调整重复按键限制时间（`max_time`）、最大重复次数（`max_count`）、通知显示方式（`notification`）等参数。

**主要特性**：
- 推荐使用 Vim 高效操作（如相对跳转、括号跳转等）。
- 提供灵活的配置选项，适配不同用户习惯。