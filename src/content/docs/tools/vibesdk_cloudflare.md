
---
title: vibesdk
---

### [cloudflare vibesdk](https://github.com/cloudflare/vibesdk)

**项目核心内容总结：**

Cloudflare VibeSDK 是一个基于 Cloudflare 平台的开发工具包，用于快速构建和部署 AI 驱动的 Web 应用程序。其主要功能包括：

- **AI 集成**：支持多种 AI 服务（如 OpenAI、Anthropic、Google AI Studio 等），可实现智能对话、内容生成等功能。
- **云原生部署**：基于 Cloudflare Workers、Durable Objects、D1 数据库、R2 存储等，实现无服务器架构部署。
- **容器化运行环境**：支持在沙箱容器中运行生成的应用，确保安全与隔离。
- **本地开发与调试**：提供本地开发环境，支持快速测试和部署。

**使用方法：**

1. **克隆项目**：从 GitHub 克隆项目并安装依赖（支持 npm、yarn、bun 等）。
2. **配置环境变量**：设置 Cloudflare API Token、Account ID 等必要参数。
3. **运行开发服务器**：使用 `bun run dev` 启动本地开发环境。
4. **部署到 Cloudflare**：使用 `bun run deploy` 命令进行构建和部署。

**主要特性：**

- 支持多种 AI 模型接入与集成。
- 提供沙箱容器运行机制，保障应用运行安全。
- 提供本地开发环境和自动化部署流程。
- 支持数据库、存储、路由等 Cloudflare 服务的无缝集成。
- 提供完善的权限管理、安全机制（如加密密钥、审计日志等）。

**适用场景：**

适用于需要快速构建 AI 驱动的 Web 应用、无服务器架构开发、云原生部署的开发者和团队。