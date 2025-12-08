
---
title: nvim-tree.lua
---

### [nvim-tree nvim-tree.lua](https://github.com/nvim-tree/nvim-tree.lua)

### 项目概述

**项目名称**：为 Neovim 编写的 Lua 文件管理器（`nvim-tree`）  
**功能特性**：
- 自动更新文件内容
- 支持文件类型图标显示
- 集成 Git 功能
- 支持 LSP 和 COC 的诊断功能
- 实时过滤功能
- 提供剪切、复制、粘贴、重命名、删除、创建等操作
- 高度可定制化

---

### 系统要求

- **Neovim 版本**：需 ≥ 0.9.0  
- **可选插件**：`nvim-web-devicons`（用于显示文件图标）  
- **推荐配置**：禁用 Neovim 的默认文件管理器 `netrw`（通过设置 `vim.g.loaded_netrw = 1` 和 `vim.g.loaded_netrwPlugin = 1`）

---

### 安装方式

- 通过包管理器安装（如 `packer.nvim`、`vim-plug` 等）  
- 支持通过版本标签指定安装版本（如 `v1`、`v1.23`）

---

### 快速入门

1. **配置 `init.lua`**：
   ```lua
   -- 禁用 netrw
   vim.g.loaded_netrw = 1
   vim.g.loaded_netrwPlugin = 1

   -- 启用 24 位颜色
   vim.opt.termguicolors = true

   -- 初始化插件
   require("nvim-tree").setup()
   ```

2. **自定义配置**（如设置排序方式、视图宽度、过滤规则等）：
   ```lua
   require("nvim-tree").setup({
     sort = { sorter = "case_sensitive" },
     view = { width = 30 },
     renderer = { group_empty = true },
     filters = { dotfiles = true }
   })
   ```

3. **自定义快捷键**（通过 `on_attach` 配置）：
   ```lua
   require("nvim-tree").setup({
     on_attach = function(bufnr)
       local api = require("nvim-tree.api")
       local opts = { buffer = bufnr, noremap = true, silent = true, nowait = true }
       vim.keymap.set("n", "<C-t>", api.tree.change_root_to_parent, opts)
       vim.keymap.set("n", "?", api.tree.toggle_help, opts)
     end
   })
   ```

4. **高亮自定义**：
   ```vim
   :hi NvimTreeExecFile guifg=#ffa0a0
   :hi NvimTreeSpecialFile guifg=#ff80ff gui=underline
   :hi NvimTreeSymlink guifg=Yellow gui=italic
   :hi link NvimTreeImageFile Title
   ```

---

### 常用命令

- `:NvimTreeToggle`：打开/关闭文件树（可选路径参数）
- `:NvimTreeFocus`：打开文件树并聚焦
- `:NvimTreeFindFile`：跳转到当前文件的路径
- `:NvimTreeCollapse`：递归折叠文件树

---

### 开发与贡献

- **路线图**：项目已稳定，未来重点是错误修复、性能优化、用户体验改进及 API 扩展。
- **API 支持**：提供公共 API，支持用户自定义功能扩展。
- **贡献方式**：欢迎参与贡献，详情参考 [CONTRIBUTING.md](https://github.com/nvim-tree/nvim-tree.lua/blob/master/CONTRIBUTING.md)

---

### 版权信息

- **许可证**：MIT 许可证（详情见 [LICENSE](https://github.com/nvim-tree/nvim-tree.lua/blob/master/LICENSE)）  
- **文档与支持**：查看 [Wiki](https://github.com/nvim-tree/nvim-tree.lua/wiki) 获取更多使用技巧和资源。