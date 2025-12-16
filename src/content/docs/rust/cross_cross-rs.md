
---
title: cross
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/cross-rs/cross?style=social) ](https://github.com/cross-rs/cross)
### [cross-rs cross](https://github.com/cross-rs/cross)

**项目核心内容总结：**

**1. 项目功能**  
cross-rs 是一个基于 Docker 的跨平台编译工具，支持在 Linux 环境下为多种目标平台（如 Android、FreeBSD、Windows、WebAssembly 等）编译 Rust 项目。提供预置的工具链镜像，包含 GCC、Clang、MSVC 等编译器及对应库。

**2. 使用方法**  
- 安装 Docker 或 Podman 容器引擎  
- 通过 `cargo install cross` 安装工具  
- 使用 `cross compile`、`cross run` 等命令进行编译和运行，指定目标平台（如 `--target x86_64-unknown-linux-gnu`）  

**3. 主要特性**  
- 支持 50+ 目标平台，涵盖主流操作系统和嵌入式设备  
- 提供调试功能（QEMU_STRACE 跟踪系统调用）  
- 支持自定义 Dockerfile 扩展目标平台  
- 兼容 Rust 1.77.2 及以上版本（部分目标需 nightly 工具链）  
- 开源双许可（Apache 2.0/MIT）  

**4. 注意事项**  
- 部分平台（如 CentOS）需手动修改 `Cross.toml` 配置镜像  
- Android 平台仅支持无依赖的原生测试  
- Thumb 汇编目标需使用 newlib 库  
- WebAssembly 目标使用 Emscripten 和 Clang 编译器