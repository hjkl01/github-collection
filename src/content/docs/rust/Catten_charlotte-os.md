
---
title: Catten
---

### [charlotte-os Catten](https://github.com/charlotte-os/Catten)

**项目核心内容总结：**

**项目功能**  
Catten 是 CharlotteOS 的单体式内核，提供安全、灵活的系统架构，支持多种高层运行时环境，具备基于能力的命名空间管理和硬件抽象层。

**主要特性**  
1. **设计理念**：结合 exokernel、Fuchsia 和微内核优势，采用单体结构提升性能，通过最小化系统调用接口兼容多种运行时。  
2. **命名空间安全**：使用 URI 路径和能力控制机制（类似 Plan 9/Fuchsia），实现跨主机资源访问和强制访问控制。  
3. **语言与依赖**：以 Rust 为主，允许少量 C 和汇编；依赖需标准化，禁止非 Rust/C/ASM 依赖。  
4. **硬件兼容**：支持 x86-64（需 UEFI/ACPI）和 RISC-V64（需 SBI/DTSpec），要求硬件文档公开且设备可识别。  

**使用方法**  
- **开发**：需 Rust 环境，遵循架构特定的汇编语法（x86-64 用 Intel 语法）。  
- **部署**：目标平台需满足内存（≥128MB）、存储（≥4GB）、显示（UEFI GOP 或 FDT `simplefb`）等硬件要求。  
- **贡献**：通过 Discord/Matrix 社区参与，提交代码需附公开硬件文档。  

**许可证**：采用 AGPLv3，允许商业授权，贡献者可选择退出商业授权。