
---
title: claude-code-hooks-mastery
---

### [disler claude-code-hooks-mastery](https://github.com/disler/claude-code-hooks-mastery)  ![GitHub Repo stars](https://img.shields.io/github/stars/disler/claude-code-hooks-mastery?style=social)

### 项目核心内容总结

**项目名称**：Claude Code Hooks Mastery（Claude Code 钩子大师）

**项目功能**：  
本项目展示了如何使用 [Claude Code 钩子](https://docs.anthropic.com/en/docs/claude-code/hooks) 来对 Claude Code 的行为进行确定性或非确定性的控制。项目包括了对 Claude Code 子代理（Sub-Agents）、元代理（Meta-Agent）以及基于团队的验证系统（Team-Based Validation）的深入讲解和实现。

---

**主要特性**：

1. **钩子生命周期管理**  
   - 实现了 Claude Code 的 13 个钩子生命周期事件的完整覆盖，包括 `UserPromptSubmit`、`PreToolUse`、`PostToolUse`、`SessionStart`、`SessionEnd` 等。
   - 每个钩子支持日志记录、安全检查、上下文注入、错误处理等功能。

2. **钩子错误码与流程控制**  
   - 钩子通过返回不同的退出码（Exit Code）控制流程，如 `0` 表示成功，`2` 表示阻断执行。
   - 支持结构化 JSON 输出，实现更精细的控制，如 `continue`、`decision`、`reason` 字段。

3. **用户输入控制（UserPromptSubmit）**  
   - 用户输入前进行验证、日志记录、上下文增强。
   - 可以阻止危险命令，如 `rm -rf`、`.env` 文件访问等。

4. **工具执行控制（PreToolUse）**  
   - 在工具执行前进行权限检查，防止危险操作。
   - 可以自动阻止或批准某些工具调用，如只读操作自动允许。

5. **子代理系统（Sub-Agents）**  
   - 支持创建多个子代理，每个代理有独立的系统提示、工具权限和上下文窗口。
   - 子代理可以处理特定任务，如代码审查、测试执行、市场分析等。
   - 主代理可以自动选择并调用子代理，实现任务的自动化和并行处理。

6. **元代理（Meta-Agent）**  
   - 一个可以动态创建子代理的高级代理。
   - 支持根据任务需求生成结构化的子代理配置文件。
   - 提升开发效率，快速构建多个功能明确的子代理。

7. **团队验证系统（Team-Based Validation）**  
   - 使用 `/plan_w_team` 命令创建“构建-验证”团队，实现任务的自动化协作。
   - 包括 `Builder`（构建者）和 `Validator`（验证者）两个角色，分别负责任务实现和质量检查。
   - 验证器自动使用 Ruff 和 Ty 检查 Python 代码质量。

8. **输出样式（Output Styles）**  
   - 提供多种输出格式，如 HTML、表格、YAML、Markdown 等，便于不同场景下的使用。
   - 支持通过 `/output-style` 命令切换输出样式。

9. **自定义状态行（Status Lines）**  
   - 提供 9 种状态行脚本，显示实时信息，如 Git 分支、会话时间、模型信息、上下文使用情况等。
   - 可通过 `.claude/settings.json` 设置默认状态行脚本。

10. **日志系统**  
    - 所有钩子事件都会记录到 `logs/` 目录下，便于调试和审计。
    - 包括用户输入日志、工具调用日志、错误日志等。

---

**使用方法**：

1. **安装依赖**  
   - 需要安装 [Astral UV](https://docs.astral.sh/uv/getting-started/installation/) 和 [Claude Code CLI](https://docs.anthropic.com/en/docs/claude-code)。
   - 可选安装 ElevenLabs、Firecrawl、OpenAI、Anthropic、Ollama 等工具。

2. **配置钩子**  
   - 所有钩子脚本位于 `.claude/hooks/` 目录下，每个钩子为一个独立的 Python 脚本。
   - 配置文件 `.claude/settings.json` 定义了每个钩子的路径和参数。

3. **运行命令**  
   - 使用 `claude code` 命令进行交互，钩子会自动触发并执行对应逻辑。
   - 可通过 `/plan_w_team` 创建团队任务，`/output-style` 切换输出样式等。

4. **查看日志**  
   - 日志文件存储在 `logs/` 目录下，可使用 `jq` 等工具解析查看。

---

**项目结构**：

- `.claude/hooks/`：钩子脚本目录。
- `.claude/status_lines/`：状态行脚本目录。
- `.claude/output-styles/`：输出样式目录。
- `.claude/agents/`：子代理定义文件。
- `.claude/commands/`：自定义命令。
- `.claude/settings.json`：钩子配置文件。
- `logs/`：日志目录。
- `ai_docs/`：项目相关文档。

---

**适用对象**：

- 希望深入掌握 Claude Code 钩子系统的开发者。
- 想要构建自动化、智能化的代码辅助系统。
- 有团队协作需求，希望通过 AI 代理实现任务分工与验证。