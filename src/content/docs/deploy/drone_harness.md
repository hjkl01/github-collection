
---
title: drone
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/harness/drone?style=social) ](https://github.com/harness/drone)
### [harness drone](https://github.com/harness/drone)

Harness Open Source 是一个开源的开发平台，集成了代码托管、自动化 DevOps 流水线、托管开发环境（Gitspaces）和制品仓库等功能，提供端到端的 DevOps 解决方案。

**核心功能：**  
- 提供代码托管、CI/CD 流水线、开发环境（Gitspaces）及制品仓库，支持全栈开发流程。  
- 基于 Drone 的下一代版本，扩展了源代码托管和开发环境能力，未来将与 Drone 的流水线功能实现兼容。  

**使用方法：**  
- 通过 Docker 镜像快速部署：运行 `docker run` 命令，访问 `http://localhost:3000` 启动服务。  
- 本地开发需安装 Node、Go 1.20+、Protobuf 3.21.11 及相关工具，执行 `make build` 构建项目，使用 `./gitness server` 启动服务。  

**主要特性：**  
- 提供 REST API 和 Swagger 文档（`http://localhost:3000/swagger`），支持 API 自动化测试。  
- 内置 CLI 工具，支持用户认证、令牌生成（PAT）及服务管理。  
- 支持注册表一致性测试（`make conformance-test`），确保功能合规性。  
- 开源协议为 Apache 2.0，代码托管于 GitHub，贡献指南详见 CONTRIBUTING.md。