
---
title: superpowers
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/obra/superpowers?style=social) ](https://github.com/obra/superpowers)
### [obra superpowers](https://github.com/obra/superpowers)

**核心内容总结：**

**项目功能**  
Superpowers 是一个基于“技能”系统构建的软件开发工作流工具，提供从需求设计、计划制定到代码实现的全流程支持。核心功能包括：  
- **交互式设计优化**：通过提问细化需求，分段展示设计文档。  
- **测试驱动开发（TDD）**：强制执行“红-绿-重构”流程，避免冗余代码。  
- **子代理驱动开发**：任务自动拆解，由子代理并行执行，确保计划高效推进。  
- **协作与审查机制**：自动生成实施计划、代码审查检查表，支持分支管理。  

**使用方法**  
1. **安装**：  
   - **Claude Code**：通过插件市场安装 `superpowers` 插件。  
   - **Codex/OpenCode**：执行指定命令下载安装文档（`.codex/INSTALL.md` 或 `.opencode/INSTALL.md`）。  
2. **工作流程**：  
   - **brainstorm**（头脑风暴）：细化需求并保存设计文档。  
   - **write-plan**（编写计划）：拆解任务为可执行的代码片段。  
   - **execute-plan**（执行计划）：子代理并行执行任务，或分批次执行。  
   - **test-driven-development**（测试驱动）：强制测试先行，确保代码质量。  
   - **requesting-code-review**（代码审查）：每步完成后自动审查，拦截问题。  

**主要特性**  
- **自动化技能触发**：无需手动操作，系统根据任务自动调用相关技能。  
- **原则导向**：严格遵循 TDD、YAGNI（按需实现）、DRY（避免重复）等开发准则。  
- **技能库扩展**：包含测试、调试、协作等模块，支持用户自定义新技能。  
- **多平台适配**：支持 Claude Code、Codex、OpenCode 等主流开发环境。