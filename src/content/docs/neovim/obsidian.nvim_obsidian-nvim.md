
---
title: obsidian.nvim
---

### [obsidian-nvim obsidian.nvim](https://github.com/obsidian-nvim/obsidian.nvim)  ![GitHub Repo stars](https://img.shields.io/github/stars/obsidian-nvim/obsidian.nvim?style=social)

obsidian.nvim 是一个用于 Neovim 的插件，旨在为 Obsidian 笔记系统提供写作和导航功能。它使用 Lua 编写，适合喜欢 Obsidian 的 Markdown 笔记方式，但更喜欢使用 Neovim 的用户。该项目是原项目的社区分支，因其长期未维护而由社区接手并继续开发。

### 项目功能
- **补全功能**：支持超快速、异步的笔记引用和标签补全，支持 `nvim-cmp` 或 `blink.cmp`。
- **导航功能**：可在笔记库中通过链接、反向链接、标签等导航。
- **图片粘贴**：支持将图片粘贴到笔记中。
- **状态显示**：在底部显示笔记状态，类似 Obsidian 应用。
- **命令支持**：提供大量命令用于笔记管理，如创建新笔记、搜索、切换工作区等。
- **工作区管理**：支持多个工作区配置，便于管理不同用途的笔记库。

### 使用方法
1. **安装依赖**：
   - Neovim >= 0.10.0
   - ripgrep（用于搜索）
   - 系统相关依赖（如 Windows WSL 用户需 `wsl-open`，Mac 用户需 `pngpaste`，Linux 用户需 `xclip` 或 `wl-clipboard`）

2. **安装插件**（以 `lazy.nvim` 为例）：
   ```lua
   return {
     "obsidian-nvim/obsidian.nvim",
     version = "*",
     ft = "markdown",
     opts = {
       workspaces = {
         {
           name = "personal",
           path = "~/vaults/personal",
         },
       },
     },
   }
   ```

3. **配置插件**：通过 `require"obsidian".setup()` 自定义配置。

4. **使用命令**：
   - `:Obsidian new`：创建新笔记
   - `:Obsidian open`：在 Obsidian 应用中打开当前笔记
   - `:Obsidian today`：打开/创建当天的每日笔记
   - `:Obsidian dailies`：列出每日笔记
   - `:Obsidian search`：搜索笔记
   - `:Obsidian help`：查看帮助文档

### 主要特性
- **快速补全**：支持链接和标签的自动补全。
- **高效导航**：支持通过链接、反向链接、标签等方式快速跳转。
- **多工作区支持**：可配置多个工作区，管理不同用途的笔记。
- **图片处理**：支持从剪贴板粘贴图片到笔记中。
- **命令丰富**：提供大量命令用于创建、搜索、管理笔记。
- **社区维护**：由于原项目不再维护，社区接手后增加了对新工具和功能的支持。

### 依赖项
- **补全工具**：`nvim-cmp` 或 `blink.cmp`
- **选择器**：`telescope.nvim`、`fzf-lua`、`mini.pick`、`snacks.picker`
- **图像查看器**：`snacks.image`
- **语法高亮**：`nvim-treesitter`、`vim-markdown`、`render-markdown.nvim`、`markview.nvim`

该项目旨在为 Obsidian 提供 Neovim 的替代方案，虽不能完全替代 Obsidian 的功能，但能与之互补，为 Neovim 用户提供高效的笔记体验。