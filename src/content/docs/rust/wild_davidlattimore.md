
---
title: wild
---

### [davidlattimore wild](https://github.com/davidlattimore/wild)

Wild 是一个旨在提升迭代开发效率的快速链接器，未来计划支持增量链接（当前尚未实现）。其核心功能包括：  

- **支持平台**：目前支持 x86-64、ARM64 和 RISC-V（Linux 系统），可生成静态库、动态库及 PIE 二进制文件，兼容 Rust proc-macro 和多数主流 crate。  
- **性能优势**：在非增量链接场景下已表现出色，基准测试显示其速度接近或优于现有链接器（如 mold、lld）。  
- **使用方法**：  
  - 安装方式包括 GitHub 发布包、cargo-binstall、crates.io 安装或从源码构建。  
  - 配置 Rust 项目时，通过 `cargo` 配置文件设置 `linker = "clang"` 并指定 `--ld-path=wild` 或 `-fuse-ld=wild` 参数。  
  - C/C++ 项目需通过环境变量（如 `LDFLAGS`）或 GCC 的 `-B` 选项指定 Wild 路径。  
- **验证方式**：使用 `readelf --string-dump .comment` 或 `strings` 命令检查生成的二进制文件是否包含 "Linker: Wild" 信息。  
- **局限性**：暂不支持 macOS、Windows、LTO 及复杂链接脚本，增量链接和更多架构支持正在开发中。  

项目开源，采用 Apache 2.0 或 MIT 双许可证，社区可通过 Zulip 参与讨论，亦可赞助开发。