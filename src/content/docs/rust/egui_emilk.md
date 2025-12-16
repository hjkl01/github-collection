
---
title: egui
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/emilk/egui?style=social) ](https://github.com/emilk/egui)
### [emilk egui](https://github.com/emilk/egui)

**项目核心内容总结：**

egui 是一个用 Rust 编写的即时模式图形用户界面（Immediate Mode GUI）库，适用于多种平台和后端。它主要用于构建交互式界面，支持与 3D 图形库结合使用。egui 的设计目标是简单、高效，适合嵌入到游戏引擎或其他图形应用中。

**主要功能：**

- 提供丰富的 UI 控件（如按钮、输入框、滑块等）。
- 支持自定义绘制，包括使用回调函数进行 3D 渲染。
- 可以与多种图形后端集成，如 eframe、bevy_egui、egui-miniquad 等。
- 支持跨平台，包括 Web、桌面和移动端。

**使用方法：**

- 通过 `eframe` 使用 egui 时，可以快速构建一个独立的 Web 或桌面应用。
- 在游戏引擎中，例如 Bevy，可以通过 `bevy_egui` 插件集成 egui。
- 支持使用 `Shape::Callback` 实现自定义 3D 渲染，或通过纹理渲染将 3D 内容嵌入 UI。

**主要特性：**

- 使用即时模式 GUI，避免了传统 GUI 的复杂状态管理。
- 简洁的 API，使用构建器模式和闭包实现 UI 元素的创建。
- 高效的性能，适合实时应用。
- 支持多种输入设备（如触摸屏、键盘等）。
- 提供良好的跨平台支持，包括 Web、桌面和移动设备。
- 支持中文及其他语言的界面显示。
- 有活跃的社区和丰富的第三方扩展支持。

**总结：**

egui 是一个轻量、高效、跨平台的即时模式图形界面库，适合用于构建交互式 UI，特别适合嵌入到游戏引擎或图形应用中。它提供了丰富的功能和灵活的扩展方式，适用于多种应用场景。