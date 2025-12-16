
---
title: gitlogue
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/unhappychoice/gitlogue?style=social) ](https://github.com/unhappychoice/gitlogue)
### [unhappychoice gitlogue](https://github.com/unhappychoice/gitlogue)

**gitlogue** 是一款用于终端的电影级 Git 提交回放工具，通过动画形式将 Git 历史转化为生动的视觉故事，支持真实打字动画、语法高亮、文件树转换等功能。

**功能与特性**  
- **动画回放**：展示提交记录中的代码变更，包含打字效果、删除操作、文件树过渡等。  
- **语法高亮**：支持 29 种编程语言（如 Python、Rust、JavaScript 等）的树状语法高亮。  
- **主题与自定义**：提供 9 种内置主题，支持自定义颜色和样式。  
- **屏保模式**：可无限循环播放随机提交，适合作为终端背景。  
- **高效性能**：基于 Rust 开发，运行轻快。  

**使用方法**  
- **安装**：可通过脚本、Homebrew、Cargo、Arch 包管理器或从源码编译安装。  
- **命令示例**：  
  - 启动屏保：`gitlogue`  
  - 回放特定提交：`gitlogue --commit abc123`  
  - 指定提交范围：`gitlogue --commit HEAD~5..HEAD`  
  - 设置主题与速度：`gitlogue --theme dracula --speed 20`  
  - 过滤提交：`gitlogue --author "john" --after "2024-01-01"`  

**注意事项**  
- 不具备传统屏保的电源管理功能，需手动控制播放。  
- OLED 显示器长期显示静态元素（如背景）可能导致烧屏风险，建议使用 LCD 屏幕。