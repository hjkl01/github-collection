
---
title: uosc
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/tomasklaen/uosc?style=social) ](https://github.com/tomasklaen/uosc)
### [tomasklaen uosc](https://github.com/tomasklaen/uosc)

**uosc项目核心内容总结：**

uosc是为mpv媒体播放器设计的简约用户界面工具，提供以下核心功能：
1. **快捷键与菜单管理**：通过`input.conf`文件配置快捷键，支持注释语法定义菜单项（如`#! 菜单项标题`），可嵌套多级子菜单。
2. **功能扩展**：支持控制音量、播放列表、字幕加载、音轨切换、截图、修改画幅比例等操作，部分功能依赖跨平台二进制工具ziggy（需Go环境构建）。
3. **脚本交互**：通过`script-message-to uosc`命令实现子菜单调用，支持模糊显示（不预选第一项）。
4. **本地化与多平台**：支持多语言本地化，发布包包含Windows/macOS/Linux的二进制文件，可跨平台使用。
5. **安全提示**：部分杀毒软件可能误报二进制文件，用户可通过源码自行构建确认安全性。

**使用方法**：
- 在`input.conf`中配置快捷键并添加`#!`注释定义菜单项。
- 使用`script-message-to`命令调用uosc功能。
- 安装跨平台二进制文件或自行构建ziggy工具处理字幕等高级功能。