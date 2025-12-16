
---
title: ebpf
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/cilium/ebpf?style=social) ](https://github.com/cilium/ebpf)
### [cilium ebpf](https://github.com/cilium/ebpf)

**项目核心内容总结：**  
ebpf-go 是一个纯 Go 编写的库，用于加载、编译和调试 eBPF 程序，适用于长期运行的进程。其主要功能包括：  
- 提供 eBPF 程序的加载、编译和调试工具；  
- 支持通过 Go 代码直接编写 eBPF 汇编指令（asm 包）；  
- 提供 `bpf2go` 工具，将 C 语言编写的 eBPF 程序编译为 Go 代码，并自动生成加载和操作 eBPF 对象的代码；  
- 支持将 eBPF 程序挂载到内核钩子（link 包）、读取 `PERF_EVENT_ARRAY`（perf 包）、处理 `BPF_MAP_TYPE_RINGBUF`（ringbuf 包）等；  
- 包含特性探测（features 包）、资源限制管理（rlimit 包）、BTF 数据读取（btf 包）及 bpffs 对象管理（pin 包）等功能。  

**使用方法：**  
- 参考 [Getting Started] 指南；  
- 社区支持通过 GitHub Discussions 或 Slack 的 `#ebpf-go` 频道；  
- 避免在问题跟踪器中提交非明确 bug 的问题。  

**主要特性：**  
- 支持 Linux（amd64、arm64）和 Windows（amd64）系统；  
- 需 Go 语言支持版本；  
- 采用 MIT 许可证；  
- 提供对 eBPF 程序的嵌入式编译、调试及高级功能（如 BTF、资源限制调整等）。