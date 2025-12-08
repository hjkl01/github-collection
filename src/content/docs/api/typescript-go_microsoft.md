
---
title: typescript-go
---

### [microsoft typescript-go](https://github.com/microsoft/typescript-go)

**核心内容总结：**

**项目功能**  
该项目是TypeScript的本地端口预览版（TypeScript 7），旨在提供与TypeScript 5.9相近的功能，但部分特性仍在开发中。支持程序创建、解析、类型检查、JSX、构建模式等，但JavaScript推断、声明输出等部分功能尚未完善。

**使用方法**  
- 通过npm安装预览包：`npm install @typescript/native-preview`，使用命令 `npx tsgo` 替代 `tsc`。  
- VS Code用户需安装扩展并设置 `"typescript.experimental.useTsgo": true`。

**主要特性**  
- **已完成**：程序创建、语法解析、类型检查、构建模式、增量构建等。  
- **开发中**：JavaScript推断、JSDoc支持、声明输出、部分目标版本的JS输出。  
- **未就绪**：语言服务（LSP）部分功能、API接口。  
- 长期计划：项目将合并至微软官方TypeScript仓库，当前仓库和问题跟踪器最终会被关闭。