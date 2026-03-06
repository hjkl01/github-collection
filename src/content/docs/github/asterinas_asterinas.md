
---
title: asterinas
---

### [asterinas asterinas](https://github.com/asterinas/asterinas)  ![GitHub Repo stars](https://img.shields.io/github/stars/asterinas/asterinas?style=social)

Asterinas 是一个基于 Rust 从零构建的通用操作系统内核，旨在成为生产级、内存安全且高性能的 Linux 替代方案。其核心特点如下：

1.  **架构设计**：采用 Framekernel 架构，结合单内核性能与微内核分离优势；将不安全 Rust 限制在最小框架（OSTD）内，大部分内核代码为安全 Rust。
2.  **兼容性**：兼容 Linux ABI，已实现 230 多个系统调用。
3.  **开发工具**：提供专用工具包 OSDK，简化 Rust 内核的构建、运行和测试。
4.  **支持平台**：支持 x86-64（主要支持）、Intel TDX、RISC-V 64 和 LoongArch 64 等 64 位架构。
5.  **应用场景**：致力于满足数据中心、自动驾驶及具身智能等关键任务部署需求。

项目采用 MPL 2.0 许可证，并提供了实验性发行版 Asterinas NixOS。