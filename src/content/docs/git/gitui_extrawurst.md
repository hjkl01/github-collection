
---
title: gitui
---

### [extrawurst gitui](https://github.com/extrawurst/gitui)

**GitUI核心内容总结：**

**项目功能**  
GitUI是一款基于终端的Git图形化工具，提供类似桌面GUI的操作体验，支持键盘控制、提交、暂存、分支管理、日志浏览、子模块等操作，兼容主流Git功能。

**主要特性**  
- 完全键盘操作，支持上下文帮助（无需记忆快捷键）  
- 支持提交、暂存、重置、分支管理、日志搜索、GPG签名等  
- 异步Git API实现流畅操作，响应式终端UI  
- 支持大仓库（如Linux内核90万提交）高效处理  
- 提供主题自定义、快捷键配置功能  

**使用方法**  
1. **安装**：支持Arch、Fedora、Homebrew、Windows包管理器（Scoop/Chocolatey）等安装命令，或通过[发布页面](https://github.com/gitui-org/gitui/releases)下载二进制文件。  
2. **构建**：需Rust 1.82+，OpenSSL依赖（需perl和C编译器），通过`cargo install gitui --locked`安装。  
3. **调试**：启用日志功能使用`gitui -l`，日志路径根据系统自动适配。  

**限制**  
- 不支持稀疏仓库、Git LFS  
- HTTPS凭证需显式配置  
- 当前非Git命令行替代工具，但可协同使用