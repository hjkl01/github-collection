
---
title: probe-rs
---

### [probe-rs probe-rs](https://github.com/probe-rs/probe-rs)  ![GitHub Repo stars](https://img.shields.io/github/stars/probe-rs/probe-rs?style=social)

**项目核心内容总结：**

**功能**  
probe-rs 是一个用 Rust 编写的嵌入式调试工具包，支持连接多种调试探针（如 STLink、JLink、DAPLink 等）和处理器架构（ARM、Risc-V、Xtensa），提供芯片内存读写、核心控制（暂停/运行/单步）、断点设置、固件下载（ELF/BIN/IHEX）及调试功能。  

**使用方法**  
- 通过 `cargo-flash` 和 `cargo-embed` 工具实现固件烧录与调试，支持 Rust 和 C/C++ 项目。  
- 集成 VS Code 的 DAP 协议实现嵌入式调试，提供 CLI、GDB 服务器等工具。  
- 示例代码展示如何用 Rust 连接探针、控制芯片核心及读写内存。  

**主要特性**  
- 支持多类调试探针和处理器架构，兼容性广。  
- 提供丰富的调试工具链（CLI、VS Code 插件、GDB 服务器）。  
- 开源且可扩展，支持自定义闪存算法及目标设备配置。  
- 文档完善，包含安装指南、使用示例及故障排查说明。