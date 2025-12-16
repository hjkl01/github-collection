
---
title: copilot-cli
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/github/copilot-cli?style=social) ](https://github.com/github/copilot-cli)
### [github copilot-cli](https://github.com/github/copilot-cli)

**GitHub Copilot CLI 核心内容总结：**  
该项目将 GitHub Copilot 的 AI 编码辅助功能引入终端，支持通过自然语言与 AI 协作编写、调试和理解代码。核心功能包括：  
1. **终端原生开发**：无需切换上下文，直接在终端使用 AI 协作。  
2. **GitHub 深度集成**：访问仓库、问题和拉取请求，支持现有 GitHub 账户认证。  
3. **代理能力**：支持代码构建、编辑、调试和重构，可执行复杂任务。  
4. **MCP 扩展性**：默认集成 GitHub MCP 服务器，支持自定义扩展。  
5. **完全控制**：所有操作需用户显式确认，确保安全。  

**使用方法**：  
- 安装前提：Node.js 22+、npm 10+，Windows 需 PowerShell 6+，需有效 Copilot 订阅。  
- 安装命令：`npm install -g @github/copilot`，启动命令：`copilot`。  
- 认证方式：通过 `/login` 命令或使用具有 "Copilot Requests" 权限的 PAT（个人访问令牌）。  
- 模型选择：使用 `/model` 命令切换模型（如 Claude Sonnet 4.5、GPT-5），每次请求消耗月度配额。  

**注意事项**：  
- 若组织禁用 Copilot CLI，需联系管理员。  
- 使用 PAT 时需在 GitHub 设置中生成并配置 `GH_TOKEN` 或 `GITHUB_TOKEN`。  
- 每次提交请求会消耗月度配额，具体详见官方文档。