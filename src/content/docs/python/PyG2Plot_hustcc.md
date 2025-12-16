
---
title: PyG2Plot
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/hustcc/PyG2Plot?style=social) ](https://github.com/hustcc/PyG2Plot)
### [hustcc PyG2Plot](https://github.com/hustcc/PyG2Plot)

**核心内容总结：**  
PyG2Plot 是一个 Python 库，作为 AntV/G2Plot 的绑定，用于生成交互式、响应式的统计图表。用户可通过简单代码快速创建图表，灵感来源于 pyecharts。  

**使用方法：**  
- 安装：`pip install pyg2plot`。  
- 生成 HTML 文件：通过 `render("文件名.html")` 输出静态文件，或 `render_html()` 获取 HTML 字符串。  
- 在 Jupyter 中渲染：使用 `render_notebook()` 或 `render_jupyter_lab()` 直接显示图表。  
- 自定义：通过 `JS` API 编写 JavaScript 回调函数，动态调整图表样式（如修改线条颜色）。  

**主要特性：**  
- 支持多种图表类型（如折线图、柱状图等）。  
- 响应式布局，适应不同屏幕尺寸。  
- 与 Jupyter Notebook/Lab 深度集成，支持实时预览。  
- 提供灵活的 JavaScript 回调接口，实现高级自定义功能。