
---
title: incubator-devlake
---

### [apache incubator-devlake](https://github.com/apache/incubator-devlake)

**Apache DevLake（孵化中）核心内容总结：**  

**项目功能**  
Apache DevLake 是一个开源的开发数据平台，用于整合、分析和可视化来自 DevOps 工具的碎片化数据，帮助团队提升工程效率、开发者体验和社区增长。支持通过预置仪表盘实现 DORA 指标、敏捷回顾等常见目标的度量，并可通过 SQL 自定义扩展分析。  

**主要特性**  
- **多数据源支持**：兼容 GitHub、GitLab、Jenkins、Jira、Sonarqube 等主流工具。  
- **灵活扩展**：可通过插件机制添加新数据源、指标和仪表盘。  
- **预置仪表盘**：提供工程负责人、开源项目维护者的实时分析看板（如 DORA 指标）。  
- **统一数据视图**：打破数据孤岛，整合软件开发生命周期（SDLC）全链路数据。  

**使用方法**  
1. **安装**：通过 [Docker Compose](https://devlake.apache.org/docs/GettingStarted/DockerComposeSetup) 或 [Helm](https://devlake.apache.org/docs/GettingStarted/HelmSetup) 部署。  
2. **配置**：通过图形化界面创建“Blueprint”定义数据连接、采集范围及同步频率。  
3. **分析**：查看预置仪表盘，或使用 SQL 自定义指标。  

**其他**  
- 提供中文文档和社区支持（Slack、邮件列表）。  
- 开源协议为 Apache License 2.0。