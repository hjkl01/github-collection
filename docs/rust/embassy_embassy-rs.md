### [embassy-rs embassy](https://github.com/embassy-rs/embassy)  ![GitHub Repo stars](https://img.shields.io/github/stars/embassy-rs/embassy?style=social)

Embassy 是一个基于 Rust 语言和异步编程机制的下一代嵌入式应用程序框架，旨在帮助用户快速编写安全、高效且节能的嵌入式代码。

主要功能包括：
1. **异步运行时**：任务在编译期转换为状态机，无需动态内存分配和操作系统支持，比传统 RTOS 更轻量、快速。
2. **硬件抽象层（HAL）**：支持 STM32、nRF、RP2040、ESP32 等多种主流微控制器芯片，简化硬件操作。
3. **内置核心库**：
   - **时间管理**：提供全局可用且防溢出的计时器。
   - **电源管理**：支持空闲自动睡眠和中断唤醒，实现低功耗。
   - **通信协议**：涵盖网络（TCP/IP）、蓝牙（BLE）、LoRa 及 USB 设备栈。
   - **实时性**：支持多优先级任务协作执行。
   - **系统升级**：提供安全的固件更新（DFU）和启动器功能。
4. **安全性**：无需运行时、垃圾回收器或 OS，利用 Rust 特性保障编译期内存与线程安全。