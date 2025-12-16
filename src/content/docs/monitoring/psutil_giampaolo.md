
---
title: psutil
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/giampaolo/psutil?style=social) ](https://github.com/giampaolo/psutil)
### [giampaolo psutil](https://github.com/giampaolo/psutil)

**核心内容总结：**  
psutil 是一个跨平台的 Python 库，用于监控系统资源（如 CPU、内存、磁盘、网络）和管理进程。其主要功能包括：  
1. **系统监控**：实时获取 CPU 使用率、内存状态、磁盘 I/O、网络连接等信息。  
2. **进程管理**：查询进程详细信息（PID、名称、内存占用、打开文件、网络连接），支持进程终止、挂起、恢复，以及设置优先级和资源限制（如文件描述符）。  
3. **高级功能**：提供内存泄漏检测工具，支持 Windows 服务管理（如获取服务状态、启动类型）。  
4. **跨平台兼容**：支持 Linux、Windows、macOS 等操作系统。  

**使用方法**：  
通过导入 `psutil` 模块，调用相关函数（如 `psutil.cpu_percent()`、`psutil.virtual_memory()`）或遍历进程（`psutil.process_iter()`）获取数据。  

**主要特性**：  
- 丰富的 API 接口，覆盖系统和进程的详细信息。  
- 支持资源控制（如 IO 优先级、RLIMIT 限制）。  
- 提供进程级操作（如终止、修改优先级）。  
- 适用于系统监控、性能分析、自动化运维等场景。