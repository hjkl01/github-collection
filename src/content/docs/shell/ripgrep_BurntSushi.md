
---
title: ripgrep
---

### [BurntSushi ripgrep](https://github.com/BurntSushi/ripgrep)

**项目核心内容总结：**

**功能：**  
ripgrep 是一个基于 Rust 的高性能文本搜索工具，支持递归搜索、正则表达式、多编码格式（如 UTF-8/UTF-16）及文件类型过滤，适用于代码、日志等文本处理场景。

**使用方法：**  
1. **安装方式**  
   - 通过包管理器（如 Debian/Ubuntu 的 `apt`、Homebrew、Nix、Guix 等）直接安装。  
   - 使用 `cargo install ripgrep` 或 `cargo binstall ripgrep` 从源码安装。  
   - 手动下载 `.deb` 或静态编译二进制文件。  

2. **构建方式**  
   - 需安装 Rust 1.85.0 及以上版本，执行 `cargo build --release` 编译。  
   - 支持静态链接（如 MUSL 目标）及 PCRE2 库扩展（需启用 `pcre2` 特性）。  

**主要特性：**  
- **高性能**：利用 Rust 的内存安全和 SIMD 优化，搜索速度显著优于传统工具。  
- **智能过滤**：自动跳过二进制文件，支持 `.gitignore` 规则过滤无关文件。  
- **灵活输出**：支持 `--json` 格式输出，兼容语法高亮工具（如 delta）。  
- **跨平台支持**：覆盖 Linux、Windows、macOS、FreeBSD、OpenBSD 等系统。  
- **扩展性**：可通过 `pcre2` 特性集成 PCRE2 库，增强正则表达式功能。  

**其他：**  
- 提供完整的测试套件（`cargo test --all`）。  
- 支持多语言文档（如中文、西班牙语）。  
- 安全漏洞可通过指定邮箱联系开发者报告。