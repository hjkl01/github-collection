
---
title: serie
---

### [lusingander serie](https://github.com/lusingander/serie)

**项目核心内容总结：**  
Serie 是一个基于终端的 Git 提交历史查看工具，支持查看提交列表、详细信息、引用（refs）及搜索功能。用户可通过自定义命令（如 `git diff`）扩展功能，并支持多种终端（如 iTerm2、kitty）的图像协议。主要特性包括：  
1. **自定义命令**：通过配置 `keybind` 和 `core.user_command` 实现外部工具调用（如查看 diff）。  
2. **终端兼容性**：支持 iTerm2、kitty 等终端的图像显示协议，不兼容 Sixel 图形及终端多路复用器（如 tmux）。  
3. **界面配置**：提供颜色、字体、布局等 UI 设置，支持键盘快捷键操作。  
4. **功能扩展**：允许通过变量（如 `{{target_hash}}`）动态替换命令参数，适配不同显示区域尺寸。  

**使用方法**：  
- 安装后通过终端启动，使用预设快捷键（如 `d`）调用自定义命令。  
- 配置 `keybind` 和 `core.user_command` 实现功能扩展。  
- 支持通过 `color` 和 `ui` 配置项调整界面显示效果。