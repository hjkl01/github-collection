
---
title: patina
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/OpenDevicePartnership/patina?style=social) ](https://github.com/OpenDevicePartnership/patina)
### [OpenDevicePartnership patina](https://github.com/OpenDevicePartnership/patina)

**核心内容总结：**  
Patina 是一个用 Rust 实现的 UEFI 固件项目，旨在通过纯 Rust 替代传统 C 语言编写的 UEFI 组件，提升固件安全性与稳定性。  

**主要功能与特性：**  
- 支持 aarch64 和 x64 平台编译，提供 DXE 核心及部分 UEFI 驱动组件。  
- 提供详细文档（包括 API 参考和开发指南）及测试框架，支持单元测试、覆盖率分析和基准测试。  
- 通过 GitHub Actions 实现持续集成，支持版本发布流程（如 PR 更新版本号后自动发布至 crates.io）。  

**使用方法：**  
1. 安装 Rust 工具链，配置 `x86_64-unknown-uefi` 目标。  
2. 使用 `cargo make` 命令进行构建（如 `cargo make build`）、测试（`cargo make test`）和覆盖率分析（`cargo make coverage`）。  
3. 参考文档中的 API 说明进行固件开发与集成。  

**项目目标：**  
逐步将 UEFI 组件从 C 迁移到 Rust，扩展 MM 核心支持，推动与 Rust 社区及固件生态的协作。