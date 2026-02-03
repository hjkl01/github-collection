
---
title: oh-my-opencode
---

### [code-yeongyu oh-my-opencode](https://github.com/code-yeongyu/oh-my-opencode)  ![GitHub Repo stars](https://img.shields.io/github/stars/code-yeongyu/oh-my-opencode?style=social)

**项目核心内容总结：**

**功能**  
Oh My OpenCode 是 OpenCode 的增强插件，提供多模型协作、自动化任务、代码分析、文档检索等功能，支持复杂开发场景下的高效协作。

**使用方法**  
- **人类用户**：通过 LLM 代理（如 Claude Code）执行安装指令，或直接阅读安装文档。  
- **LLM 代理**：使用 `curl` 命令获取安装指南并执行。  
- **卸载**：移除插件配置、删除用户/项目配置文件，并验证卸载结果。

**主要特性**  
1. **多代理协作**：主代理 Sisyphus 协调 Prometheus（规划）、Oracle（调试）、Librarian（文档检索）等子代理，支持并行任务处理。  
2. **代码工具**：集成 LSP 与 AST 工具，实现精准重构、代码搜索与诊断。  
3. **自动化任务**：内置 `git-master`（原子提交）、`playwright`（浏览器自动化）等技能，支持 Ralph Loop、Todo 强制执行等生产力工具。  
4. **扩展性**：支持自定义 MCP（如 Exa 搜索、GitHub 代码检索），配置灵活，支持 JSONC 格式注释。  
5. **兼容性**：适配 OpenCode，兼容 Claude Code、AmpCode 等工具特性，提供更稳定的多模型调度。  

**注意事项**  
- 若使用 OpenCode 1.0.132 及以下版本，需升级以避免配置问题。  
- 安装后建议使用 `ultrawork` 或 `ulw` 关键字触发完整任务流程，无需手动管理上下文。