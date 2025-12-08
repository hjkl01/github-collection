
---
title: lazygit
---

### [jesseduffield lazygit](https://github.com/jesseduffield/lazygit)

**核心内容总结：**

Lazygit 是一个基于 Go 语言开发的 Git 图形化界面工具，用于在终端中交互式地管理 Git 仓库。它提供了丰富的功能，包括分支管理、提交记录查看、差异对比、文件修改、提交操作等。用户可以通过键盘快捷键进行操作，界面简洁直观，支持自定义命令和分页器，同时也支持 Gitflow 工作流。

**使用方法：**  
在 Git 仓库目录中运行 `lazygit` 命令即可启动。用户还可以通过设置别名（如 `alias lg='lazygit'`）简化调用。

**主要特性：**  
- 支持 Git 的基本操作，如提交、分支切换、合并、变基等；
- 提供图形化界面，支持键盘快捷键操作；
- 支持 Gitflow 工作流；
- 支持自定义命令和分页器；
- 可通过 `--debug` 和 `--logs` 参数进行调试；
- 支持多种操作系统，包括 Linux、macOS、Windows 等；
- 可通过 Go 安装，也提供多种包管理工具的安装方式（如 Homebrew、Chocolatey、Conda、Nix 等）；
- 支持退出时自动切换目录（通过自定义脚本实现）；
- 提供撤销和重做功能。