
---
title: just
---

### [casey just](https://github.com/casey/just)  ![GitHub Repo stars](https://img.shields.io/github/stars/casey/just?style=social)

`just` 是一个跨平台的命令运行器，用于在 `justfile` 文件中保存和运行项目特定的命令（称为 recipes）。其语法受 `make` 启发，但设计更简洁，避免了 `make` 的复杂性（例如无需 `.PHONY` 声明）。

核心功能包括：
- **跨平台支持**：兼容 Linux、macOS、Windows 及类 Unix 系统，无额外依赖。
- **命令管理**：支持食谱依赖、模块导入、别名、分组及命令行参数传递。
- **环境配置**：支持加载 `.env` 文件、自定义 Shell、环境变量导出及工作目录控制。
- **脚本能力**：支持编写任意语言的脚本（通过 Shebang 或 `[script]` 属性）。
- **开发体验**：提供静态错误检查、具体的错误信息、食谱列表查看、Shell 自动补全及编辑器语法高亮支持。
- **函数与表达式**：提供丰富的内置函数用于字符串、路径、文件系统操作及系统信息查询。

项目致力于向后兼容性，支持通过多种包管理器安装。