
---
title: opencode
---

### [anomalyco opencode](https://github.com/anomalyco/opencode)  ![GitHub Repo stars](https://img.shields.io/github/stars/anomalyco/opencode?style=social)

**核心内容总结：**  
OpenCode 是一个开源的 AI 编码代理工具，提供终端和桌面应用版本，支持多平台（Windows、macOS、Linux）安装。  

**功能与特性：**  
1. **核心功能**：  
   - 提供两个内置代理模式：  
     - **build**（默认）：支持开发全流程操作。  
     - **plan**（只读）：用于代码分析和规划，禁止文件修改，需授权执行命令。  
   - 内置 **general** 子代理，支持复杂搜索和多步骤任务。  

2. **技术特性**：  
   - 支持多种大模型（如 Claude、OpenAI、Google 等），不绑定特定提供商。  
   - 原生集成语言服务器协议（LSP）。  
   - 客户端/服务器架构，支持远程控制。  
   - 聚焦终端用户界面（TUI），由 Neovim 用户和 terminal.shop 团队开发。  

**使用方法：**  
- **安装方式**：  
  - 一键安装：`curl -fsSL https://opencode.ai/install | bash`。  
  - 包管理器：`npm i -g opencode-ai`、`brew install opencode` 等。  
- **桌面应用**：从 GitHub 发布页或官网下载对应平台安装包（如 `.dmg`、`.exe`、`.deb` 等）。  

**其他**：  
- 文档和社区支持：提供官方文档（[opencode.ai/docs](https://opencode.ai/docs)）、Discord 社群和 X.com 官号。