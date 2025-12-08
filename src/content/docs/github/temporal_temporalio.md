
---
title: temporal
---

### [temporalio temporal](https://github.com/temporalio/temporal)

**核心内容总结**  
Temporal 是一个持久化执行平台，用于构建可扩展且可靠的应用程序。其核心功能是通过 Temporal 服务器自动处理 Workflows（工作流）中的故障和重试，确保任务可靠执行。项目源自 Uber 的 Cadence，由 Temporal Technologies 开发维护。  

**使用方法**  
1. **本地启动**：通过 `brew install temporal` 安装后，执行 `temporal server start-dev` 启动服务器。  
2. **运行示例**：使用 Go 或 Java 的示例代码（如 HelloWorld）配合本地服务器测试。  
3. **CLI 工具**：通过 `temporal operator namespace list` 等命令管理服务器和工作流。  
4. **Web UI**：访问 [http://localhost:8233](http://localhost:8233) 查看工作流执行状态。  

**主要特性**  
- 自动处理故障和重试，保障任务可靠性。  
- 支持多语言（如 Go、Java）开发 Workflows、Activities 和 Workers。  
- 提供 CLI 工具和可视化 Web UI。  
- 开源 MIT 许可证，社区活跃，文档完善。