
---
title: gitbutler
---

### [gitbutlerapp gitbutler](https://github.com/gitbutlerapp/gitbutler)  ![GitHub Repo stars](https://img.shields.io/github/stars/gitbutlerapp/gitbutler?style=social)

GitButler 是一款基于 Git 的版本控制工具，允许用户在同一个工作目录中同时处理多个分支，通过“虚拟分支”技术实现并行开发。其核心功能包括：  
1. **虚拟分支**：无需切换分支即可并行处理多个任务，可随时将修改分配到不同虚拟分支并单独推送或创建 Pull Request。  
2. **提交管理**：支持拖拽操作实现提交的撤销、合并或拆分。  
3. **GitHub 集成**：支持认证后直接创建 PR、查看分支状态等。  
4. **AI 辅助**：自动生成提交信息和分支名称（依赖 OpenAI API，未来支持本地模型）。  
5. **其他特性**：SSH 密钥管理、提交签名（GPG/SSH）、操作日志回溯等。  

技术栈基于 Tauri（Rust 后端 + Svelte 前端），适用于需要多分支并行开发、频繁切换任务的场景，例如：在开发功能时临时修复 Bug，或测试他人分支而无需切换上下文。