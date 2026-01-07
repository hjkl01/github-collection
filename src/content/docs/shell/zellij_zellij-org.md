
---
title: zellij
---

### [zellij-org zellij](https://github.com/zellij-org/zellij)  ![GitHub Repo stars](https://img.shields.io/github/stars/zellij-org/zellij?style=social)

**项目功能**  
Zellij 是一款面向开发者和运维人员的终端多路复用器，支持自定义布局、多用户协作、插件系统（基于 WebAssembly）、浮动/堆叠窗格以及内置网页客户端（无需终端即可使用）。  

**使用方法**  
- 安装方式：通过操作系统包管理器、下载预编译二进制文件，或使用 `cargo install --locked zellij`。  
- 无需安装即可体验：运行 `bash <(curl -L https://zellij.dev/launch)`。  
- 开发环境搭建：克隆项目后，使用 `cargo xtask run` 构建，`cargo xtask test` 运行测试。  

**主要特性**  
- 简单易用，兼顾高级功能，适合新手和资深用户。  
- 支持通过布局和插件系统实现高度自定义。  
- 独特的 UX 特性：浮动窗格、堆叠布局。  
- 提供网页客户端，可在浏览器中操作终端。  
- 支持多人协作和自动化配置。