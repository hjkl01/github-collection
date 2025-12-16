
---
title: fresh
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/sinelaw/fresh?style=social) ](https://github.com/sinelaw/fresh)
### [sinelaw fresh](https://github.com/sinelaw/fresh)

**核心内容总结：**

**项目功能**  
Fresh 是一款基于终端的文本编辑器，支持文件管理、多光标编辑、搜索替换、代码导航、语言服务器（LSP）集成、Markdown 预览等功能，可处理超大文件（多GB级）。

**使用方法**  
支持多平台安装：  
- macOS（Homebrew）、Arch Linux（AUR）、Debian/Ubuntu（.deb）、Fedora/RHEL（.rpm）  
- 预编译二进制文件、npm（全局安装或 npx 临时使用）  
- Rust 用户可通过 `cargo-binstall` 或 crates.io 安装  
- Nix 用户可用 Nix flakes 安装  
- 从源码编译（需 Cargo 和 Rust）  

**主要特性**  
1. **低延迟性能**：快速加载和编辑超大文件。  
2. **现代扩展性**：TypeScript 插件在 Deno 沙箱中运行，支持 LSP、语法高亮、TODO 标记等。  
3. **全面功能**：包含文件管理、智能缩进、多窗口布局、命令面板、Git 集成等。  
4. **跨平台兼容**：支持鼠标操作，适合从图形编辑器过渡。  

**许可证**：GNU General Public License v2.0 (GPL-2.0)。