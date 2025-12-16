
---
title: iced
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/iced-rs/iced?style=social) ](https://github.com/iced-rs/iced)
### [iced-rs iced](https://github.com/iced-rs/iced)

**项目核心内容总结：**  
Iced 是一个用于 Rust 的跨平台 GUI 库，专注于简单性和类型安全性，灵感来自 Elm。其主要功能包括：  
- **跨平台支持**：兼容 Windows、macOS、Linux 和 Web。  
- **响应式编程模型**：通过状态（State）、消息（Messages）、视图逻辑（View）和更新逻辑（Update）四部分分离设计，实现类型安全的交互。  
- **模块化架构**：提供渲染器无关的运行时、基于 `wgpu` 和 `tiny-skia` 的渲染器，以及窗口管理模块。  
- **内置功能**：支持文本输入、滚动视图等常用小部件，可自定义组件；提供调试性能指标的覆盖层。  
- **异步支持**：兼容 Rust 的异步操作（如 `futures`）。  

**使用方法**：  
通过定义状态、消息、视图和更新逻辑，结合 `iced::run` 启动应用。例如，示例中的计数器通过按钮操作更新状态并渲染界面。  

**主要特性**：  
- 简单易用的 API，开箱即用。  
- 基于 Elm 架构的可维护性设计。  
- 实验性阶段，需关注路线图和问题跟踪。