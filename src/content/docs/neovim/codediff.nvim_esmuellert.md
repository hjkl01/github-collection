
---
title: codediff.nvim
---

### [esmuellert codediff.nvim](https://github.com/esmuellert/codediff.nvim)  ![GitHub Repo stars](https://img.shields.io/github/stars/esmuellert/codediff.nvim?style=social)

### 项目总结：codediff.nvim

#### 项目简介
`codediff.nvim` 是一个为 Neovim 设计的插件，提供与 VSCode 类似的**侧边对比差异视图**，支持 Git 集成、语法高亮、异步操作等功能。插件使用 C 语言实现的高性能差异计算引擎，并通过 Lua FFI 调用，支持多核并行计算。

---

#### 主要功能

- **双层高亮系统**：
  - 行级高亮：插入（绿色）、删除（红色）使用 `DiffAdd` 和 `DiffDelete`。
  - 字符级高亮：精确到字符的差异高亮，颜色根据主题自动调整（暗色主题更亮，亮色主题更暗）。
  
- **Git 集成**：
  - 支持比较任意 Git 提交（HEAD、分支、标签）。
  - 异步 Git 操作，不阻塞 Neovim。
  - 支持文件历史查看（`CodeDiff history`），查看每个提交的更改。

- **文件对比模式**：
  - 支持任意两个文件或目录的对比。
  - 支持 Git merge 冲突解决。

- **交互式文件浏览器**：
  - 显示 Git 差异文件列表（新增、修改、删除）。
  - 支持树状或列表视图。

- **快捷键支持**：
  - 支持跳转到下一个/上一个修改块、切换文件、获取差异内容等操作。
  - 冲突解决快捷键支持选择当前或对方内容。

- **自动下载 C 库**：
  - 插件首次使用时自动下载对应平台的 C 库（无需手动编译）。
  - 支持手动安装或更新（`:CodeDiff install`）。

- **支持多种对比模式**：
  - 文件对比（`:CodeDiff file A B`）
  - 目录对比（`:CodeDiff dir A B`）
  - Git 提交对比（`:CodeDiff HEAD~2`）
  - PR 式对比（`:CodeDiff main...`，显示分支上的唯一更改）

- **Lua API**：
  - 提供 Lua 接口，支持自定义配置、差异计算、Git 文件获取等。

---

#### 使用方法

1. **安装**（推荐使用 `lazy.nvim`）：
   ```lua
   {
     "esmuellert/codediff.nvim",
     dependencies = { "MunifTanjim/nui.nvim" },
     cmd = "CodeDiff",
   }
   ```

2. **常用命令**：
   - `:CodeDiff`：打开 Git 差异文件浏览器。
   - `:CodeDiff file <file>`：对比当前文件与 Git 提交。
   - `:CodeDiff dir <dir1> <dir2>`：对比两个目录。
   - `:CodeDiff history`：查看提交历史。
   - `:CodeDiff merge <file>`：解决 Git merge 冲突。

3. **Git 集成**：
   - 配置为 Git 的 `difftool` 和 `mergetool`，支持 `git difftool` 和 `git mergetool`。

---

#### 特性亮点

- **高性能**：使用 C 实现的差异计算引擎，支持多核并行处理。
- **自动适配主题**：根据 Neovim 主题自动调整字符级高亮亮度。
- **异步非阻塞**：Git 文件获取和差异计算不阻塞编辑器。
- **冲突解决支持**：提供快捷键快速接受或拒绝冲突内容。
- **可定制性强**：支持自定义高亮颜色、快捷键、视图布局等。

---

#### 项目结构

- **C 模块**：差异计算核心逻辑（Myers 算法 + 字符级优化）。
- **Lua 层**：FFI 接口、UI 渲染、Git 操作、命令处理。
- **测试支持**：包含 C 单元测试和 Lua 集成测试。

---

#### 未来计划

- [ ] 增加行内差异模式（单缓冲区视图）
- [ ] 支持折叠大差异块