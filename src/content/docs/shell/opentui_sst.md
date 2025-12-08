
---
title: opentui
---

### [sst opentui](https://github.com/sst/opentui)

**项目功能**  
OpenTUI 是一个用于构建终端用户界面（TUI）的 TypeScript 库，目前处于开发阶段，尚未适用于生产环境。它将作为 opencode 和 terminaldotshop 的基础 TUI 框架，提供核心库（支持独立运行）、SolidJS/React/Vue 的集成方案（部分模块未维护）。

**使用方法**  
1. **快速开始**：通过 `bun create tui` 命令初始化项目。  
2. **安装依赖**：需先安装 [Zig](https://ziglang.org/)，再使用 `bun install @opentui/core` 安装核心库。  
3. **运行示例**：通过脚本或下载 GitHub 发布版本直接体验示例；从项目根目录运行示例需执行 `bun install` 并进入 `packages/core` 目录执行 `bun run src/examples/index.ts`。

**主要特性**  
- 核心库提供命令式 API 和基础组件，可独立运行。  
- 支持 SolidJS、React 等框架的集成（Vue 和 Go 绑定未维护）。  
- 提供开发文档、环境变量配置及本地开发链接指南。