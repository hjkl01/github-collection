
---
title: bubbles
---

### [charmbracelet bubbles](https://github.com/charmbracelet/bubbles)  ![GitHub Repo stars](https://img.shields.io/github/stars/charmbracelet/bubbles?style=social)

**项目核心内容总结：**  

Bubbles 是一个为 [Bubble Tea](https://github.com/charmbracelet/bubbletea) 框架提供终端 UI 组件的 Go 语言库，包含以下功能组件：  

- **Spinner**：加载状态指示器，支持自定义动画帧。  
- **Text Input/TextArea**：支持 Unicode、粘贴、滚动的文本输入框，适用于单行或多行输入。  
- **Table**：可滚动的表格组件，支持列行数据展示与自定义样式。  
- **Progress**：可动画化的进度条，支持实心/渐变填充及百分比显示。  
- **Paginator**：分页逻辑处理组件，支持“点状”分页或数字页码显示。  
- **Viewport**：高性能垂直滚动视口，支持键盘和鼠标滚轮操作。  
- **List**：集成分页、模糊搜索、帮助提示等功能的列表浏览组件。  
- **File Picker**：文件系统选择器，支持目录导航与文件类型过滤。  
- **Timer/Stopwatch**：可自定义频率的倒计时/计时器。  
- **Help**：自动生成的快捷键帮助视图，支持单行/多行模式切换。  
- **Key**：用于管理键盘绑定的非可视化组件，支持快捷键重映射。  

**使用方法**：  
通过 Go 模块引入库（如 `github.com/charmbracelet/bubbles`），参考各组件的示例代码（如 `bubbletea/examples/` 目录）集成到项目中。  

**主要特性**：  
- 提供丰富的终端交互组件，适用于构建复杂 CLI 应用。  
- 支持高度自定义（如样式、动画、布局）。  
- 与 Bubble Tea 生态深度集成，兼容 Harmonica（动画库）和 Reflow（文本排版库）。  
- 示例代码覆盖基础到高级用法，便于快速上手。  

**适用场景**：  
适合需要构建交互式终端应用的开发者，如命令行工具、数据查看器、文件管理器等。