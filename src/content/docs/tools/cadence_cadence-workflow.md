
---
title: cadence
---

### [cadence-workflow cadence](https://github.com/cadence-workflow/cadence)  ![GitHub Repo stars](https://img.shields.io/github/stars/cadence-workflow/cadence?style=social)

**核心内容总结：**  
Cadence Workflow 是一个开源平台，用于构建和运行可扩展、容错且长期运行的工作流。其核心功能包括工作流编排引擎、CLI 工具、模式管理、基准测试和金丝雀发布工具。  

**使用方法：**  
1. **启动后端**：通过 `docker compose -f docker/docker-compose.yml up` 命令在本地运行 Cadence 后端服务（支持 Cassandra/MySQL/PostgreSQL 数据库及可选的 Kafka+Elasticsearch）。  
2. **运行示例**：使用 [Go](https://github.com/cadence-workflow/cadence-samples) 或 [Java](https://github.com/cadence-workflow/cadence-java-samples) 示例代码验证功能。  
3. **访问 UI**：通过 http://localhost:8088 查看工作流历史和详细追踪。  

**主要特性：**  
- **多语言支持**：提供 Go、Java 官方 SDK，以及社区维护的 Python 和 Ruby SDK。  
- **CLI 工具**：支持工作流、任务列表、域和集群操作，可通过 Homebrew、Docker 或自行编译安装。  
- **可视化界面**：集成 Web UI（通过 Docker Compose 启动后默认访问）。  
- **附加工具**：包含基准测试、金丝雀发布、数据库模式管理工具（支持 SQL 和 Cassandra）。  

**其他说明：**  
- 通过 Homebrew 安装 CLI 和模式工具，支持版本回退。  
- 社区资源包括 GitHub 讨论区、Slack 频道和 StackOverflow 技术问答。