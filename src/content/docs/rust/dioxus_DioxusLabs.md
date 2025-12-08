
---
title: dioxus
---

### [DioxusLabs dioxus](https://github.com/DioxusLabs/dioxus)

**核心内容总结：**  
Dioxus 是一个用于构建跨平台应用的 Rust 框架，支持 Web、桌面（Windows/macOS/Linux）、移动端（iOS/Android）及服务端渲染。主要功能包括零配置开发、热重载、模块化架构及社区驱动的生态。  

**使用方法：**  
1. 安装 CLI 工具（通过 `cargo binstall` 或 Git 安装）；  
2. 运行示例项目（`cargo run --example <名称>`）或使用 CLI 启动 Web 平台项目（`dx serve --example <名称> --platform web`）。  

**主要特性：**  
- 支持 WebAssembly 渲染、服务端 SSR 及客户端水合；  
- 提供桌面端（Webview/WGPU）和移动端（Webview/Skia）渲染方案；  
- 内置热重载、开发服务器及快速迭代工具；  
- 模块化设计，允许自定义渲染器或使用社区方案（如 Freya）；  
- 活跃社区支持，提供企业级工具及开源协作生态。  

**许可证：** 采用 MIT 或 Apache-2.0 双许可协议。