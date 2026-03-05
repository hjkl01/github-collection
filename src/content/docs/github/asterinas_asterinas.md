
---
title: asterinas
---

### [asterinas asterinas](https://github.com/asterinas/asterinas)  ![GitHub Repo stars](https://img.shields.io/github/stars/asterinas/asterinas?style=social)

Asterinas 是一个基于 Rust 编写的现代化操作系统内核，旨在成为生产级、内存安全且高性能的 Linux 替代品。项目采用“帧内核”（framekernel）架构，将不安全 Rust 代码限制在小型框架 OSTD 中，其余部分使用安全 Rust 编写。

主要功能与特性包括：
1. **Linux 兼容**：兼容 Linux ABI，支持 230 多个系统调用。
2. **多架构支持**：支持 x86-64（Tier 1）、x86-64 Intel TDX、RISC-V 64 及 LoongArch 64 架构。
3. **架构与性能**：结合单内核性能与微内核分离优势，通过 CortenMM 等创新方案优化内存管理与 CPU 可扩展性。
4. **开发工具链**：提供专用工具包 OSDK，简化 Rust 内核的构建、运行与测试流程。
5. **系统发行**：提供实验性发行版 Asterinas NixOS，支持运行真实应用与包管理。

项目致力于消除历史遗留 C 代码的安全漏洞，目标是在数据中心、自动驾驶及 AI 等领域实现关键任务的生产级部署。