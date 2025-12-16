
---
title: moffee
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/wbopan/moffee?style=social) ](https://github.com/wbopan/moffee)
### [wbopan moffee](https://github.com/wbopan/moffee)

**项目功能**  
moffee 是一个开源工具，将 Markdown 文档转换为专业幻灯片，支持布局、分页和样式自动处理，用户专注内容创作。提供实时网页预览、PDF 导出功能，并内置多种主题（如 default、beam、robo 等）。

**使用方法**  
1. 安装：通过 `pipx install moffee` 或 `pip install moffee` 安装。  
2. 命令行操作：  
   - `moffee live example.md`：启动本地服务器预览幻灯片。  
   - `moffee make example.md -o output_html/`：导出为 HTML。  
3. Markdown 语法：  
   - 用 `##` 创建新幻灯片，`---` 触发分页，`<->` 水平布局，`===` 垂直布局。  
   - 通过 YAML 配置主题、背景颜色等（如 `theme: default`）。  
   - 使用 `@(layout=content)` 装饰器自定义单页样式。

**主要特性**  
- 简化语法：支持 Markdown 扩展语法（如 strikethrough、代码块等）。  
- 灵活布局：通过 `<->`/`===` 实现图文混排，自动适配内容比例。  
- 配置自由：支持全局 YAML 配置和局部装饰器，可自定义背景、颜色等。  
- 多主题支持：提供多种内置主题，满足不同场景需求。