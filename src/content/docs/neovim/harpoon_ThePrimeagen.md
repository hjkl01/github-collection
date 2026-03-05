
---
title: harpoon
---

### [ThePrimeagen harpoon](https://github.com/ThePrimeagen/harpoon)  ![GitHub Repo stars](https://img.shields.io/github/stars/ThePrimeagen/harpoon?style=social)

Harpoon 是一款适用于 Neovim 的 Lua 插件，旨在通过最少的按键实现快速导航与管理。核心功能总结如下：

1. **文件标记与导航**：允许快速标记项目中的常用文件，支持列表查看、重新排序、删除及通过快捷键快速切换；支持在垂直分屏、水平分屏或新标签页中打开文件。
2. **终端管理**：支持管理多个持久化终端，可导航至指定索引的终端（不存在则自动创建），支持向指定终端发送命令或调用预设的常用命令。
3. **Tmux 集成**：原生支持 Tmux，可导航 Tmux 窗口或 Pane 并发送命令，提供切换回 Neovim 的脚本集成。
4. **扩展兼容**：支持注册为 Telescope 扩展，可在 Telescope 界面中管理文件标记。
5. **灵活配置**：支持自定义保存策略（如切换时保存）、排除特定文件类型、按 Git 分支隔离标记、Tabline 显示集成、动态菜单宽度设置及日志记录等级配置。