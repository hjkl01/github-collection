
---
title: bun
---

### [oven-sh bun](https://github.com/oven-sh/bun)  ![GitHub Repo stars](https://img.shields.io/github/stars/oven-sh/bun?style=social)

Bun 是一个用于 JavaScript 和 TypeScript 应用的全能工具包，提供单一的可执行文件 `bun`。其核心是基于 Zig 编写并采用 JavaScriptCore 引擎的高性能运行时，作为 Node.js 的即插即用替代品，显著降低启动时间和内存使用。

项目主要功能包括：
1. **运行与打包**：支持 TypeScript 和 JSX 开箱即用，内置打包器支持热更新。
2. **包管理**：兼容 Node.js 的包管理工具（install/add/run），速度更快。
3. **测试**：内置测试运行器，支持 watch 模式、模拟和快照。
4. **内置 API**：提供 HTTP 服务器、WebSocket、文件 I/O、数据库（SQLite、PostgreSQL）、Redis、S3 及网络操作等原生 API。
5. **跨平台**：支持 Linux、macOS 和 Windows 系统。

旨在通过单一工具替代多个开发依赖，兼容现有 Node.js 项目。