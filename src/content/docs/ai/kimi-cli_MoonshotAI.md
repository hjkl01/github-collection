
---
title: kimi-cli
---

### [MoonshotAI kimi-cli](https://github.com/MoonshotAI/kimi-cli)  ![GitHub Repo stars](https://img.shields.io/github/stars/MoonshotAI/kimi-cli?style=social)

**Kimi Code CLI 核心内容总结**

**项目功能：**  
Kimi Code CLI 是一个运行在终端中的 AI 代理程序，旨在帮助用户完成软件开发任务和终端操作。它可以读取和编辑代码、执行 shell 命令、搜索和获取网页内容，并在执行过程中自主规划和调整操作。

**使用方法：**  
1. 安装后，通过终端运行 `kimi` 命令启动。  
2. 可通过 [文档](https://moonshotai.github.io/kimi-cli/zh/) 了解详细使用方式。  
3. 支持与 VS Code、Zed、JetBrains 等 IDE 集成，作为 ACP 代理使用。  
4. 支持 Zsh 插件，通过快捷键 `Ctrl-X` 切换代理模式。  
5. 可通过 `kimi mcp` 管理 MCP 服务器，或通过配置文件连接 MCP 服务。

**主要特性：**  
- **Shell 命令模式**：支持在不离开 Kimi 的情况下直接运行 shell 命令（部分内置命令暂不支持）。  
- **VS Code 插件**：提供 VS Code 扩展，增强代码开发体验。  
- **ACP 集成**：支持与任意 ACP 兼容的编辑器或 IDE 集成（如 Zed、JetBrains）。  
- **Zsh 插件支持**：通过插件与 Zsh 集成，增强 shell 使用体验。  
- **MCP 支持**：支持 MCP 协议工具，可连接多种 MCP 服务。  
- **开发支持**：提供完整的开发文档和构建命令，便于开发者参与项目。