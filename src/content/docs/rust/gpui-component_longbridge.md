
---
title: gpui-component
---

### [longbridge gpui-component](https://github.com/longbridge/gpui-component)

GPUI Component 是一个基于 GPUI 的跨平台桌面应用 UI 组件库，提供 60+ 跨平台组件，支持 macOS 和 Windows 原生控件风格与现代设计结合。主要特性包括：多主题定制、灵活布局（支持 Dock 和 Tiles 布局）、高性能虚拟化表格/列表、Markdown 和 HTML 渲染、内置图表、支持 20 万行代码的高性能编辑器（含 LSP 和语法高亮）。  

使用方法需在 Cargo.toml 中添加 `gpui` 和 `gpui-component` 依赖，并通过 `init(cx)` 初始化组件。示例代码展示如何创建窗口并渲染基础界面。WebView 功能需启用 `webview` 特性并依赖 Wry。图标需自行添加 SVG 文件，命名需符合预定义规则。  

项目对比其他框架（如 Iced、egui、Qt）的优势包括更小的二进制体积、更好的 CJK 支持、虚拟化表格列调整功能，以及更完善的 Markdown 和 HTML 混排支持。许可证为 Apache-2.0。