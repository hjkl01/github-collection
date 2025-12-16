
---
title: brush
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/ArthurBrussee/brush?style=social) ](https://github.com/ArthurBrussee/brush)
### [ArthurBrussee brush](https://github.com/ArthurBrussee/brush)

**核心内容总结：**

**项目功能：**  
Brush 是一个基于高斯点扩散（Gaussian Splatting）的 3D 重建引擎，支持训练和实时渲染。可处理 COLMAP 或 Nerfstudio 格式数据，支持遮罩图像（透明度处理、区域忽略）。作为查看器，支持加载 `.ply`、`.compressed.ply` 和 ZIP 动画文件，兼容 Web 端（通过 URL 流式加载）。

**使用方法：**  
- **本地运行**：需安装 Rust 1.88+，通过 `cargo run` 或 `cargo run --release` 启动。  
- **Web 端**：使用 Next.js 启动 demo（`npm run dev`），需 Chrome/Edge 浏览器。  
- **Android**：需配置 Android SDK/NDK，通过 `cargo ndk` 编译并集成到 Android Studio 项目中。  
- **CLI 工具**：支持命令行操作，如 `brush --help`，可结合 `--with-viewer` 启动调试界面。

**主要特性：**  
1. **跨平台兼容**：支持 macOS/Windows/Linux/Android/浏览器，适配 AMD/Nvidia/Intel 显卡。  
2. **实时交互**：训练时可实时预览场景、对比输入视图，支持动态渲染。  
3. **轻量依赖**：生成无依赖的二进制文件，无需 CUDA 等复杂依赖。  
4. **WebGPU 支持**：基于 WebGPU 技术，实现浏览器端渲染。  
5. **扩展功能**：支持 Rerun 可视化工具（通过 `rerun` 可视化训练数据），兼容 4D 动态模型（如 cat-4D、Cap4D）。  
6. **性能优化**：渲染和训练速度优于 gsplat，提供基准测试工具（`cargo bench`）。