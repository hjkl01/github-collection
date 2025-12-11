
---
title: segment-geospatial
---

### [opengeos segment-geospatial](https://github.com/opengeos/segment-geospatial)

**项目核心内容总结：**

**功能**：  
该项目提供一个基于Python的工具库，利用Facebook的Segment Anything Model（SAM）对地理空间数据（如遥感影像、地图瓦片）进行语义分割。支持从地图服务下载瓦片并转换为GeoTIFF格式，通过交互式标记、文本提示等方式进行分割，结果可保存为GeoJSON、Shapefile等向量格式。

**使用方法**：  
- 安装方式：通过PyPI（`pip install segment-geospatial`）或conda-forge安装，支持多种选项（如[samgeo]基础功能、[samgeo2]包含HQ-SAM模型等）。  
- 提供Jupyter Notebook示例和教程，支持Google Colab和AWS环境。

**主要特性**：  
- 支持OpenStreetMap、Google Maps等地图服务，可自定义下载区域与分辨率。  
- 交互式分割工具，支持鼠标点击、文本提示等操作。  
- 优化处理大尺寸GeoTIFF文件，兼容HQ-SAM模型提升分割精度。  
- 包含中文、英文教程及视频教学资源。  

**注意事项**：  
- 项目仅用于教育和研究，使用需遵守相关法律法规。  
- 大规模下载地图瓦片前需获得地图服务提供商许可。  
- 建议使用至少8GB显存的GPU加速处理。