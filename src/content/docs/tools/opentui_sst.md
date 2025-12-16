
---
title: opentui
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/sst/opentui?style=social) ](https://github.com/sst/opentui)
### [sst opentui](https://github.com/sst/opentui)

**OpenTUI 核心内容总结：**

OpenTUI 是一个用于构建终端用户界面（TUI）的 TypeScript 库，目前处于开发阶段，暂不适用于生产环境。其核心功能提供独立的命令式 API 和基础组件，支持 SolidJS、React 等框架的集成（Vue 和 Go 绑定为非维护状态）。

**使用方法：**
1. 安装依赖：需先安装 [Zig](https://ziglang.org/)，通过 `bun install @opentui/core` 安装核心库。
2. 快速启动：使用 `bun create tui` 创建项目，或通过脚本直接运行示例。
3. 运行示例：克隆仓库后执行 `bun install`，进入 `packages/core` 目录运行 `bun run src/examples/index.ts`。

**主要特性：**
- 支持多框架集成（React/SolidJS）；
- 提供独立运行的终端 UI 基础能力；
- 包含开发文档及环境变量配置说明；
- 支持通过 [awesome-opentui](https://github.com/msmps/awesome-opentui) 展示基于 OpenTUI 的项目。