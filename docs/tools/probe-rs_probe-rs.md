### [probe-rs probe-rs](https://github.com/probe-rs/probe-rs)  ![GitHub Repo stars](https://img.shields.io/github/stars/probe-rs/probe-rs?style=social)

probe-rs 是一个用 Rust 编写的现代嵌入式调试工具包，旨在提供与各类嵌入式 MCUs 及调试探头的交互接口，并暴露底层调试功能供其他软件使用。

主要功能如下：
*   **探头支持**：兼容 DAPLink、STLink、JLink、FTDI、ESP32 USB JTAG、WLink 及 Blackmagic 等调试器。
*   **核心架构**：支持 ARM、Risc-V 和 Xtensa 内核，通过 SWD 或 JTAG 协议通信。
*   **调试操作**：支持任意内存的读写、核心控制（暂停、运行、单步、断点、追踪）。
*   **固件烧录**：支持使用标准 CMSIS-Pack 算法下载 ELF、BIN 和 IHEX 二进制文件。
*   **工具生态**：提供 CLI 工具（如 `cargo-flash`、`cargo-embed`）、GDB 服务器以及基于 Microsoft DAP 协议的 VS Code 等编辑器集成。

项目既可作为 Rust 库集成使用，也包含可直接用于 flashing 和调试的独立命令行工具。