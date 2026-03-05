
---
title: cross
---

### [cross-rs cross](https://github.com/cross-rs/cross)  ![GitHub Repo stars](https://img.shields.io/github/stars/cross-rs/cross?style=social)

cross 是一个用于 Rust 项目的零配置跨编译和跨测试工具。它利用 Docker 或 Podman 提供隔离的交叉工具链环境，无需修改主机系统即可针对多种目标架构（如 Linux、Android 等）构建和测试 Rust 项目。cross 的命令行与 Cargo 完全一致，支持 Rust 稳定版、Beta 版及 nightly 通道，测试功能依赖 QEMU 模拟，并允许通过配置文件或环境变量自定义配置。