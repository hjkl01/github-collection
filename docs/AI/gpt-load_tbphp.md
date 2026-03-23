### [tbphp gpt-load](https://github.com/tbphp/gpt-load)  ![GitHub Repo stars](https://img.shields.io/github/stars/tbphp/gpt-load?style=social)

GPT-Load 是一款基于 Go 语言的高性能企业级 AI API 透明代理服务，旨在帮助企业和开发者高效整合多个 AI 服务提供商。

核心功能如下：
- **透明代理**：完全保留原生 API 格式，支持 OpenAI、Google Gemini、Anthropic Claude 等，无需修改业务代码。
- **智能密钥管理**：支持高性能密钥池、分组管理、自动轮换、故障自动恢复及黑名单机制。
- **负载均衡**：支持多上游端点加权负载均衡，提升服务可用性与稳定性。
- **动态配置**：系统设置与分组配置支持热加载，修改后即时生效无需重启服务。
- **管理监控**：提供基于 Vue 3 的可视化后台，具备实时统计、健康检查及详细请求日志功能。
- **高可用架构**：支持分布式主从部署、水平扩展，具备密钥加密存储、双重认证及零拷贝流式传输等特性。

支持 Docker、Docker Compose、源码构建及集群等多种部署方式。