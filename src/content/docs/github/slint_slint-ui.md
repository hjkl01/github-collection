
---
title: slint
---

### [slint-ui slint](https://github.com/slint-ui/slint)

Slint 是一个开源的声明式 GUI 工具包，支持跨平台开发（嵌入式系统、桌面、移动设备和 Web），用户可通过 `.slint` 文件用类似 XML 的标记语言定义 UI，再通过 Rust、C++、JavaScript 或 Python 实现业务逻辑。  

**核心功能**：  
- **跨平台**：支持多种操作系统和硬件架构，UI 设计可适配不同设备。  
- **轻量化**：占用资源少，提供流畅的用户交互体验。  
- **原生渲染**：生成的 UI 界面符合各平台设计规范，支持 OpenGL ES、Skia 或 CPU 渲染。  
- **工具链**：提供 Live Preview、Figma 插件、VSCode 扩展、在线编辑器（SlintPad）等开发辅助工具。  
- **稳定 API**：1.x 版本接口长期兼容，避免代码迁移问题。  

**使用方法**：  
1. 用 `.slint` 文件定义 UI（如示例中的“Hello World”代码）。  
2. 通过对应语言的 API（如 Rust、C++ 等）连接业务逻辑。  
3. 使用编译器生成目标语言代码，或通过解释器运行。  

**特性**：  
- 支持多语言绑定（Rust、C++、JavaScript、Python）。  
- 提供嵌入式设备、桌面和 WebAssembly 的应用案例。  
- 提供三种许可证选项（开源 GPLv3、商业免费 Royalty-free、付费 Software 许可）。  

项目通过 GitHub 管理，提供文档、示例和社区支持。