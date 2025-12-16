
---
title: vello
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/linebender/vello?style=social) ](https://github.com/linebender/vello)
### [linebender vello](https://github.com/linebender/vello)

**项目核心内容总结：**  
Vello 是一个基于 GPU 计算的高性能 2D 渲染器，使用 Rust 编写，依赖 [wgpu](https://wgpu.rs/) 实现跨平台 GPU 访问。支持渲染形状、图像、渐变、文本等图形元素，采用类似 PostScript 的 API 设计。其核心特性是通过 GPU 并行计算和前缀和算法优化渲染性能，减少临时缓冲区使用，要求设备支持计算着色器。  

**使用方法：**  
- 快速入门：通过 `cargo run -p with_winit` 启动示例项目。  
- 开发流程：初始化 wgpu 上下文，创建场景对象，调用渲染接口将图形数据输出到纹理。  
- 平台支持：提供 Web（需注意兼容性）、Android（通过 `cargo apk` 部署）等跨平台方案。  

**主要特性：**  
- 基于 GPU 的并行计算，提升复杂场景渲染效率；  
- 依赖 wgpu 实现跨平台（Web/Android 等）兼容；  
- 集成扩展库（如 `vello_svg`、`vello_shaders`）支持更多功能；  
- 开源社区活跃，讨论渠道为 [Linebender Zulip 的 #vello 频道](https://xi.zulipchat.com/#narrow/channel/197075-vello)。  

**注意事项：**  
- 项目处于 alpha 阶段，部分功能（如模糊效果、GPU 内存优化）尚未完善；  
- 需 Rust 1.86 及以上版本，部分依赖可能要求更高版本；  
- 许可证为 Apache 2.0 或 MIT，部分着色器代码采用 Unlicense。