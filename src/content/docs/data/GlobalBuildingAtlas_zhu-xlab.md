
---
title: GlobalBuildingAtlas
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/zhu-xlab/GlobalBuildingAtlas?style=social) ](https://github.com/zhu-xlab/GlobalBuildingAtlas)
### [zhu-xlab GlobalBuildingAtlas](https://github.com/zhu-xlab/GlobalBuildingAtlas)

**核心内容总结：**  
该项目提供全球范围的建筑LoD1数据，包括建筑多边形、高度信息及三维模型。  

**功能与使用方法：**  
1. **数据访问**  
   - 通过WFS接口（`https://tubvsig-so2sat-vm1.srv.mwn.de/geoserver/ows?`）用GIS软件（如QGIS）调用数据；  
   - 通过在线Web Viewer（[链接](https://tubvsig-so2sat-vm1.srv.mwn.de)）浏览数据（可能因高并发导致部分数据加载不全）；  
   - 从[mediaTUM](https://mediatum.ub.tum.de/1782307)下载全量数据。  

2. **开发代码**  
   - 建筑多边形生成（`./im2bf`）、高度估计（`./im2bh`及`./infer_height`）、LoD1模型生成（`./fuse_bf`及`./make_lod1`）；  
   - 可视化代码（`./make_plots`）用于复现论文图表。  

**主要特性：**  
- 全球覆盖，提供建筑多边形、高度及LoD1三维模型；  
- 代码模块化，支持建筑提取、高度估算、模型生成等全流程；  
- 采用MIT许可证（禁止商业使用）。  

**引用要求：**  
使用该数据需引用论文：Zhu et al., *Earth System Science Data*, 2025.