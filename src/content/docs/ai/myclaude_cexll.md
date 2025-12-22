
---
title: myclaude
---

### [cexll myclaude](https://github.com/cexll/myclaude)  ![GitHub Repo stars](https://img.shields.io/github/stars/cexll/myclaude?style=social)

**项目核心内容总结：**

**项目功能**  
Claude Code Multi-Agent Workflow System 是一个基于多AI后端（Codex/Claude/Gemini）的开发自动化系统，通过分离 **Orchestrator（Claude Code负责规划与协调）** 和 **Executor（codeagent-wrapper负责代码执行）** 的双代理架构，实现复杂开发任务的自动化处理。

**主要特性**  
1. **多后端执行**：根据任务自动选择模型（`--backend codex|claude|gemini`），如Codex执行代码、Claude处理逻辑、Gemini用于原型设计。  
2. **多样化工作流**：  
   - **Dev Workflow**：支持90%测试覆盖率、任务并行执行，适合功能开发与重构。  
   - **BMAD敏捷流程**：包含6个角色（产品负责人、架构师等），适用于大型项目协作。  
   - **需求驱动流程**：快速生成代码原型。  
   - **开发基础命令**：直接执行代码编写、调试、测试等任务。  
3. **企业级功能**：集成GitHub工作流（如自动生成Issue、准备PR）、技能钩子（自动化测试/审查）及模块化配置。  
4. **强制质量管控**：如测试覆盖率门禁、失败回滚机制。

**使用方法**  
1. **安装**：  
   ```bash  
   git clone https://github.com/cexll/myclaude.git  
   cd myclaude  
   python3 install.py --install-dir ~/.claude  
   ```  
   可选模块安装（如`--module dev`）或强制覆盖（`--force`）。  

2. **执行命令**：  
   - 开发任务：`/dev "实现JWT认证"`  
   - 快速调试：`/debug` 或 `/code`  
   - 多任务并行：  
     ```bash  
     codeagent-wrapper --parallel <<'EOF'  
     ---TASK---  
     id: backend_api  
     workdir: /project/backend  
     ---CONTENT---  
     实现REST接口  
     EOF  
     ```  

**适用场景**  
- 新功能开发（推荐`/dev`）  
- 大型项目协作（`/bmad-pilot`）  
- 快速原型（`/requirements-pilot`）  
- 代码审查、性能优化（`/review`、`/optimize`）