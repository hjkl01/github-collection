
---
title: neogit
---

### [NeogitOrg neogit](https://github.com/NeogitOrg/neogit)  ![GitHub Repo stars](https://img.shields.io/github/stars/NeogitOrg/neogit?style=social)

### 项目简介

**Neogit** 是一个为 [Neovim](https://neovim.io) 设计的 Git 界面，灵感来源于 [Magit](https://magit.vc)。它提供了一个强大的、可定制的 Git 操作界面，适合在 Neovim 中高效地进行版本控制。

---

### 核心功能

- **Git 界面集成**：在 Neovim 中提供类似 Magit 的 Git 操作界面。
- **支持多种弹窗操作**：包括分支管理、提交、合并、拉取、推送、重置、标签、补丁等。
- **可视化 Git 提交历史**：支持 ASCII、Unicode、Kitty 风格的提交图。
- **自定义配置**：提供大量配置选项，包括界面样式、快捷键、提交编辑器行为等。
- **插件集成**：支持与 Telescope、FZF、Diffview 等插件集成。
- **自动刷新**：自动监控 `.git/` 目录变化并刷新状态。
- **事件支持**：支持 Git 操作的事件回调，方便插件扩展。

---

### 使用方法

1. **安装**：使用 Lazy 等插件管理器安装。
2. **命令使用**：
   - `:Neogit` 打开 Git 界面。
   - `:Neogit commit` 直接打开提交界面。
   - 支持 `tab`、`split`、`floating` 等方式打开界面。
3. **快捷键映射**：可自定义快捷键，如 `<leader>gg` 打开 Git 界面。
4. **Lua API**：支持通过 Lua 脚本控制 Neogit 的打开方式和参数。

---

### 主要特性

- **弹窗操作**：支持多种 Git 操作弹窗（如 Commit、Branch、Rebase、Merge、Pull、Push 等）。
- **提交编辑器**：支持在编辑器中编写提交信息，并显示已暂存的更改。
- **Git 服务集成**：支持 GitHub、GitLab、Bitbucket 等平台的 URL 生成。
- **高亮样式**：支持自定义高亮样式（斜体、粗体、下划线等）。
- **多窗口支持**：支持多种窗口布局，如分割、浮动窗口。
- **自动刷新与监听**：自动监听 Git 状态变化，保持界面更新。
- **快捷键映射**：提供丰富的快捷键，支持自定义。
- **兼容性好**：兼容 Neovim 0.10+，并持续更新以适配最新版本。

---

### 适用人群

适用于使用 Neovim 并希望通过命令行方式高效管理 Git 的开发者。尤其适合对 Magit 有一定使用经验的用户。