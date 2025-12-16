
---
title: avante.nvim
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/yetone/avante.nvim?style=social) ](https://github.com/yetone/avante.nvim)
### [yetone avante.nvim](https://github.com/yetone/avante.nvim)

**avante.nvim** 是一个基于 Neovim 的 AI 辅助插件，核心功能包括：  
1. **AI 代码交互**：支持与当前文件、选中代码块、项目整体（通过 `@codebase`）对话，生成代码、分析问题、提供修改建议。  
2. **工具集成**：自动执行文件操作、Bash 命令、网络搜索等工具，支持禁用特定工具（如 `bash`、`python`）。  
3. **模式切换**：提供两种交互模式——  
   - **Agentic 模式**：AI 自动执行工具完成任务；  
   - **Legacy 模式**：仅提供建议，需手动确认操作。  
4. **扩展性**：兼容 LSP、Tree-sitter，支持与其他插件（如 `nvim-tree`）集成，可自定义文件选择/取消选择操作。  
5. **模板自定义**：通过 Jinja 模板文件（如 `*.avanterules`）自定义不同模式（规划、编辑、建议）的交互逻辑。  

**使用方法**：  
- 安装后通过配置文件设置模式、禁用工具或扩展插件；  
- 使用 `/` 命令触发 AI 功能，或通过 `@codebase` 与项目对话；  
- 集成扩展模块（如 `nvim-tree`）实现文件管理功能。  

**主要特性**：  
- 智能 Tab（Cursor Flow）导航；  
- 支持 MCP（多上下文规划）和 ACP（自动代码补全）；  
- 高度可定制的交互流程与模板系统；  
- 与主流开发工具深度集成，提升代码分析与修改效率。