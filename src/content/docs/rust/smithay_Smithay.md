
---
title: smithay
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/Smithay/smithay?style=social) ](https://github.com/Smithay/smithay)
### [Smithay smithay](https://github.com/Smithay/smithay)

Smithay 是一个用于构建 Wayland 合成器的 Rust 库，提供通用功能模块（如核心协议支持、输入处理、窗口管理等），但不强制要求使用所有功能。其核心特性包括：  
- **功能**：支持 Wayland 核心协议、官方扩展协议及部分外部协议（如 wlroots、KDE 相关协议），提供合成器开发所需的基础组件。  
- **使用方法**：通过示例合成器 [Anvil](https://github.com/Smithay/smithay/blob/master/anvil/README.md) 学习实现，可参考其他基于 Smithay 的合成器（如 Cosmic、Strata 等）进行开发。  
- **特性**：文档完善（[docs.rs](https://docs.rs/smithay)）、模块化设计、安全性（基于 Rust 语言特性）、高层抽象（减少底层细节处理）。  

**系统依赖**：需安装 `libwayland`、`libxkbcommon`、`libudev` 等库。  
**交流**：可通过 Matrix 房间 `#smithay:matrix.org` 参与讨论。