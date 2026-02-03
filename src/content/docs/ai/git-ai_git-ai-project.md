
---
title: git-ai
---

### [git-ai-project git-ai](https://github.com/git-ai-project/git-ai)  ![GitHub Repo stars](https://img.shields.io/github/stars/git-ai-project/git-ai?style=social)

**项目功能：**  
`git-ai` 是一个用于跟踪代码库中由 AI 生成代码的 Git 工具。它支持多种 AI 编码代理工具，能够在提交代码时记录 AI 生成代码的来源、使用的模型和提示内容。通过 Git 的原生功能，它保证 AI 代码的归属信息在合并、重写、变基等 Git 操作中不会丢失。

**使用方法：**  
- **Mac、Linux、Windows（WSL）**：  
  通过命令安装：
  ```bash
  curl -sSL https://usegitai.com/install.sh | bash
  ```
- **Windows（非 WSL）**：  
  通过 PowerShell 安装：
  ```powershell
  powershell -NoProfile -ExecutionPolicy Bypass -Command "irm http://usegitai.com/install.ps1 | iex"
  ```

安装后无需额外配置，即可在所有支持的 AI 编码工具中自动使用。

**主要特性：**  
1. **多代理支持**：支持 Cursor、Claude Code、GitHub Copilot、Droid、Google Gemini 等多个 AI 编码代理。
2. **AI 归属追踪**：记录 AI 生成的每一行代码，并在提交时保存为 Git 注释，支持 AI Blame 和贡献统计。
3. **支持真实 Git 流程**：AI 代码归属信息在合并、重写、变基、挑拣等 Git 操作中不会丢失。
4. **提示与代码关联**：保存生成代码时使用的提示内容，便于后续审查和追溯。
5. **Git 原生 + 高性能**：基于 Git 原生命令构建，对大型仓库影响极小（小于 100ms）。
6. **企业级配置支持**：提供企业部署和自定义配置文档。
7. **数据统计工具（早期访问）**：可聚合 AI 生成数据，分析每个 Pull Request、开发者、仓库和组织的 AI 代码占比、接受率等指标。

**目标：**  
- 实现多代理 AI 代码的统一追踪；
- 提供准确的代码归属信息，从开发到合并全过程；
- 支持复杂 Git 操作；
- 保持提示与代码的关联性；
- 构建高性能、Git 原生的工具。