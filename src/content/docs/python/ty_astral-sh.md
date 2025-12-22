
---
title: ty
---

### [astral-sh ty](https://github.com/astral-sh/ty)  ![GitHub Repo stars](https://img.shields.io/github/stars/astral-sh/ty?style=social)

ty 是一个用 Rust 编写的超快速 Python 类型检查器和语言服务器，由 Astral 团队开发（该团队还开发了 uv 和 Ruff）。其核心功能包括：  
- **类型检查**：比 mypy 和 Pyright 快 10-100 倍，支持渐进式类型检查、交集类型、类型缩小等高级特性；  
- **语言服务器**：提供代码导航、自动补全、代码操作、增量分析、编辑器集成（支持 VS Code、PyCharm、Neovim 等）；  
- **可配置性**：支持规则级别调整、文件覆盖、抑制注释、项目级配置；  
- **诊断能力**：提供丰富的上下文信息和精准的错误提示。  

**使用方法**：  
- 通过 `uvx ty check` 快速启动；  
- 可访问在线 Playground（[play.ty.dev](https://play.ty.dev)）体验；  
- 安装和编辑器集成需参考官方文档。  

**适用场景**：适合需要高性能类型检查、复杂类型系统支持及强大 IDE 集成的 Python 项目。