
---
title: segment-geospatial
---

### [opengeos segment-geospatial](https://github.com/opengeos/segment-geospatial)  ![GitHub Repo stars](https://img.shields.io/github/stars/opengeos/segment-geospatial?style=social)

SamGeo 是一个 Python 包，旨在简化利用 Segment Anything Model (SAM) 进行地理空间数据分析的过程。其核心功能包括：

1.  **数据获取**：从地图瓦片服务（TMS）下载图块并创建 GeoTIFF 文件。
2.  **影像分割**：使用 SAM、HQ-SAM、Fast SAM 及 SAM 3 等模型对 GeoTIFF 文件和遥感影像进行分割。
3.  **交互与提示**：支持通过文本提示（Text Prompts）或交互式创建前景/背景标记进行分割，并支持从现有矢量数据加载标记。
4.  **结果输出**：将分割结果保存为 GeoPackage、Shapefile、GeoJSON 等常见矢量格式，支持在交互式地图上可视化，并具备时序遥感影像分割能力。
5.  **扩展支持**：提供 QGIS 插件及 ArcGIS 工具箱集成。