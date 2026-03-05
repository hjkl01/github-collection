
---
title: probe-rs
---

### [probe-rs probe-rs](https://github.com/probe-rs/probe-rs)  ![GitHub Repo stars](https://img.shields.io/github/stars/probe-rs/probe-rs?style=social)

probe-rs 是一个用 Rust 编写的现代嵌入式调试工具包。它支持连接 DAPLink、STLink、JLink、FTDI、WLink、Blackmagic 及 ESP32 等多种调试探针，并通过 SWD 或 JTAG 协议与 ARM、Risc-V 及 Xtensa 内核通信。项目提供内存读写、核心控制（暂停、运行、单步、断点、跟踪）及基于 CMSIS-Pack 算法的固件下载功能。此外，它还包含 CLI 工具（cargo-flash、cargo-embed）及支持通过 Microsoft DAP 协议的编辑器集成（如 VSCode），用于嵌入式设备的烧录和调试。