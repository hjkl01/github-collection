
---
title: delta
---

### [dandavison delta](https://github.com/dandavison/delta)

**核心内容总结：**

Delta 是一个用于 Git、diff 和 grep 输出的语法高亮分页器，旨在提升代码差异查看体验。其主要功能包括：  
1. **语法高亮**：支持与 [bat](https://github.com/sharkdp/bat) 相同的主题，可自定义颜色和样式。  
2. **差异化展示**：支持词级差异高亮、侧边对比视图（可自动换行）、行号显示。  
3. **交互优化**：通过 `n/N` 快捷键在大型差异中导航，支持 Git 合并冲突、blame 信息的增强显示。  
4. **兼容性**：兼容传统 unified diff 格式，支持 Git 的 `--color-moved` 功能，可复制代码内容。  
5. **链接支持**：提交哈希和文件路径可格式化为终端超链接（支持 GitHub、GitLab 等平台）。  

**使用方法**：  
- 安装后，通过修改 `~/.gitconfig` 配置文件，设置 `core.pager = delta`、`interactive.diffFilter = delta --color-only` 等参数。  
- 支持命令行直接配置，如 `git config --global core.pager delta`。  
- 可通过 `delta --help` 查看详细用法及自定义选项。  

**主要特性**：  
- 支持多种主题（如 Dracula、GitHub）的语法高亮。  
- 侧边对比视图与行号显示可独立开启。  
- 支持 ripgrep、git grep 的输出高亮。  
- 提供与 `diff-highlight`、`diff-so-fancy` 的兼容模式。