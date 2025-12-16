
---
title: DearPyGui
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/hoffstadt/DearPyGui?style=social) ](https://github.com/hoffstadt/DearPyGui)
### [hoffstadt DearPyGui](https://github.com/hoffstadt/DearPyGui)

**核心内容总结：**  
Dear PyGui 是一个基于 C/C++ 的现代 Python GUI 框架，支持跨平台（Windows、macOS、Linux、Raspberry Pi 4），具备高性能 GPU 渲染和异步操作能力。主要特性包括：  
- **可视化功能**：支持图表（百万数据点 60fps 渲染）、节点编辑器、画布绘图（可开发 2D 游戏）。  
- **开发效率**：提供内置演示工具、主题调试、实时性能监控等功能。  
- **易用性**：通过简单 Python 代码即可创建窗口、控件（如按钮、输入框、滑块）并绑定回调函数。  

**使用方法**：  
1. 安装：`pip install dearpygui`。  
2. 示例代码：创建窗口并添加控件，通过回调函数实现交互逻辑。  
3. 运行内置演示：`python -m dearpygui.demo` 查看所有功能示例。  

**技术特点**：  
基于 [Dear ImGui](https://github.com/ocornut/imgui) 及其扩展 [ImPlot](https://github.com/epezent/implot)、[imnodes](https://github.com/Nelarius/imnodes)，采用即时模式（Immediate Mode）和 GPU 加速，适合开发动态可视化界面和高性能应用。