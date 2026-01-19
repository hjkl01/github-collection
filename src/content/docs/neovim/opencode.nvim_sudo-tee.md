
---
title: opencode.nvim
---

### [sudo-tee opencode.nvim](https://github.com/sudo-tee/opencode.nvim)  ![GitHub Repo stars](https://img.shields.io/github/stars/sudo-tee/opencode.nvim?style=social)

Opencode.nvim 是一个 Neovim 插件，用于集成 Opencode AI 编码代理，提供代码编辑、会话管理、上下文操作等功能。核心功能包括：  
1. **AI 交互**：通过快捷键启动临时会话（如 `<leader>o/`），支持代码转换、注释生成、错误修复等操作。  
2. **会话管理**：支持分享、压缩、撤销/重做会话，可切换会话和子会话。  
3. **快照与恢复**：自动创建工作区快照，支持对比差异、还原文件或全部文件至快照状态，并提供撤销还原操作的恢复点。  
4. **权限控制**：通过 `prompt_guard` 配置函数限制 AI 交互的触发条件，防止误操作。  
5. **自定义扩展**：支持用户自定义命令、钩子函数（如文件编辑后触发操作），并可配置高亮主题（如消息角色颜色、快照操作提示等）。  

**使用方法**：安装 Opencode 后，通过 `:Opencode` 命令或快捷键启动功能，配置认证信息（如 LLM 提供商和模型），通过 `/share`、`/undo` 等命令管理会话。  

**主要特性**：轻量级 AI 协作、上下文感知操作、快照版本控制、权限保护机制、高度可定制化界面与行为。