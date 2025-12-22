
---
title: agent
---

### [stakpak agent](https://github.com/stakpak/agent)  ![GitHub Repo stars](https://img.shields.io/github/stars/stakpak/agent?style=social)

Stakpak 是一个开源的 AI DevOps 终端代理工具，旨在通过安全、高效的方式帮助开发者管理基础设施。其核心功能包括：  
- **安全特性**：支持双向 TLS 加密、动态密钥替换、敏感信息脱敏、密码生成等，保障生产环境安全。  
- **DevOps 工具集成**：提供异步任务管理、实时进度追踪、Terraform/Kubernetes/Dockerfile 等代码索引与搜索、CI/CD 配置、云服务商文档检索等功能。  
- **智能代理能力**：通过规则书（Rulebooks）自定义操作流程，支持 AI 生成基础设施代码、调试 Kubernetes、自动化部署等，且内置防护机制阻止高风险操作。  

**使用方法**：  
1. **安装**：支持 Homebrew（`brew install stakpak`）、二进制下载、Docker（`docker pull ghcr.io/stakpak/agent:latest`）等方式。  
2. **运行**：通过 API 密钥（`stakpak` 命令自动创建）或自定义 OpenAI 兼容端点启动，支持本地/远程/混合模式（`--tool-mode` 参数）。  
3. **高级功能**：  
   - 启动 MCP 代理服务器（`stakpak mcp start`），支持多工具模式。  
   - 通过 ACP 协议与 Zed 编辑器集成，实现实时代码分析与 AI 协作。  
   - 管理规则书（Rulebooks）以定义操作规范（如 `stakpak rb apply my-rulebook.md`）。  

**主要特性**：  
- 安全硬加固（如 mTLS、隐私模式）、自适应 AI 学习、可扩展的规则书系统。  
- 支持 Docker 容器化任务、批量操作审批、可逆文件操作等 DevOps 场景优化功能。