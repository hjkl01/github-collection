
---
title: wild
---

### [davidlattimore wild](https://github.com/davidlattimore/wild)  ![GitHub Repo stars](https://img.shields.io/github/stars/davidlattimore/wild?style=social)

Wild 是一个用 Rust 编写的高性能链接器，旨在加速迭代开发，最终目标是实现增量链接。虽然目前尚未支持增量链接，但其非增量模式下的速度已非常快。它支持 Linux 平台的 x86-64、ARM64、RISC-V 及 LoongArch64 架构，兼容 Rust 和 C/C++ 构建。当前支持静态与动态链接、共享库、调试信息及基础链接器脚本，暂不支持 Windows 和 Mac 系统、增量链接及复杂脚本。