### [ibhagwan fzf-lua](https://github.com/ibhagwan/fzf-lua)  ![GitHub Repo stars](https://img.shields.io/github/stars/ibhagwan/fzf-lua?style=social)

fzf-lua 是一款基于 Lua 编写的 Neovim 插件，提供基于 fzf 或 skim 的模糊搜索界面，旨在实现开箱即用和高度可定制。

核心功能：
- **文件与缓冲管理**：搜索文件、打开缓冲、历史记录、标签页、参数列表及缓冲区行内容。
- **搜索与导航**：实时/静态 Grep、项目级搜索、LSP 符号（定义/引用/实现）、工作区及文档符号。
- **Git 集成**：管理 Git 状态、提交历史、分支、Diff、Hunks、Blame 及 Stash。
- **调试与系统**：支持 nvim-dap 调试命令、Tmux 缓冲区、Zoxide 目录跳转及拼写检查。
- **命令与配置**：执行 Neovim 命令、查找命令历史、切换颜色方案、修改选项及键位映射。
- **插入模式补全**：提供路径、文件及行文本的模糊补全功能。

界面与定制：
- **预览支持**：内置预览（语法高亮、Treesitter、Markdown）、外部预览器（bat、git-delta）及图片终端预览。
- **高度可定制**：支持配置窗口布局、UI 选项、动作绑定、颜色方案及 Fzf 选项。
- **预设配置**：提供多种 Profile（如 fzf-native, telescope, fzf-vim）及组合配置。
- **API 扩展**：实现 `vim.ui.select` 接口，支持 nvim-dap 等扩展功能。