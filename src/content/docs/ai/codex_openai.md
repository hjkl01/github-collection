
---
title: codex
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/openai/codex?style=social) ](https://github.com/openai/codex)
### [openai codex](https://github.com/openai/codex)

**项目核心内容总结：**

Codex CLI 是 OpenAI 推出的本地化代码生成工具，支持通过命令行与代码编辑器（如 VS Code）集成，提供编程辅助功能。  

**功能与使用方法：**  
1. **安装方式**：支持 npm 全局安装（`npm install -g @openai/codex`）或 Homebrew 安装（`brew install --cask codex`），亦可从 GitHub 发布页下载对应平台的二进制文件。  
2. **启动与登录**：安装后运行 `codex` 命令启动，支持通过 ChatGPT 账户登录（需 Plus/Pro 等订阅计划）或使用 API 密钥（需额外配置）。  
3. **核心特性**：  
   - 支持与 Model Context Protocol（MCP）服务器交互，扩展模型能力。  
   - 提供配置文件（`~/.codex/config.toml`）自定义行为，如执行策略（Execpolicy）限制命令权限。  
   - 支持非交互模式（`codex exec`）实现自动化操作。  

**文档与支持：**  
包含详细配置指南、安全沙箱机制、GitHub Action 集成、TypeScript SDK 等扩展功能，以及常见问题解答（FAQ）。  

**许可证**：采用 Apache-2.0 开源协议。