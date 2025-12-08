
---
title: embassy
---

### [embassy-rs embassy](https://github.com/embassy-rs/embassy)

Embassy 是一个基于 Rust 的嵌入式应用开发框架，通过异步编程特性实现安全、高效、低功耗的嵌入式开发。其核心功能包括：  
1. **硬件支持**：提供 STM32、nRF、RP2040、ESP32 等主流芯片的硬件抽象层（HAL），无需直接操作寄存器。  
2. **异步编程**：利用 Rust 的 async/await 实现无动态内存分配的协作式多任务，替代传统 RTOS，提升性能和代码简洁性。  
3. **关键特性**：  
   - 全局时间管理（无硬件定时器依赖）；  
   - 实时任务优先级调度；  
   - 低功耗设计（空闲时自动休眠）；  
   - 网络协议栈（Ethernet、TCP/UDP 等）；  
   - 蓝牙、LoRa、USB、DFU 等外设支持。  
4. **使用方法**：  
   - 安装 `probe-rs` 工具；  
   - 配置 Cargo.toml 和 `.cargo/config.toml` 指定目标芯片；  
   - 运行示例（如 `cargo run --release --bin blinky`）。  
5. **开发环境**：支持 Rust Analyzer，需在 VSCode 等编辑器中配置 `rust-analyzer.linkedProjects`。  
6. **兼容性**：需 Rust 1.75 及以上版本，采用 Apache 2.0 或 MIT 双许可证。