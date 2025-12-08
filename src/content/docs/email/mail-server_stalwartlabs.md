
---
title: mail-server
---

### [stalwartlabs mail-server](https://github.com/stalwartlabs/mail-server)

**核心内容总结：**  
Stalwart 是一个功能完整的开源邮件与协作平台，支持标准协议（如 SMTP、IMAP、JMAP、CalDAV、CardDAV 等）及现代特性（如 DMARC、TLS 报告、Webhook 通知等）。其主要功能包括：  
- **全面协议支持**：覆盖邮件收发、日历、联系人管理等。  
- **企业级功能**：如两步验证、OpenID Connect 认证、OAuth 2.0 授权、ACL 控制等。  
- **可观测性**：集成 OpenTelemetry、Prometheus，提供日志、指标、告警和实时监控。  
- **管理界面**：支持 Web 控制台，可管理账户、域名、队列、日志等。  
- **部署灵活**：支持 Linux/MacOS/Windows/Docker，兼容 Kubernetes、Docker Swarm 等容器编排工具。  

**使用方法**：  
通过官方文档（[stalw.art/docs](https://stalw.art/docs/install/get-started)）选择对应平台安装，或通过 Docker 部署。  

**主要特性**：  
- 支持多种存储后端（如 SQL、Redis）和消息队列（如 Kafka、NATS）。  
- 提供企业级许可证（需付费）以获取优先支持。  
- 社区驱动开发，通过 GitHub 提交功能建议并投票优先级。  
- 项目已实现功能完整，当前重点优化性能和数据库架构，计划发布 1.0 版本。  

**许可证**：  
采用 AGPL-3.0 开源协议，或企业专有 SELv1 许可证（商业用途）。