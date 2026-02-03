
---
title: bubbletea
---

### [charmbracelet bubbletea](https://github.com/charmbracelet/bubbletea)  ![GitHub Repo stars](https://img.shields.io/github/stars/charmbracelet/bubbletea?style=social)

**项目名称**：Bubble Tea（气泡茶）

**项目功能**：  
Bubble Tea 是一个基于 Go 语言的终端用户界面（TUI）开发框架，灵感来自 Elm 架构。它适用于构建简单或复杂的终端应用，支持鼠标操作、键盘事件处理、性能优化等功能，适合开发交互式命令行程序。

**使用方法**：  
1. 定义一个模型（model）用于保存应用状态。  
2. 实现三个方法：  
   - `Init()`：初始化模型和初始命令。  
   - `Update(msg Msg) (Model, Cmd)`：处理事件（如按键），更新模型。  
   - `View() string`：根据模型渲染界面。  
3. 使用 `tea.NewProgram(initialModel)` 启动程序。

**主要特性**：  
- 基于 Elm 架构，函数式设计，状态管理清晰。  
- 支持键盘、鼠标操作。  
- 内置帧率渲染器，优化性能。  
- 提供调试工具，如日志记录和 Delve 调试支持。  
- 提供丰富的 UI 组件库（Bubbles）和样式工具（Lip Gloss）等扩展库。

**适用场景**：  
开发终端工具、交互式命令行应用、实时数据展示等。