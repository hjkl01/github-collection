
---
title: just
---

### [casey just](https://github.com/casey/just)  ![GitHub Repo stars](https://img.shields.io/github/stars/casey/just?style=social)

`just` 是一个跨平台的命令运行器，用于保存和运行项目特定的命令。它使用 `justfile` 文件存储任务（recipes），语法受 `make` 启发但更简洁，且作为命令运行器而非构建系统，避免了 `make` 的复杂性和特殊性。

核心功能特性包括：
- **跨平台兼容**：支持 Linux、macOS、Windows 及各类 Unix 系统，无需额外依赖。
- **任务管理**：支持任务依赖、参数传递、工作目录控制及环境变量（.env）加载。
- **脚本灵活性**：支持任意语言脚本（Shebang），内置丰富的函数库（字符串、路径、文件系统、时间等）。
- **易用性**：提供具体且带上下文的错误报告、静态语法检查、命令行补全及主流编辑器集成。
- **扩展性**：支持模块、别名、分组、属性配置、交互式任务选择及全局配置文件。

该工具旨在作为 `make` 的现代化替代方案，简化项目构建与日常开发命令的执行。