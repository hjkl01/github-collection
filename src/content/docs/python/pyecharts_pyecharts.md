
---
title: pyecharts
---

### [pyecharts pyecharts](https://github.com/pyecharts/pyecharts)

**项目核心内容总结：**  
pyecharts 是一个基于 ECharts 的 Python 图表生成库，支持丰富的 2D/3D 图表类型（如折线图、柱状图、饼图、散点图、热力图、地图、3D 柱状图等），可快速实现数据可视化。  

**功能与使用方法：**  
1. **安装**：通过 `pip install pyecharts` 安装。  
2. **使用**：导入模块后，创建图表对象（如 `Bar()`、`Line()`），添加数据与配置，最后生成 HTML 文件（如 `render()` 方法）。  
3. **特性**：  
   - 支持多种数据格式（如列表、DataFrame）。  
   - 提供主题定制、交互功能（缩放、悬停提示）。  
   - 兼容 Jupyter Notebook 直接显示图表。  

**主要优势：**  
- 中英文文档齐全，提供大量示例（[示例链接](https://gallery.pyecharts.org)）。  
- 支持动态图表（如时间轴 `Timeline`）与多图表组合（如 `Grid` 布局）。  
- 代码简洁，可通过 `make` 命令运行单元测试确保质量。