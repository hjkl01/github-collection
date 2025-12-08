
---
title: gofr
---

### [gofr-dev gofr](https://github.com/gofr-dev/gofr)

**GoFr项目核心内容总结**：

**项目功能**  
GoFr是一个面向微服务开发的框架，专注于简化Kubernetes部署和提供开箱即用的可观测性（日志、追踪、指标）。支持构建通用应用，但核心定位是微服务。

**主要特性**  
- 简单API语法与默认REST标准  
- 配置管理、认证中间件、gRPC、HTTP服务（含熔断）、Pub/Sub、健康检查、数据库迁移、定时任务  
- 支持远程调整日志级别、Swagger文档生成、抽象文件系统、WebSocket  
- 提供开箱即用的可观测性能力  

**使用方法**  
- **环境要求**：Go 1.24及以上  
- **安装**：通过`go get -u gofr.dev/pkg/gofr`或导入包`import "gofr.dev/pkg/gofr"`  
- **运行示例**：创建包含`gofr.New()`和路由定义的代码，执行`go run main.go`后访问`localhost:8000/greet`  

**其他**  
- 文档：提供[GoDoc](https://pkg.go.dev/gofr.dev)和[官方文档](https://gofr.dev/docs)  
- 贡献：可通过提交PR、撰写教程等方式参与，贡献者可获纪念品  
- 克隆方式：支持HTTPS或SSH克隆仓库  
- 合作伙伴：如JetBrains等。