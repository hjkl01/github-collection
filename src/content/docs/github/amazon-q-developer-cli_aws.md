
---
title: amazon-q-developer-cli
---

### [aws amazon-q-developer-cli](https://github.com/aws/amazon-q-developer-cli)

**核心内容总结：**  
Amazon Q CLI 是一个用于与 Amazon Q Developer 交互的命令行工具，支持跨平台安装（macOS 和 Linux）。  

**功能与使用方法：**  
- **安装方式**：  
  - macOS 可通过 DMG 文件或 HomeBrew 安装（`brew install --cask amazon-q`）。  
  - Linux 支持 Ubuntu/Debian、AppImage 及其他发行版安装。  
- **开发贡献**：  
  - 需 macOS、Xcode 13+ 和 HomeBrew。  
  - 克隆代码后，通过 Rustup 安装 Rust 工具链（含 nightly 版本），并使用 Cargo 编译运行（`cargo run --bin chat_cli`）。  
  - 支持测试（`cargo test`）、代码检查（`cargo clippy`）、格式化（`cargo +nightly fmt`）及子命令执行（如 `cargo run --bin chat_cli -- login`）。  

**主要特性：**  
- 项目结构模块化，包含 CLI 工具（`chat_cli`）、脚本（`scripts/`）、Rust 模块（`crates/`）及文档（`docs/`）。  
- 遵循 MIT 和 Apache 2.0 双许可证，提供安全文档（`SECURITY.md`）。  

**其他信息：**  
- 项目使用 Rust 编写，支持跨平台开发与本地调试。