
---
title: helix
---

### [helix-editor helix](https://github.com/helix-editor/helix)

**项目核心内容总结：**  
Helix 是一个受 Kakoune 和 Neovim 启发、用 Rust 编写的终端编辑器，核心功能包括：  
- **Vim 风格的模态编辑**  
- **多选操作**  
- **内置语言服务器支持**  
- **基于 Tree-sitter 的智能、增量语法高亮与代码编辑**  

**使用方法：**  
- 安装方式见官方文档（[安装指南](https://docs.helix-editor.com/install.html)）  
- 支持通过包管理器安装（如 Repology 提供的版本）  

**主要特性：**  
- 当前已支持部分语言的缩进定义（需查看 `runtime/queries/<lang>/indents.scm`）  
- 计划探索自定义渲染器（如使用 wgpu 或 skulpin）  
- 提供详细的 [键位映射](https://docs.helix-editor.com/keymap.html) 和 [文档](https://docs.helix-editor.com/)  

**其他信息：**  
- 社区支持：可通过 [Matrix 空间](https://matrix.to/#/#helix-community:matrix.org) 讨论  
- 贡献指南见 [CONTRIBUTING.md](./docs/CONTRIBUTING.md)  
- 常见问题解答在 [FAQ](https://github.com/helix-editor/helix/wiki/FAQ)