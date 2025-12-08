
---
title: wgpu
---

### [gfx-rs wgpu](https://github.com/gfx-rs/wgpu)

**核心内容总结：**

`wgpu` 是一个跨平台、安全的纯 Rust 图形 API，支持 Vulkan、Metal、D3D12、OpenGL 等原生图形接口，以及 WebGPU 和 WebGL2 在 WebAssembly 上的运行。它是 Firefox、Servo 和 Deno 的 WebGPU 集成核心。

**使用方法：**  
- 通过在线示例（[https://wgpu.rs/examples/](https://wgpu.rs/examples/)）学习和运行代码，使用 `cargo run --bin wgpu-examples <示例名>` 执行示例。  
- 新手可参考 [Learn Wgpu](https://sotrh.github.io/learn-wgpu/) 或 [WebGPU Fundamentals](https://webgpufundamentals.org/) 教程。  

**主要特性：**  
- 基于 WebGPU 标准，但作为原生 Rust 库实现。  
- 支持多平台（Windows、Linux、macOS、Web 等），可通过环境变量（如 `WGPU_BACKEND`）灵活配置后端和行为。  
- 提供社区支持（Matrix 和 Discord 讨论组），并兼容 C 等其他语言（通过 [wgpu-native](https://github.com/gfx-rs/wgpu-native)）。  
- 最小 Rust 版本（MSRV）为 1.88，部分组件支持 1.82。  
- 提供详细的测试文档和 WebGPU/WGSL 规范跟踪机制。