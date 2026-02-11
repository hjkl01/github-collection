
---
title: gpt-load
---

### [tbphp gpt-load](https://github.com/tbphp/gpt-load)  ![GitHub Repo stars](https://img.shields.io/github/stars/tbphp/gpt-load?style=social)

### GPT-Load 核心内容总结

#### 项目简介  
GPT-Load 是一个高性能、企业级的 AI API 透明代理服务，专为企业和开发者设计，用于集成多个 AI 服务。该项目使用 Go 语言编写，具备智能密钥管理、负载均衡、全面监控等功能，适用于高并发生产环境。

#### 主要功能  
- **透明代理**：完全保留原生 API 格式，支持 OpenAI、Google Gemini、Anthropic Claude 等多种格式。
- **智能密钥管理**：高性能密钥池，支持按组管理、自动轮换、失败恢复。
- **负载均衡**：支持多上游端点的加权负载均衡，提高服务可用性。
- **智能失败处理**：自动密钥黑名单管理和恢复机制，确保服务连续性。
- **动态配置**：系统设置和组配置支持热加载，无需重启。
- **企业架构**：支持分布式主从部署，水平扩展和高可用。
- **现代管理界面**：基于 Vue 3 的 Web 管理界面，直观易用。
- **全面监控**：实时统计、健康检查和详细请求日志。
- **高性能设计**：零拷贝流式处理、连接池复用、原子操作。
- **生产就绪**：优雅关闭、错误恢复和全面安全机制。
- **双重认证**：管理端和代理端的独立认证，代理认证支持全局和组级密钥。

#### 支持的 AI 服务  
- **OpenAI 格式**：官方 OpenAI API、Azure OpenAI 等兼容服务。
- **Google Gemini 格式**：Gemini Pro、Gemini Pro Vision 等模型。
- **Anthropic Claude 格式**：Claude 系列模型。

#### 使用方法  
1. **Docker 快速启动**  
   使用 Docker 镜像快速部署，支持环境变量配置密钥和数据存储路径。

2. **Docker Compose（推荐）**  
   提供完整的 `.env` 配置文件，支持 SQLite、MySQL、PostgreSQL 和 Redis，推荐用于生产部署。

3. **源码构建**  
   要求本地安装数据库和 Redis（可选），通过 `go mod` 安装依赖，运行服务。

4. **集群部署**  
   支持多节点部署，所有节点连接统一的数据库和 Redis，推荐使用 MySQL/PostgreSQL 和 Redis 集群。

#### 配置系统  
- **静态配置**：通过环境变量设置，如数据库连接、端口、认证密钥等，需重启生效。
- **动态配置**：通过数据库配置，支持热加载，无需重启服务，优先级为：组配置 > 系统设置 > 环境配置。

#### 数据加密迁移  
- 支持 API 密钥的加密存储，可随时启用、禁用或更换加密密钥。
- 提供 Docker Compose 和源码部署的迁移命令，操作前需备份数据库，防止数据丢失。

#### Web 管理界面  
- 提供实时统计、密钥管理、请求日志、系统设置等功能。
- 支持创建 AI 服务组、添加和管理 API 密钥、查看请求历史等。

#### API 使用指南  
- 通过组名路由请求到不同 AI 服务。
- 代理接口格式为：`http://localhost:3001/proxy/{group_name}/{original_api_path}`。
- 支持 OpenAI、Gemini、Anthropic 等接口示例，只需替换原始地址和密钥为代理地址和代理密钥即可使用。

#### 相关项目  
- [New API](https://github.com/QuantumNous/new-api)：优秀的 AI 模型聚合管理与分发系统。

#### 开源协议  
- MIT 协议，详情见 [LICENSE](LICENSE) 文件。