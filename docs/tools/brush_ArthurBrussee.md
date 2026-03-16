### [ArthurBrussee brush](https://github.com/ArthurBrussee/brush)  ![GitHub Repo stars](https://img.shields.io/github/stars/ArthurBrussee/brush?style=social)

Brush 是一个基于 Rust 和 Burn 框架的 3D 高斯泼溅（Gaussian splatting）重建引擎，利用 WebGPU 技术实现跨平台支持，涵盖 macOS、Windows、Linux、Android 及浏览器，兼容 AMD、Nvidia 和 Intel 显卡。

主要功能：
1. 训练：支持 COLMAP 和 Nerfstudio 格式，支持多端实时训练与交互，提供训练动态可视化及图像掩膜处理。
2. 查看器：支持加载 .ply 文件，支持 Web 端流式传输和 4D 动画播放。
3. 工具链：提供 CLI 命令行接口，支持开启 UI 调试及集成 Rerun 可视化。

项目生成无依赖二进制文件，无需复杂设置即可运行，渲染与训练性能通常优于 gsplat。