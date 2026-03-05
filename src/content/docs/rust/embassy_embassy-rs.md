
---
title: embassy
---

### [embassy-rs embassy](https://github.com/embassy-rs/embassy)  ![GitHub Repo stars](https://img.shields.io/github/stars/embassy-rs/embassy?style=social)

Embassy 是基于 Rust 语言的下一代嵌入式应用框架，利用 async/await 机制实现安全、高效且低功耗的开发，无需传统 RTOS、运行时或操作系统。

核心功能包括：
1. **硬件抽象层 (HAL)**：支持 STM32、Nordic nRF、Raspberry Pi RP2040/23xx、ESP32 等多种微控制器系列，提供安全的硬件 API，避免直接操作寄存器。
2. **异步任务调度**：任务在编译期转换为状态机，支持协作式多任务、单栈运行及零动态内存分配；具备实时优先级任务调度与自动低功耗休眠能力。
3. **通信协议栈**：内置网络 (TCP/UDP/ICMP/DHCP)、蓝牙 (BLE)、LoRa/LoRaWAN、USB 设备栈，以及支持安全升级的 Bootloader/DFU 模块。
4. **系统工具**：提供全局无溢出时间管理、丰富的跨芯片示例代码，最低支持 Rust 1.75+ 稳定版本。