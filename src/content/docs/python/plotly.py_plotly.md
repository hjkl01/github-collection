
---
title: plotly.py
---

### [plotly plotly.py](https://github.com/plotly/plotly.py)

**核心内容总结：**  
`plotly.py` 是一个基于 Python 的交互式可视化库，依托 `plotly.js` 提供 30 多种图表类型（如科学图表、3D 图形、地图等），支持在 Jupyter 笔记本、Dash 应用中展示或导出为静态图片。  

**使用方法：**  
通过 `pip install plotly` 安装，使用 `plotly.express` 快速生成图表，如示例代码 `px.bar()` 创建柱状图并调用 `fig.show()` 显示。  

**主要特性：**  
- MIT 开源许可证，免费商用；  
- 支持静态图像导出（需安装 `kaleido` 或 `orca`）；  
- 提供扩展地理数据支持（需额外安装 `plotly-geo`）；  
- 兼容 Jupyter、Dash 等多种开发环境。