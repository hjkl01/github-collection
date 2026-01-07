
---
title: axonhub
---

### [looplj axonhub](https://github.com/looplj/axonhub)  ![GitHub Repo stars](https://img.shields.io/github/stars/looplj/axonhub?style=social)

AxonHub 是一个统一的 AI 开发平台，核心功能包括：

**项目功能**  
1. 提供 OpenAI Chat Completions 和 Anthropic Messages 的统一 API 网关，支持自动格式转换，无需修改现有 SDK 代码即可调用不同模型（如 Claude、GPT、Gemini）。  
2. 支持多数据库部署（TiDB、PostgreSQL、MySQL、SQLite 等），适应不同规模场景需求。  
3. 提供用户权限管理、渠道配置、模型映射、API 密钥分层控制等功能。  

**使用方法**  
- **部署方式**：支持本地开发环境（单机运行）、服务器生产环境（Docker Compose、虚拟机部署）及云数据库（TiDB Cloud、Neon DB）。  
- **配置管理**：通过 YAML 文件或环境变量配置数据库连接、日志级别、端口等参数。  
- **操作流程**：通过管理界面配置 AI 提供商密钥、创建用户角色、设置模型映射规则，并生成 API 密钥供应用调用。  

**主要特性**  
- **跨平台兼容**：兼容 OpenAI、Anthropic、Gemini 等多模型，支持自动 API 格式转换。  
- **灵活管理**：模型与渠道动态映射、多级权限控制、API 密钥分层配置。  
- **高可用部署**：支持云数据库自动扩展、生产环境分布式部署。  
- **开箱即用**：提供一键安装脚本、配置检查工具及详细文档指导。  

项目基于 MIT 许可证开源，依赖 Go 语言构建，集成 Gin 框架、Ent ORM 等技术。