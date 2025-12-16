
---
title: localstack
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/localstack/localstack?style=social) ](https://github.com/localstack/localstack)
### [localstack localstack](https://github.com/localstack/localstack)

**核心内容总结：**

**项目功能**  
LocalStack 是一个本地云开发框架，用于在本地运行和测试 AWS 应用程序。它模拟了 AWS 的多项服务（如 Lambda、S3、DynamoDB、SQS 等），允许开发者无需连接真实云服务即可进行开发和测试。Pro 版本支持更多高级功能。

**使用方法**  
1. **安装**：支持通过 Homebrew、二进制文件下载或 PyPI 安装 LocalStack CLI。  
2. **启动**：使用 `localstack start` 命令在 Docker 容器中运行。  
3. **交互**：通过 `awslocal` CLI 调用本地模拟的 AWS 服务（例如创建 SQS 队列）。  
4. **其他方式**：支持 Docker、Docker Compose、Helm 等部署方式。

**主要特性**  
- 支持多种 AWS 服务，覆盖广泛。  
- 提供详细的文档、CI 集成和开发工具（如桌面客户端、Docker 插件）。  
- 开源社区驱动，支持贡献和扩展。  
- 提供免费版和 Pro 版（付费），后者包含更多功能。  

**其他**  
- 项目遵循 Apache 2.0 协议，提供 End-User License Agreement。  
- 社区支持通过 Slack、GitHub Issues 等渠道。