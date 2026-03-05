
---
title: implot
---

### [epezent implot](https://github.com/epezent/implot)  ![GitHub Repo stars](https://img.shields.io/github/stars/epezent/implot?style=social)

ImPlot 是基于 Dear ImGui 的即时模式 GPU 加速绘图库，专为实时可视化程序数据和创建交互式图表设计，集成简便且仅依赖 ImGui。

核心功能：
1. 多图表类型：支持折线、散点、柱状、热力图、饼图、直方图、图像等，可混合绘制。
2. 灵活轴配置：支持线性/对数缩放、时间格式化、子图、多坐标轴及轴范围锁定。
3. 交互控制：提供缩放、平移、框选、自动适配数据及查询范围。
4. 样式定制：支持自定义标记、线宽、颜色映射、图例、标题及标签，可继承 ImGui 主题。
5. 广泛数据支持：兼容多种数值类型，支持自定义数据获取器与数据步进。

注意事项：适用于实时交互场景，非出版级绘图或导出工具；高密度绘图时需确保 ImGui 使用 32 位索引或支持顶点偏移。