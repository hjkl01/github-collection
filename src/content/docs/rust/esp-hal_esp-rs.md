
---
title: esp-hal
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/esp-rs/esp-hal?style=social) ](https://github.com/esp-rs/esp-hal)
### [esp-rs esp-hal](https://github.com/esp-rs/esp-hal)

**项目核心内容总结：**  
esp-hal 是为 Espressif 设备（如 ESP32、ESP32-C2/C3/C6、ESP32-H2、ESP32-S2/S3 等）提供的裸机（no_std）硬件抽象层（HAL），支持通过 `esp-lp-hal` 编程 ESP32-C6、S2、S3 的低功耗 RISC-V 核心。  

**使用方法：**  
- 参考《The Rust on ESP Book》和项目文档进行开发；  
- 示例代码需使用特定版本标签（如 `esp-hal-v1.0.0`）以确保兼容性，避免使用 `main` 分支的不稳定 API。  

**主要特性：**  
- 支持多款 Espressif 芯片，覆盖主流型号；  
- 提供稳定且可扩展的 HAL 接口，适用于嵌入式开发；  
- 明确支持政策：仅对最新小版本分支（如 `1.1.x`）回溯补丁；  
- 开源许可证为 Apache 2.0 或 MIT，支持社区贡献。