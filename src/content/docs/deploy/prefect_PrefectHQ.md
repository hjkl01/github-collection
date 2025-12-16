
---
title: prefect
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/PrefectHQ/prefect?style=social) ](https://github.com/PrefectHQ/prefect)
### [PrefectHQ prefect](https://github.com/PrefectHQ/prefect)

**核心内容总结：**  
Prefect 是一个用于构建数据流水线的 Python 工作流编排框架，支持自动化、重试、依赖管理及复杂分支逻辑。  

**功能与特性：**  
- 通过 `flow` 和 `task` 装饰器简化脚本转为生产级工作流，支持调度、缓存、事件触发等。  
- 可部署至本地自托管服务器或 Prefect Cloud，提供可视化监控与管理界面。  
- 提供轻量级客户端库 `prefect-client`，适用于临时执行环境与远程服务器交互。  

**使用方法：**  
1. 安装：`pip install prefect` 或 `uv add prefect`。  
2. 编写脚本：使用装饰器定义任务与流程（如示例中的 GitHub 星标统计）。  
3. 运行：本地启动 Prefect 服务器（`prefect server start`）或通过 `serve` 方法部署为定时任务。  

**其他：**  
支持与 Prefect Cloud 集成，提供团队协作、工具扩展等企业级功能，社区资源包括文档、Slack 群组、YouTube 教程等。