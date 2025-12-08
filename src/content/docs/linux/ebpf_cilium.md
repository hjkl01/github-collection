
---
title: ebpf
---

### [cilium ebpf](https://github.com/cilium/ebpf)

**项目功能**：  
ebpf-go 是一个纯 Go 实现的库，用于加载、编译和调试 eBPF 程序，适用于长期运行的进程。支持通过多种包实现 eBPF 程序的编写、附加、调试及与内核交互，包括汇编、C 代码编译、事件读取、特性探测等功能。

**使用方法**：  
- 使用 `bpf2go` 工具将 C 编写的 eBPF 程序编译并嵌入 Go 代码，自动生成加载和操作代码。  
- 通过 `asm` 包直接编写 eBPF 汇编指令。  
- 使用 `link` 包将 eBPF 程序附加到内核钩子，`perf` 和 `ringbuf` 包读取性能事件或环形缓冲区数据。  
- 支持通过 `features` 包探测内核特性，`rlimit` 包管理资源限制，`pin` 包操作 bpffs 上的固定对象。

**主要特性**：  
- 支持 Linux（amd64、arm64）及 Windows（amd64）系统，兼容较新内核版本。  
- 提供多个功能模块，涵盖 eBPF 程序开发全流程。  
- MIT 开源许可证，适合长期运行的高性能场景。