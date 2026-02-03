
---
title: deno
---

### [denoland deno](https://github.com/denoland/deno)  ![GitHub Repo stars](https://img.shields.io/github/stars/denoland/deno?style=social)

**Deno 是一个 JavaScript、TypeScript 和 WebAssembly 运行时环境，具有安全默认设置和优秀的开发者体验。** 它基于 V8 引擎、Rust 和 Tokio 构建。

### 核心功能：
- 支持 JavaScript、TypeScript 和 WebAssembly；
- 默认具有安全机制，运行程序时需要明确授权访问网络、文件系统等资源；
- 提供现代开发工具链，如模块系统、标准库和包管理（JSR）；
- 可用于构建本地应用、Web 服务器、脚本工具等。

### 使用方法：
- 安装方式包括使用 Shell、PowerShell、Homebrew、Chocolatey、WinGet、Scoop 等；
- 可从源码编译安装；
- 示例：创建一个 `server.ts` 文件，使用 `Deno.serve` 启动一个本地 Web 服务器，通过命令 `deno run --allow-net server.ts` 运行；
- 默认运行时需通过权限标志（如 `--allow-net`）授权资源访问。

### 主要特性：
- 安全性高，权限控制严格；
- 支持现代 JavaScript/TypeScript 特性；
- 集成标准库（@std）和现代包注册中心（JSR）；
- 提供官方文档、博客和社区支持（Discord、Twitter、YouTube 等）。

### 资源链接：
- 官方文档：[Deno Docs](https://docs.deno.com)
- 标准库：[Deno Standard Library](https://jsr.io/@std)
- 包注册中心：[JSR](https://jsr.io/)
- 开发者博客：[Deno Blog](https://deno.com/blog)