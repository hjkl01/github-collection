
---
title: asterinas
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/asterinas/asterinas?style=social) ](https://github.com/asterinas/asterinas)
### [asterinas asterinas](https://github.com/asterinas/asterinas)

**项目核心内容总结**  
Asterinas 是一个用 Rust 编写的操作系统内核，兼容 Linux ABI，提供安全、快速且通用的解决方案，可作为 Linux 的替代品。  

**主要特性**  
- 通过 Rust 语言和 **framekernel 架构** 限制不安全代码使用，仅保留最小可信计算基（TCB），提升内存安全性和系统可靠性。  
- 提供 **OSDK 工具包**，优化开发者工作流，支持开源或专有发布（基于 MPL 2.0 许可证）。  
- 支持 x86-64、RISC-V、LoongArch 等架构，并兼容 Intel TDX 安全虚拟化技术。  

**使用方法**  
1. 克隆源码：`git clone https://github.com/asterinas/asterinas`。  
2. 使用 Docker 容器作为开发环境：  
   ```bash  
   docker run -it --privileged --network=host -v /dev:/dev -v $(pwd)/asterinas:/root/asterinas asterinas/asterinas:0.16.1-20251130  
   ```  
3. 容器内执行构建与运行：  
   ```bash  
   make build && make run  
   ```  
   成功后，Asterinas 将在虚拟机中运行。