
---
title: ralph-orchestrator
---

### [mikeyobrien ralph-orchestrator](https://github.com/mikeyobrien/ralph-orchestrator)  ![GitHub Repo stars](https://img.shields.io/github/stars/mikeyobrien/ralph-orchestrator?style=social)

**项目核心内容总结：**

**项目功能：**  
Ralph Orchestrator 是一个基于 AI 的自动化任务协调工具，支持多步骤流程管理、代码生成、文档编写、调试分析等场景。通过模块化角色（Hats）分工协作，结合共享内存（Scratchpad）和质量控制（Backpressure）机制，实现复杂任务的自动化执行。

**主要特性：**  
1. **模块化角色（Hats）**：支持任务分解为不同角色（如调试、代码生成、文档编写等），每个角色可定义触发条件、输出事件及执行逻辑。  
2. **共享内存（Scratchpad）**：所有角色共享 `.agent/scratchpad.md` 文件，用于跨步骤保存任务状态、上下文及进度标记（如 `[ ]`、`[x]`）。  
3. **质量控制（Backpressure）**：强制要求构建结果包含测试、代码检查、类型校验等通过证明（如 `tests: pass, lint: pass`）。  
4. **多后端支持**：兼容 Claude、Kiro、Gemini 等 AI 接口，可通过配置文件灵活切换。  
5. **事件驱动架构**：支持事件记录与回放（JSONL 格式），便于调试与测试。  

**使用方法：**  
1. **初始化配置**：通过 `ralph init` 创建 `ralph.yml` 配置文件，可指定后端（如 `--backend gemini`）或预设流程（如 `--preset tdd-red-green`）。  
2. **执行任务**：  
   - 运行流程：`ralph run -p "任务描述"` 或 `ralph run -P prompt.txt`。  
   - 恢复中断任务：`ralph resume`。  
   - 查看事件日志：`ralph events`。  
3. **高级功能**：  
   - 交互式规划：`ralph plan` 生成任务计划。  
   - 代码生成：`ralph task` 根据描述生成代码。  
   - 测试与录制：`--record-session` 记录会话日志用于回放测试。  

**适用场景：**  
- 代码生成与重构（如 `refactor`、`spec-driven` 预设）。  
- 调试与问题分析（如 `debug`、`incident-response` 预设）。  
- 文档编写与知识整理（如 `docs`、`documentation-first` 预设）。  
- 多角色协作流程（如 `mob-programming`、`pr-review` 预设）。