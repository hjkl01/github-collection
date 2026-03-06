
---
title: Gooey
---

### [chriskiehl Gooey](https://github.com/chriskiehl/Gooey)  ![GitHub Repo stars](https://img.shields.io/github/stars/chriskiehl/Gooey?style=social)

Gooey 是一个 Python 3 库，用于将基于 argparse 的控制台程序快速转换为图形界面（GUI）应用程序。

核心功能如下：

1.  **一键转换**：通过在 `main` 函数添加 `@Gooey` 装饰器，自动将命令行参数解析映射为 GUI 界面。
2.  **丰富组件**：支持文件选择、日期时间、密码框、滑块等多种控件；可通过 `GooeyParser` 替代标准 `ArgumentParser` 以自定义输入控件类型。
3.  **高度定制**：提供多种布局模式（高级/基本/无配置），支持多语言国际化、自定义图标、颜色主题、导航样式（侧边栏或标签页）及菜单栏配置。
4.  **高级特性**：包含输入动态验证、程序生命周期事件钩子（成功/失败回调）、控制台进度条监控及菜单自定义功能。
5.  **便捷部署**：支持使用 PyInstaller 打包为独立可执行文件。

适用场景：适合为普通用户或办公环境开发的“运行即完成”型脚本和工具，不适用于需要复杂管道输出的命令行工具。