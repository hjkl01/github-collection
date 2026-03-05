
---
title: brush
---

### [ArthurBrussee brush](https://github.com/ArthurBrussee/brush)  ![GitHub Repo stars](https://img.shields.io/github/stars/ArthurBrussee/brush?style=social)

Brush 是一个基于高斯泼溅（Gaussian Splatting）技术的跨平台 3D 重建引擎，支持 macOS、Windows、Linux、Android 及浏览器（WebGPU）。

其核心功能包括：
1. **训练**：支持 COLMAP 和 Nerfstudio 格式数据集，可在本地、移动端和浏览器中实时交互训练，支持图像透明度及区域掩膜。
2. **查看器**：支持加载 .ply 及压缩文件，具备网页流式加载能力，并可播放动画或 4D 点云数据。
3. **命令行**：提供 CLI 接口，支持开启查看器进行调试。
4. **可视化**：集成 Rerun 工具，便于训练过程中的数据可视化。
5. **性能**：渲染与训练速度通常优于 gsplat。

项目基于 Rust 开发，生成无依赖的二进制文件，无需复杂环境配置即可运行。