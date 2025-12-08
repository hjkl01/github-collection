
---
title: mcp-grafana
---

### [grafana mcp-grafana](https://github.com/grafana/mcp-grafana)

**项目核心内容总结：**  
该项目是基于Model Context Protocol（MCP）的Grafana工具，用于连接和管理Grafana实例，支持数据源、告警、日志等操作。主要功能包括：  
1. **连接方式**：支持三种传输模式（stdio、sse、streamable-http），适用于本地开发、实时通信或云环境部署。  
2. **TLS配置**：支持客户端连接Grafana时的TLS认证（证书、CA等），以及服务端HTTPS配置（用于streamable-http模式）。  
3. **健康检查**：提供`/healthz`接口，用于监控服务器状态。  
4. **兼容性**：要求Grafana版本≥9.0（否则部分API会报错）。  

**使用方法**：  
- 通过命令行或Docker运行工具，指定传输模式、TLS参数及Grafana地址。  
- 配置文件支持JSON格式定义TLS证书路径、调试模式等。  
- 开发者可集成到代码中，通过Go语言库调用。  

**主要特性**：  
- 支持多种数据源（Prometheus、Loki等）和告警管理。  
- 提供标准化的CLI工具和程序化接口。  
- 适用于本地测试、云部署及自动化运维场景。