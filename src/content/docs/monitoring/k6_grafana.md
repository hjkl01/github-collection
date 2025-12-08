
---
title: k6
---

### [grafana k6](https://github.com/grafana/k6)

**项目核心内容总结：**  
k6 是一款现代负载测试工具，专为 DevOps 时代开发者和测试人员设计，支持通过代码编写测试脚本，集成到 CI/CD 流程中，适用于 HTTP、WebSocket、gRPC 等多种协议。其核心特性包括：  
1. **可配置负载生成**：低配设备也可模拟高并发流量；  
2. **测试代码化**：支持脚本复用、版本控制、CI 集成；  
3. **JavaScript API**：结合 Go 语言性能与 JS 编程熟悉度；  
4. **多协议支持**：覆盖 HTTP、WebSocket、gRPC 等；  
5. **扩展生态**：社区提供丰富扩展插件；  
6. **指标可视化**：支持灵活导出指标至自定义服务；  
7. **Grafana 云集成**：提供测试执行、数据分析等 SaaS 服务。  

**使用方法**：  
通过编写 JavaScript 脚本定义测试场景（如示例中的 HTTP 请求、阈值设置），在 CLI、CI 或 Kubernetes 集群中运行。无需编码用户可通过 [k6 Studio](https://github.com/grafana/k6-studio) 生成脚本。  

**其他**：  
提供详细文档、社区论坛、公开路线图及 AGPL-3.0 开源协议。