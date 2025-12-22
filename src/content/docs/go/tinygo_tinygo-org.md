
---
title: tinygo
---

### [tinygo-org tinygo](https://github.com/tinygo-org/tinygo)  ![GitHub Repo stars](https://img.shields.io/github/stars/tinygo-org/tinygo?style=social)

TinyGo 是一个针对微控制器、WebAssembly（wasm/wasi）及命令行工具的 Go 语言编译器。项目基于 Go 工具链和 LLVM 技术，提供更小的二进制体积和对嵌入式设备的优化支持。  

**核心功能**：  
- **嵌入式开发**：支持 94 种以上微控制器开发板，可直接编译运行如 Arduino、Adafruit 等硬件的 LED 控制等程序，通过 `tinygo flash -target` 命令实现设备烧录。  
- **WebAssembly**：支持编译为 WASM/WASI 模块，适用于浏览器、Fastly Compute、Fermyon Spin 等环境，提供 `add` 函数示例及 `tinygo build -target=wasip1` 编译命令。  
- **操作系统支持**：兼容 Linux、macOS、Windows 平台。  

**主要特性**：  
- 极小的二进制体积，按需编译；  
- 支持主流微控制器及 WebAssembly 运行时；  
- 良好的 CGo 兼容性，无额外开销；  
- 支持标准库大部分功能，兼容多数 Go 代码。  

**使用方法**：  
通过 `tinygo build` 或 `tinygo flash` 命令指定目标平台（如 `-target=arduino` 或 `-target=wasip1`）进行编译，具体文档指引见官网。  

**非目标**：  
不追求极致的高并发性能，不兼容所有 Go 代码，不保证与标准 Go 编译器（gc）的性能一致。  

项目旨在弥补 Go 语言在嵌入式领域的不足，通过 LLVM 优化实现更高效的资源利用，适用于资源受限的微控制器及 WebAssembly 场景。许可证为 BSD 3-clause，部分代码采用 Apache 2.0 或 PJRC 许可证。