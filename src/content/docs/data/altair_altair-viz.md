
---
title: altair
---

### [altair-viz altair](https://github.com/altair-viz/altair)

**Vega-Altair** 是一个基于 Python 的声明式统计可视化库，依托 [Vega-Lite](https://vega.github.io/vega-lite/) 规范，提供简洁友好的 API，用于快速生成交互式数据可视化图表。  

**核心功能**：  
- 通过声明式语法定义图表（如散点图、联动直方图等），支持数据筛选、联动交互等复杂操作。  
- 自动适配 JupyterLab、VS Code、GitHub 等环境，支持导出为 PNG/SVG/HTML 等格式，或序列化为 JSON。  

**使用方法**：  
1. 安装：`pip install altair` 或 `conda install -c conda-forge altair`。  
2. 示例代码：  
   ```python  
   import altair as alt  
   from altair.datasets import data  
   alt.Chart(data.cars()).mark_point().encode(x='Horsepower', y='Miles_per_Gallon', color='Origin')  
   ```  

**主要特性**：  
- 声明式 API 设计，代码简洁且符合 Vega-Lite 规范。  
- 内置类型检查，确保可视化逻辑正确性。  
- 支持交互操作（如通过选择区域联动过滤数据）。  
- 兼容多种显示环境及导出格式，适合学术研究与数据探索。  

**获取帮助**：  
- 技术问题可咨询 [StackOverflow](https://stackoverflow.com/questions/tagged/altair)（标签 `altair`）。  
- Bug 报告或功能请求请提交 [GitHub Issues](https://github.com/vega/altair/issues)。  

**引用说明**：  
如用于学术研究，需引用 [JOSS 论文](https://joss.theoj.org/papers/10.21105/joss.01057) 及 [Vega-Lite 原文](https://dl.acm.org/doi/10.1109/TVCG.2016.2599030)。