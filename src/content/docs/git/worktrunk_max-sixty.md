
---
title: worktrunk
---

### [max-sixty worktrunk](https://github.com/max-sixty/worktrunk)  ![GitHub Repo stars](https://img.shields.io/github/stars/max-sixty/worktrunk?style=social)

**Worktrunk 核心内容总结：**

**项目功能**  
Worktrunk 是一个命令行工具（CLI），用于简化 Git 工作树（worktree）管理，专为并行运行 AI 代理（如 Claude Code）设计。通过将工作树与分支名称绑定，自动生成路径，避免手动操作复杂路径。

**主要特性**  
1. **核心命令**：  
   - `wt switch`：切换工作树（类似切换分支）。  
   - `wt create`：一键创建并启动工作树（如配合 Claude Code）。  
   - `wt list`：列出所有工作树及其状态。  
   - `wt remove`：清理工作树。  
2. **自动化功能**：  
   - 钩子（Hooks）：自动执行创建、合并等操作的脚本。  
   - LLM 提交信息：通过 AI 生成提交信息。  
   - 合并工作流：一键合并、整理代码。  
3. **效率提升**：  
   - 避免重复输入分支名和路径，减少手动操作。  
   - 支持多代理并行工作，如多个 Claude Code 实例。  

**使用方法**  
- **安装**：  
  - macOS/Linux：`brew install worktrunk` 或 `cargo install worktrunk`。  
  - Windows：通过 Winget 安装，或使用 `git-wt` 命令。  
- **配置**：安装后运行 `wt config shell install` 启用 shell 集成。  
- **操作示例**：  
  - 创建并启动工作树：`wt switch -c -x claude feat`。  
  - 查看状态：`wt list`。  
  - 清理：`wt remove`。  

**适用场景**  
适合需要同时管理多个 AI 代理任务的开发者，简化 Git 工作流，提升并行开发效率。